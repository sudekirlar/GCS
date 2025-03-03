(function() {
    // Orijinal metotları saklayalım:
    var proto_initIcon = L.Marker.prototype._initIcon,
        proto_setPos   = L.Marker.prototype._setPos;

    // Marker başlatılırken, ikonun dönüş ayarlarını ekle
    L.Marker.addInitHook(function () {
        var iconOptions = this.options.icon && this.options.icon.options,
            iconAnchor  = iconOptions && iconOptions.iconAnchor;
        if (iconAnchor) {
            iconAnchor = iconAnchor[0] + 'px ' + iconAnchor[1] + 'px';
        }
        // Dönme merkezi: ya marker ayarlarında varsa ya da ikonun merkezi ya da varsayılan 'center bottom'
        this.options.rotationOrigin = this.options.rotationOrigin || iconAnchor || 'center bottom';
        // rotationAngle tanımlı değilse sıfır olarak ayarla (0° dahi uygulanacak)
        if (typeof this.options.rotationAngle === 'undefined') {
            this.options.rotationAngle = 0;
        }
        // Sürükleme sırasında dönüşün korunması için:
        this.on('drag', function(e) { e.target._applyRotation(); });
    });

    L.Marker.include({
    _setPos: function(pos) {
        // pos, {x, y} şeklinde konum bilgisidir.
        var x = pos.x,
            y = pos.y;
        // Hem translate hem de rotate bilgisini birlikte ayarla:
        this._icon.style[L.DomUtil.TRANSFORM] = 'translate3d(' + x + 'px, ' + y + 'px, 0) rotateZ(' + this.options.rotationAngle + 'deg)';

        // Eğer marker'ın gölgesi (shadow) varsa, sadece konum bilgisi uygulanmalı:
        if (this._shadow) {
            this._shadow.style[L.DomUtil.TRANSFORM] = 'translate3d(' + x + 'px, ' + y + 'px, 0)';
        }
    },

    setRotationAngle: function(angle) {
        this.options.rotationAngle = angle;
        // Marker güncelleniyor:
        if (this._map) {
            this.update();
        }
        return this;
    }
});

})();
