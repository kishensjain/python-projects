from src.sensor import TemperatureSensor
from src.modes import HeatMode, CoolMode, OffMode
import json
class ThermostatController:
    def get_current_temperature(self):
        sensor = TemperatureSensor()
        try:
            curr_temp = sensor.read_temperature()
            return curr_temp
        except Exception as e:
            return e
    
    def determine_mode(self, temperature):
        with open("src/temp_thresholds.json", "r") as f:
            thresholds = json.load(f)
        min_temp = thresholds["heating"]["min_temperature"]
        max_temp = thresholds["heating"]["max_temperature"]
        if temperature < min_temp:
            return HeatMode()
        elif temperature > max_temp:
            return CoolMode()
        else:
            return OffMode()
    
    def get_mode(self):
        temperature = self.get_current_temperature()
        mode = self.determine_mode(temperature)
        return mode