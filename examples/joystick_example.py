import pygame
import pytest

from robot.xbox_joystick import XboxJoystick

joystick = XboxJoystick().connect()

print("Joystick connected")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.JOYBUTTONDOWN:
            print(f"Button {event.button} pressed on joystick {event.joy}")

            if event.button == 2:  # 'X' button to quit
                running = False
        elif event.type == pygame.JOYAXISMOTION:
            print(f"Joystick axis {event.axis} value {event.value}")
