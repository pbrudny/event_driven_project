from .base_event.py import Event

class MotionDetectedEvent(Event):
    def __init__(self):
        super().__init__("motion_detected", {})
