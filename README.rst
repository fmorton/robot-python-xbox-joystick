========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - package
      - | |version| |wheel| |supported-versions|
.. |docs| image:: https://readthedocs.org/projects/robot-python-xbox-joystick/badge/?style=flat
    :target: https://robot-xbox-joystick.readthedocs.io/
    :alt: Documentation Status

.. |github-actions| image:: https://github.com/fmorton/robot-python-xbox-joystick/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/fmorton/robot-xbox-joystick/actions

.. |requires| image:: https://requires.io/github/fmorton/robot-xbox-joystick/requirements.svg?branch=main
    :alt: Requirements Status
    :target: https://requires.io/github/fmorton/robot-xbox-joystick/requirements/?branch=main

.. |codecov| image:: https://codecov.io/gh/fmorton/robot-xbox-joystick/branch/main/graphs/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://codecov.io/github/fmorton/robot-xbox-joystick

.. |version| image:: https://img.shields.io/pypi/v/robot-xbox-joystick.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/robot-xbox-joystick

.. |wheel| image:: https://img.shields.io/pypi/wheel/robot-xbox-joystick.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/robot-xbox-joystick

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/robot-xbox-joystick.svg
    :alt: Supported versions
    :target: https://pypi.org/project/robot-xbox-joystick

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/robot-xbox-joystick.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/robot-xbox-joystick


.. end-badges

Library for basic xbox joystick controllers.

* Free software: MIT License

Installation
============

::

    pip install robot-xbox-joystick

You can also install the in-development version with::

    pip install https://github.com/fmorton/robot-xbox-joystick/archive/main.zip



Xbox Joystick Example
=====================

.. code-block:: python

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


Xbox Joystick Example Using run() and the Joystick State
========================================================

The run() loop maintains the state of the joysticks and all buttons for processing by your supplied method, "robot" in the example below.

.. code-block:: python

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



The joystick.state has the following methods to retrieve the selections from the controller.

.. code-block:: python

  joystick.state.left_x()        # returns x value of left joystick (-1 means max forward/1 max backward)
  joystick.state.left_y()        # returns y value of left joystick (-1 means max left/1 max right)
  joystick.state.left_axis()     # returns left_x, left_y

  joystick.state.right_x()       # returns x value of right joystick (-1 means max forward/1 max backward)
  joystick.state.right_y()       # returns y value of right joystick (-1 means max left/1 max right)
  joystick.state.right_axis()    # returns right_x, right_y

  joystick.state.left_trigger()       # returns left trigger value (0 to 1 if fully pressed)
  joystick.state.right_trigger()      # returns right trigger value (0 to 1 if fully pressed)

  joystick.state.left_trigger_raw()   # returns left trigger unadjusted value (-1 to 1 if fully pressed)
  joystick.state.right_trigger_raw()   # returns right trigger unadjusted value (-1 to 1 if fully pressed)

  joystick.state.button_down_seconds(button)       # how many seconds "button" has been pressed
  joystick.state.button_down_milliseconds(button)  # how many milliseconds "button" has been pressed



The following button constant values are available in XboxJoystick:

.. code-block:: python

  BUTTON_A = 0
  BUTTON_B = 1
  BUTTON_X = 2
  BUTTON_Y = 3
  BUTTON_VIEW = 4   #  left middle button
  BUTTON_XBOX = 5   #  center middle button
  BUTTON_SHARE = 6  # right middle button
  BUTTON_LEFT_JOYSTICK = 7
  BUTTON_RIGHT_JOYSTICK = 8
  BUTTON_LEFT_BUMPER = 9
  BUTTON_RIGHT_BUMPER = 10
  BUTTON_FORWARD = 11
  BUTTON_BACKWARD = 12
  BUTTON_LEFT = 13
  BUTTON_RIGHT = 14



Testing
=======

To run all the tests run::

    pytest -s
