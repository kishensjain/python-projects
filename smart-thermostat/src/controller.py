from src.sensor import TemperatureSensor

class ThermostatController:
    
    def get_current_temperature(self):
        sensor = TemperatureSensor()
        try:
            return sensor.read_temperature()
        except Exception as e:
            return e
    
    def determine_mode(self, temperature):
        pass