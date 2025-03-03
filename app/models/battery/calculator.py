import logging

class BatteryHealthCalculator:
    @staticmethod
    def calculate(battery, cell_count=3):
        try:
            if not battery:
                return 0.0, "Battery not available"
            max_voltage = 4.2 * cell_count
            current_voltage = battery.voltage if battery.voltage else 0
            if current_voltage <= 0:
                return 0.0, "Invalid voltage reading"
            health_percent = min((current_voltage / max_voltage) * 100, 100)
            health_status = (
                "Excellent" if health_percent >= 85 else
                "Good" if health_percent >= 70 else
                "Fair" if health_percent >= 50 else
                "Poor"
            )
            return health_percent, health_status
        except Exception as e:
            logging.error(f"Battery health calculation error: {str(e)}")
            return 0.0, "Calculation error"