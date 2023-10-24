# Ping Clock

A Raspberry Pi Pico W Powered Ping Clock!

## Bill of Materials

- Raspberry Pi Pico W

- Clock

    - Still need to figure out which to use

- DC Motor

    - Still need to figure out which to use

- Motor Driver 

    - Still need to figure out which to use

## Setup

1. Flash Raspberry Pi Pico W with [Circuit Python](https://circuitpython.org)

2. Install Code

    1. Clone repo or download files for easy copy/paste

    2. Move `code.py` from repo into `CIRCUITPY` Flash Storage

    3. Move `settings.toml.dist` (and rename as `settings.toml`) into 
    `CIRCUITPY` Flash Storage

    4. OPTIONAL. Move `rename_drive.py`, and rename as `boot.py` into
    `CIRCUITPY` Flash Storage to rename the drive to `PING_CLOCK`.
        - Note: Delete boot.py after a reboot and storage is renamed.

3. TODO: Finish this Setup List. (Probably go over how to wire up the Motor and
driver to the pico?)

## Resources

- [Welcome to CircuitPython](https://cdn-learn.adafruit.com/downloads/pdf/welcome-to-circuitpython.pdf)

- [Circuit Python for Pico W](https://circuitpython.org/board/raspberry_pi_pico_w/)

- [Adafruit Pico W Basic Wifi Test](https://learn.adafruit.com/pico-w-wifi-with-circuitpython/pico-w-basic-wifi-test)



