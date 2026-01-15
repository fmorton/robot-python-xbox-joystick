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
.. |docs| image:: https://readthedocs.org/projects/robot-xbox-joystick/badge/?style=flat
    :target: https://robot-xbox-joystick.readthedocs.io/
    :alt: Documentation Status

.. |github-actions| image:: https://github.com/fmorton/robot-xbox-joystick/actions/workflows/github-actions.yml/badge.svg
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
import pytest

from robot.xbox_joystick import XboxJoystick

def test_xbox_joystick():
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

    assert True


Testing
=======

To run all the tests run::

    pytest -s
