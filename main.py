from devices.thermostat import Thermostat
from devices.light_sensor import LightSensor
from devices.security_camera import SecurityCamera
from control.control_center import ControlCenter
from events import communication_queue

# Initialize devices and control center
thermostat = Thermostat()
light_sensor = LightSensor()
security_camera = SecurityCamera()
control_center = ControlCenter()

# Simulate device actions
thermostat.monitor_temperature()
light_sensor.detect_light_level()
security_camera.detect_motion()

# Process events in the queue
while communication_queue:
    event = communication_queue.pop(0)
    control_center.handle_event(event)
