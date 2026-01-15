import os
import pygame
import time


class XboxJoystick:
    def __init__(self):
        self.connected = False
        self.joystick = None
        self.joystick_name = None
        self.device_index = None

        os.environ["SDL_VIDEODRIVER"] = "dummy"

        pygame.init()
        pygame.joystick.init()

    def _connect_event(self, event):
        self.device_index = event.device_index
        self.joystick = pygame.joystick.Joystick(self.device_index)
        self.joystick_name = self.joystick.get_name()
        self.connected = True

        return self

    def connect(self, wait_for_joystick_message="Waiting for Xbox Controller"):
        if wait_for_joystick_message:
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.JOYDEVICEADDED:
                        return self._connect_event(event)

                print(wait_for_joystick_message)

                time.sleep(1.0)
