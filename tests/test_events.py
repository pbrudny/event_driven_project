from events.temperature_event import TemperatureAlertEvent

def test_temperature_alert_event():
    event = TemperatureAlertEvent(25, "high")
    assert event.name == "temperature_alert"
    assert event.payload["temperature"] == 25
    assert event.payload["alert_type"] == "high"
