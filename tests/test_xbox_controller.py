import pytest

from robot.xbox_joystick import XboxJoystick
def test_xbox_joystick():
    joystick = XboxJoystick().connect()
    
    assert True

