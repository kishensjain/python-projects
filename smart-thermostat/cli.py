from src.controller import ThermostatController
def main():
    thermostat = ThermostatController()
    print(thermostat.get_current_temperature())