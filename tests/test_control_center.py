from control.control_center import ControlCenter
from events.temperature_event import TemperatureAlertEvent

def test_control_center_handles_temperature_event():
    control_center = ControlCenter()
    event = TemperatureAlertEvent(25, "high")
    control_center.handle_event(event)
    # Additional test logic as needed
