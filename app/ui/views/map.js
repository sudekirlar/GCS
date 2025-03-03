"use strict";

// Global değişkenler
var map;             // Leaflet harita nesnesi
var droneMarker;     // Drone simgesini temsil eden marker
var routePoints = []; // Rota noktaları (Python'dan gelen JSON verisi ile güncellenecek)
var routeLine;       // Drone rotasını gösteren polyline
var markers = [];    // Eklenen diğer markerlar
var dynamicZoomEnabled = true; // Varsayılan olarak dinamik zoom aktif

// initMap(): Haritayı başlatır.
function initMap() {
    map = L.map('map').setView([0, 0], 2);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19
    }).addTo(map);

    var droneIcon = L.icon({
        iconUrl: 'assets/icons/drone.png',
        iconSize: [32, 32],
        iconAnchor: [16, 16]
    });

    droneMarker = L.marker([0, 0], {
        icon: droneIcon,
        rotationAngle: 0,
        rotationOrigin: 'center center'
    }).addTo(map);

    routeLine = L.polyline([], {
        color: 'red',
        weight: 3,
        opacity: 0.5,
        smoothFactor: 1
    }).addTo(map);

    // Leaflet event'leri: Eğer orijinal (kullanıcı tarafından tetiklenmiş) event varsa:
    map.on('movestart', function(e) {
        if (e.originalEvent) {
            dynamicZoomEnabled = false;
            console.log("movestart detected (Leaflet): dynamic zoom disabled.");
        }
    });
    map.on('zoomstart', function(e) {
        if (e.originalEvent) {
            dynamicZoomEnabled = false;
            console.log("zoomstart detected (Leaflet): dynamic zoom disabled.");
        }
    });

    // Ekstra: Doğrudan DOM event listener'ları ile de kontrol edelim. (Trigger detection)
    var mapContainer = document.getElementById("map");
    if (mapContainer) {
        mapContainer.addEventListener("mousedown", function(e) {
            dynamicZoomEnabled = false;
            console.log("mousedown detected (DOM): dynamic zoom disabled.");
        });
        mapContainer.addEventListener("touchstart", function(e) {
            dynamicZoomEnabled = false;
            console.log("touchstart detected (DOM): dynamic zoom disabled.");
        });
        mapContainer.addEventListener("wheel", function(e) {
            dynamicZoomEnabled = false;
            console.log("wheel event detected (DOM): dynamic zoom disabled.");
        });
    }

    setTimeout(function() {
        map.invalidateSize();
    }, 500);
}

// updateDrone(): Drone simgesini günceller.
// Burada, gelen yaw değeri Pixhawk'tan (radyan cinsinden) olduğu için dereceye çevriliyor.
function updateDrone(lat, lon, yaw) {
    var yawDegrees = parseFloat(yaw) * 180 / Math.PI; // Radyan -> derece dönüşümü
    droneMarker.setLatLng([lat, lon]);
    droneMarker.setRotationAngle(yawDegrees);
}

// updateMap(): Gelen rota noktalarını polyline olarak çizer ve,
// dynamicZoomEnabled true ise otomatik odaklama uygular.
function updateMap(jsonPoints) {
    try {
        var points = JSON.parse(jsonPoints);
        var polyPoints = points.map(function(entry) {
            return [entry[0], entry[1]];
        });
        routePoints = polyPoints;
        routeLine.setLatLngs(polyPoints);
        console.log("Updated routePoints:", polyPoints);

        if (dynamicZoomEnabled) {
            if (polyPoints.length < 2) {
                map.setView(polyPoints[0], 19);
            } else {
                var bounds = L.latLngBounds(polyPoints);
                console.log("Computed bounds:", bounds);
                map.fitBounds(bounds, { padding: [10, 10] });
            }
        }
        if (points.length > 0) {
            var lastPoint = points[points.length - 1];
            droneMarker.setLatLng([lastPoint[0], lastPoint[1]]);
        }
    } catch (e) {
        console.error("Error parsing routePoints JSON:", e);
    }
}

// addMarker(): Belirtilen koordinatlara marker ekler.
function addMarker(lat, lon) {
    var marker = L.marker([lat, lon]).addTo(map);
    markers.push(marker);
}

// clearMarkers(): Eklenen markerları temizler.
function clearMarkers() {
    markers.forEach(function(marker) {
        map.removeLayer(marker);
    });
    markers = [];
}

// QWebChannel kurulumu: Python tarafındaki bridge nesnesi ile iletişim kurar.
new QWebChannel(qt.webChannelTransport, function(channel) {
    window.bridge = channel.objects.bridge;

    bridge.updateDrone.connect(function(lat, lon, yaw) {
        console.log("updateDrone received:", lat, lon, yaw);
        updateDrone(lat, lon, yaw);
    });

    bridge.updateMap.connect(function(jsonPoints) {
        console.log("updateMap received:", jsonPoints);
        updateMap(jsonPoints);
    });

    bridge.addMarker.connect(function(lat, lon) {
        console.log("addMarker received:", lat, lon);
        addMarker(lat, lon);
    });

    bridge.clearMarkers.connect(function() {
        console.log("clearMarkers received");
        clearMarkers();
    });

    // Go To Focus: Manuel etkileşim sonucu iptal edilmişse, dinamik zoom'u yeniden aktif eder.
    bridge.goToFocus.connect(function() {
        console.log("goToFocus received");
        dynamicZoomEnabled = true;
        if (routePoints.length > 0) {
            if (routePoints.length < 2) {
                map.setView(routePoints[routePoints.length - 1], 19);
            } else {
                var bounds = L.latLngBounds(routePoints);
                map.fitBounds(bounds, { padding: [10, 10] });
            }
        }
    });

    // Clear Path: Rota çizgilerini temizler ve routePoints listesini sıfırlar.
    bridge.clearPath.connect(function() {
        console.log("clearPath received");
        routePoints = [];
        routeLine.setLatLngs([]);
    });
});

// Sayfa yüklendiğinde haritayı başlat.
window.onload = initMap;
