from events.light_event import LightLevelChangeEvent
from events import communication_queue

class LightSensor:
    def detect_light_level(self):
        import random
        light_level = random.choice(["dark", "bright"])
        event = LightLevelChangeEvent(light_level)
        communication_queue.append(event)
        print(f"Event {event.name} emitted with payload {event.payload}!")
