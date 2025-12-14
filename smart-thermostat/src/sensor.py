import random
from src.exceptions import SensorError
class TemperatureSensor:

    def read_temperature(self):
        try:
            return random.randint(10,35)
        except Exception:
            raise SensorError("Failed to read temperature")