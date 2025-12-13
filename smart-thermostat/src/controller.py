from src.sensor import TemperatureSensor
from src.modes import HeatMode, CoolMode, OffMode
import json
from pathlib import Path
class ThermostatController:

    def __init__(self):
        config_path = Path(__file__).parent / "temp_thresholds.json"
        with open(config_path, "r") as f:
            self.thresholds = json.load(f)
    def get_current_temperature(self):
        sensor = TemperatureSensor()
        try:
            return sensor.read_temperature()
        except Exception as e:
            return e
    
    def determine_mode(self, temperature):
        min_temp = self.thresholds["heating"]["min_temperature"]
        max_temp = self.thresholds["heating"]["max_temperature"]
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