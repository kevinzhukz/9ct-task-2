from machine import Pin, ADC, time_pulse_us
import time

light_sensor = ADC(26)  # light sensor/LDR
trig = Pin(15, Pin.OUT)  # trigger
echo = Pin(17, Pin.IN)  #  echo
led = Pin(16, Pin.OUT)  # LED light

light_limit = 50
motion_limit = 5
light_time = 30


def light():
    """
    Checks the light level in the room using the LDR.
    If the room is dark, it checks for movement.
    """

    light_level = light_sensor.read_u16()

    # if the light level is low, the room is dark
    if light_level <= light_limit:

        # check if movement has been detected
        if motion_detect():
            turn_light_on()

    else:
        # If the room is bright, keep the LED off
        led.off()


def distance():
    """
    Measures the distance using the ultrasonic sensor
    and returns the distance in centimetres.
    """

    # Send a short signal to the ultrasonic sensor
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)

    # measure how long the echo takes to return
    duration = time_pulse_us(echo, 1)

    # convert the time into distance
    distance_cm = (duration * 0.0343) / 2

    return distance_cm


# Ultrasonic sensor code was learnt from this tutorial:
# https://randomnerdtutorials.com/raspberry-pi-pico-hc-sr04-micropython/
def motion_detect():
    """
    Checks if there has been movement by comparing
    two distance measurements.

    Returns True if movement is detected and False
    if there is no movement.
    """

    starting_distance = distance()

    time.sleep(0.1)

    current_distance = distance()

    # if the distance changes by more than 5 cm,
    # movement has been detected
    if abs(current_distance - starting_distance) >= motion_limit:
        return True
    else:
        return False


def turn_light_on():
    """
    Turns the LED on for 30 seconds.
    If more movement is detected, the timer starts again.
    """

    led.on()

    start_time = time.ticks_ms()

    while time.ticks_diff(time.ticks_ms(), start_time) < light_time * 1000:

        # Check for more movement while the light is on
        if motion_detect():
            start_time = time.ticks_ms()

        time.sleep(0.1)

    led.off()


while True:

    # Continuously run the nightlight system
    light()

    time.sleep(0.1)