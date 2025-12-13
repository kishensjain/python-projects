from src.controller import ThermostatController
def main():
    thermostat = ThermostatController()
    print(f"Current temp: {thermostat.get_current_temperature()}")
    print(f"Current mode: {thermostat.get_mode()}")

if __name__ == "__main__":
    main()
