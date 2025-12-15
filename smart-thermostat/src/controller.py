from src.sensor import TemperatureSensor
from src.modes import HeatMode, CoolMode, OffMode
from src.exceptions import ConfigError
import json
from pathlib import Path
class ThermostatController:
    def __init__(self):
        config_path = Path(__file__).parent / "temp_thresholds.json"

        try:
            with open(config_path, "r") as f:
                self.thresholds = json.load(f)
        except Exception as e:
            raise ConfigError("Invalid or missing config file") from e

        try:
            heating = self.thresholds["heating"]
            cooling = self.thresholds["cooling"]

            heating_min = heating["min_temperature"]
            heating_max = heating["max_temperature"]
            cooling_min = cooling["min_temperature"]
            cooling_max = cooling["max_temperature"]

            if not (heating_min < heating_max):
                raise ConfigError("Heating min must be less than heating max")

            if not (cooling_min < cooling_max):
                raise ConfigError("Cooling min must be less than cooling max")

            if heating_max >= cooling_min:
                raise ConfigError(
                    "Heating max must be less than cooling min (ranges overlap)"
                )

        except KeyError as e:
            raise ConfigError(f"Missing config key: {e}") from e

    def get_current_temperature(self):
        sensor = TemperatureSensor()
        try:
            return sensor.read_temperature()
        except Exception as e:
            raise
    
    def determine_mode(self, temperature):
        heating = self.thresholds["heating"]
        neutral = self.thresholds["neutral"]
        cooling = self.thresholds["cooling"]

        if temperature < heating["min_temperature"]:
            return HeatMode()

        elif temperature >= cooling["min_temperature"]:
            return CoolMode()

        else:
            return OffMode()

    
    def get_mode(self):
        temperature = self.get_current_temperature()
        mode = self.determine_mode(temperature)
        return (temperature,mode)