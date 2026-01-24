import pygame
import pytest

from robot.xbox_joystick import XboxJoystick
from robot.xbox_state import XboxState

def test_state():
    joystick = XboxJoystick().connect()

    assert True
