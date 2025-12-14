from src.controller import ThermostatController
from src.logger import ThermostatLogger
from src.exceptions import ConfigError, SensorError
import time
def main():
    try:
        thermostat = ThermostatController()
        logger = ThermostatLogger()

        while True:
            temperature = thermostat.get_current_temperature()
            mode = thermostat.get_mode()

            print(f"Current temp: {temperature}")
            print(f"Current mode: {mode}")
            print("-" * 30)

            logger.lof(temperature, mode)

            time.sleep(5)
            
    except KeyboardInterrupt:
        print("\nThermostat stopped.")
    
    except ConfigError as e:
        print(f"CONFIG ERROR: {e}")

    except SensorError as e:
        print(f"SENSOR ERROR: {e}")

if __name__ == "__main__":
    main()
