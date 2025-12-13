from src.controller import ThermostatController
from src.logger import ThermostatLogger
def main():
    thermostat = ThermostatController()
    logger = ThermostatLogger()

    temperature = thermostat.get_current_temperature()
    mode = thermostat.get_mode()

    print(f"Current temp: {temperature}")
    print(f"Current mode: {mode}")

    logger.lof(temperature, mode)

if __name__ == "__main__":
    main()
