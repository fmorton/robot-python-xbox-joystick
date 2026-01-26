import pygame
import time


class XboxState:
    JOYSTICK_DRIFT = 0.18

    def __init__(self):
        self.axis_value = [0.0, 0.0, 0.0, 0.0, -1.0, -1.0]
        self.button_down_at = [0] * 16
        pass

    def show_value_string(self, value):
        return "{:6.2f}".format(value)

    def state_string(self):
        s = ""
        s = s + self.show_value_string(self.left_x())
        s = s + self.show_value_string(self.left_y())
        s = s + self.show_value_string(self.right_x())
        s = s + self.show_value_string(self.right_y())
        s = s + self.show_value_string(self.left_trigger())
        s = s + self.show_value_string(self.right_trigger())
        for button in range(15):
            down_seconds = self.button_down_seconds(button)

            if down_seconds > 0:
                s += f" button{button:3d} down: {down_seconds:4.2f} seconds"

        return s

    def event(self, event, debugging=False):
        if event.type == pygame.JOYBUTTONUP:
            self.button_down_at[event.button] = 0
        elif event.type == pygame.JOYBUTTONDOWN:
            self.button_down_at[event.button] = time.perf_counter()
        elif event.type == pygame.JOYAXISMOTION:
            value = event.value

            if abs(value) < XboxState.JOYSTICK_DRIFT:
                value = 0.0

            self.axis_value[event.axis] = value
        else:
            print("Unprocessed event:", event)

        if debugging:
            print(self.state_string())

    def left_x(self):
        return self.axis_value[0]

    def left_y(self):
        return self.axis_value[1]

    def left_axis(self):
        return self.left_x(), self.left_y()

    def right_x(self):
        return self.axis_value[2]

    def right_y(self):
        return self.axis_value[3]

    def right_axis(self):
        return self.right_x(), self.right_y()

    def adjusted_trigger_value(self, value):
        return abs((value + 1.0) / 2.0)

    def left_trigger(self):
        return self.adjusted_trigger_value(self.axis_value[4])

    def right_trigger(self):
        return self.adjusted_trigger_value(self.axis_value[5])

    def left_trigger_raw(self):
        return self.axis_value[4]

    def right_trigger_raw(self):
        return self.axis_value[5]

    def button_down_seconds(self, button):
        if self.button_down_at[button] <= 0:
            return 0

        return time.perf_counter() - self.button_down_at[button]

    def button_down_milliseconds(self, button):
        return int(self.button_down_seconds(button) * 1000.0)
