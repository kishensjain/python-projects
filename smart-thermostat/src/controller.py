from src.sensor import TemperatureSensor
from src.modes import HeatMode, CoolMode, OffMode
class ThermostatController:
    def get_current_temperature(self):
        sensor = TemperatureSensor()
        try:
            curr_temp = sensor.read_temperature()
            return curr_temp
        except Exception as e:
            return e
    
    def determine_mode(self, temperature):
        if temperature < 20:
            return HeatMode()
        elif temperature > 30:
            return CoolMode()
        else:
            return OffMode()
    
    def get_mode(self):
        temperature = self.get_current_temperature()
        mode = self.determine_mode(temperature)
        return mode