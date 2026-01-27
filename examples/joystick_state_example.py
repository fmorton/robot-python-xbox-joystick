from robot.xbox_joystick import XboxJoystick
from time import sleep


def robot(joystick):
    print("runner", joystick.state.state_string())

    if joystick.state.button_down_milliseconds(XboxJoystick.BUTTON_XBOX):
        return False

    sleep(XboxJoystick.EVENT_LOOP_DELAY)

    return True


joystick = XboxJoystick().connect()

joystick.run(robot)
