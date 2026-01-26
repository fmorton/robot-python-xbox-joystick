import pygame
import pytest

from robot.xbox_joystick import XboxJoystick

joystick = XboxJoystick().connect()

def test_xbox_joystick():
    print("Joystick connected")

    running = True

    while running:
        for event in pygame.event.get():
            if joystick.quit_event(event):
                running = False
            elif event.type == pygame.JOYBUTTONDOWN:
                print(f"Button {event.button} pressed on joystick {event.joy}")

                if event.button == 15:  # options button to quit
                    running = False
            elif event.type == pygame.JOYAXISMOTION:
                print(f"Joystick axis {event.axis} value {event.value}")

    assert True


def wheel_speed_calculation(x_axis, y_axis, left_speed_target, right_speed_target, max_speed=1.0):
    left_speed, right_speed = XboxJoystick.wheel_speeds(x_axis, y_axis, max_speed)

    assert left_speed == left_speed_target
    assert right_speed == right_speed_target


def test_wheel_speeds():
    wheel_speed_calculation(0.0, -1.0, 1.0, 1.0)  #  forward
    wheel_speed_calculation(0.0, -0.5, 0.5, 0.5)  #  forward slow

    wheel_speed_calculation(0.0, 1.0, -1.0, -1.0)  #  backwards
    wheel_speed_calculation(0.0, 0.5, -0.5, -0.5)  #  backwards slow

    wheel_speed_calculation(-1.0, 0.0, -1.0, 1.0)  #  left
    wheel_speed_calculation(-0.5, 0.0, -0.5, 0.5)  #  left slow

    wheel_speed_calculation(1.0, 0.0, 1.0, -1.0)  #  right
    wheel_speed_calculation(0.5, 0.0, 0.5, -0.5)  #  right slow

    wheel_speed_calculation(0.0, -1.0, 1.0, 1.0)  #  forward
    wheel_speed_calculation(0.0, -0.5, 0.5, 0.5)  #  forward slow

    wheel_speed_calculation(1.0, -1.0, 1.0, 0.0)  #  right 45 degrees
    wheel_speed_calculation(0.5, -0.5, 1.0, 0.0)  #  right 45 degrees slow

    wheel_speed_calculation(0.0, -1.0, 100.0, 100.0, 100.0)  #  forward (100 scale)
    wheel_speed_calculation(0.0, -0.5, 50.0, 50.0, 100.0)  #  forward slow (100 scale)


def test_wheel_speed_and_angle():
    speed, angle = XboxJoystick.wheel_speed_and_angle(0.0, -1.0)
    assert speed == 1.0
    assert angle == 90.0

def test_state():  # this code is the same as joystick.run()
        running = True

        while running:
            for event in pygame.event.get():
                if joystick.quit_event(event):
                    running = False
                else:
                    joystick.state.event(event, True)