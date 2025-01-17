from events.temperature_event import TemperatureAlertEvent
from events import communication_queue

class Thermostat:
    def monitor_temperature(self):
        import random
        temperature = random.randint(15, 30)
        alert_type = "low" if temperature < 18 else "high" if temperature > 25 else None
        if alert_type:
            event = TemperatureAlertEvent(temperature, alert_type)
            communication_queue.append(event)
            print(f"Event {event.name} emitted with payload {event.payload}!")
