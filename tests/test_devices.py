from devices.thermostat import Thermostat

def test_thermostat_emits_event():
    thermostat = Thermostat()
    thermostat.monitor_temperature()
    # Additional test logic as needed
