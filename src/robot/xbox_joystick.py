import math
import os
import pygame
import time

from robot.xbox_state import XboxState

class XboxJoystick:
    def __init__(self):
        self.connected = False
        self.joystick = None
        self.joystick_name = None
        self.device_index = None
        self.state = XboxState()

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
                print("DEBUG: get an event")
                for event in pygame.event.get():
                    print("DEBUG: startup event",event)
                    if event.type == pygame.JOYDEVICEADDED:
                        return self._connect_event(event)

                print(wait_for_joystick_message)

                time.sleep(1.0)

    def run(self):
        running = True
        debugging = True

        while running:
            for event in pygame.event.get():
                print("Event:", event)
                if event.type in QUEUED_EVENTS:
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.JOYBUTTONDOWN:
                        if debugging:
                            print("Button Pressed:", event.button)


    @classmethod
    def wheel_speeds(cls, x_axis, y_axis, max_speed=1.0):
        """
        Converts joystick axes to differential wheel speeds.
        y_axis: forward/backward (-1 to 1)
        x_axis: left/right (-1 to 1)
        """
        # Simple mapping:
        # Forward: Y is negative, so invert it
        # Turn: X is positive to the right

        speed = -y_axis
        turn = x_axis

        # Calculate speeds
        left_speed = speed + turn
        right_speed = speed - turn

        # Normalize/Clamp values to -1.0 to 1.0
        left_speed = max(-1.0, min(1.0, left_speed)) * max_speed
        right_speed = max(-1.0, min(1.0, right_speed)) * max_speed

        return round(left_speed, 2), round(right_speed, 2)

    @classmethod
    def wheel_speed_and_angle(cls, x_axis, y_axis, max_speed=1.0):
        if abs(x_axis) < 0.25:
            x_axis = 0.0
        if abs(y_axis) < 0.25:
            y_axis = 0.0

        speed = math.sqrt(x_axis**2 + y_axis**2)

        if speed > 1.0:
            speed = 1.0

        angle_rad = math.atan2(-y_axis, x_axis)
        angle_deg = math.degrees(angle_rad)

        # if angle_deg < 0:
        #    angle_deg += 360

        print("Axis:", x_axis, y_axis, "  speed:", speed, "  angle", angle_deg)
        return round(speed, 2), round(angle_deg, 2)
