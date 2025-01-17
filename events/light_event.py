from .base_event.py import Event

class LightLevelChangeEvent(Event):
    def __init__(self, light_level):
        super().__init__("light_level_change", {"light_level": light_level})
