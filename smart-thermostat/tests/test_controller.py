from src.controller import ThermostatController
from src.modes import HeatMode, CoolMode, OffMode

controller = ThermostatController()

def test_heat_mode_when_temp_is_low():
    mode = controller.determine_mode(10)
    assert isinstance(mode, HeatMode)

def test_cool_mode_when_temp_is_high():
    mode = controller.determine_mode(35)
    assert isinstance(mode, CoolMode)

def test_off_mode_when_temp_is_normal():
    mode = controller.determine_mode(25)
    assert isinstance(mode, OffMode)