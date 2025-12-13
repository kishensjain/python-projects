from src.controller import ThermostatController
from src.logger import ThermostatLogger
import time
def main():
    thermostat = ThermostatController()
    logger = ThermostatLogger()

    try:
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

if __name__ == "__main__":
    main()
