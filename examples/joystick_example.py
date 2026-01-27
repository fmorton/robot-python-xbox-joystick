import pygame

from robot.xbox_joystick import XboxJoystick

joystick = XboxJoystick().connect()

print("Joystick connected")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.JOYAXISMOTION:
            print(f"Joystick axis {event.axis} value {event.value}")
        elif event.type == pygame.JOYBUTTONDOWN:
            print(f"Button {event.button} pressed on joystick {event.joy}")

            if event.button == XboxJoystick.BUTTON_XBOX:
                running = False
