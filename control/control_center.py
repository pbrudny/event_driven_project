class ControlCenter:
    def handle_event(self, event):
        if event.name == "temperature_alert":
            print(f"Handling temperature alert: {event.payload}")
        elif event.name == "light_level_change":
            print(f"Handling light level change: {event.payload}")
        elif event.name == "motion_detected":
            print("Handling motion detected event.")
