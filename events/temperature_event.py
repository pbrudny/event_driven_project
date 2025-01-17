from .base_event.py import Event

class TemperatureAlertEvent(Event):
    def __init__(self, temperature, alert_type):
        super().__init__("temperature_alert", {"temperature": temperature, "alert_type": alert_type})
