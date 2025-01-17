from events.motion_event import MotionDetectedEvent
from events import communication_queue

class SecurityCamera:
    def detect_motion(self):
        import random
        if random.choice([True, False]):
            event = MotionDetectedEvent()
            communication_queue.append(event)
            print(f"Event {event.name} emitted!")
