"""
Plug in Nightlight - Before testing/ Early Model

This program simulates a nightlight system using an LDR and PIR sensor.
The nightlight only turns on when the room is dark AND motion is detected.
The light remains on for 30 seconds before turning off.
"""

import time


# Variables
# The amount of time the nightlight stays on.
light_duration = 30

# Stores whether the LED is currently on or off.
led_on = False


# FUNCTIONS
def checklightsensor():
    """
    Checks whether the room is dark

    In the early model, user input is used to represent/copy
    the LDR light sensor

    Returns:
        True if the room is dark.
        False if the room is bright.
    """

    light = input("Is the room dark? (yes/no): ").lower()

    if light == "yes":
        return True
    else:
        return False


def checkmotionsensor():
    """
    Checks whether motion has been detected

    In the early model, user input is used to represent/copy
    the PIR motion sensor

    Returns:
        True if motion is detected.
        False if no motion is detected.
    """

    motion = input("Is motion detected? (yes/no): ").lower()

    if motion == "yes":
        return True
    else:
        return False


def turnlighton():
    """
    Turns the nightlight LED on when movement is detected
    in a dark room
    """

    global led_on

    led_on = True
    print("Nightlight ON: gentle glow activated.")


def turnlightoff():
    """
    Turns the nightlight LED off
    """

    global led_on

    led_on = False
    print("Nightlight OFF")


def starttimer():
    """
    Starts the 30-second timer after the nightlight
    has been activated

    Once 30 seconds have passed, the LED is turned off
    """

    print("30-second timer started.")

    # Keep the LED on for the required 30 seconds.
    time.sleep(light_duration)

    # Turn the nightlight off after the timer finishes.
    turnlightoff()

# MAINLINE ROUTINE
def main():
    """
    Runs the main nightlight algorithm.

    The system checks the light level first.
    If the room is dark, it checks for movement.
    The LED only turns on when both conditions are met.
    """

    print("Nightlight system starting...")

    # 1) Check the LDR/light sensor.
    dark = checklightsensor()

    # 2) If the room is bright, keep the LED off.
    if not dark:
        print("Room is bright. Nightlight remains OFF.")
        turnlightoff()
        return

    # 3) The room is dark, so check the PIR sensor.
    motion = checkmotionsensor()

    # 4) If movement is detected, turn the LED on.
    if motion:
        turnlighton()

        `# 5) Keep the LED on for 30 seconds.
        starttimer()

    # 6) If there is no movement, keep the LED off.
    else:
        print("No motion detected. Nightlight remains OFF.")
        turnlightoff()


# PROGRAM START
if __name__ == "__main__":
    main()