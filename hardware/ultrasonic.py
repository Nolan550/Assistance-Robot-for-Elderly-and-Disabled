import time
import RPi.GPIO as GPIO

from config.pins import (
    TRIG_PIN,
    ECHO_PIN
)


class UltrasonicSensor:

    def __init__(self):

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        GPIO.setup(
            TRIG_PIN,
            GPIO.OUT
        )

        GPIO.setup(
            ECHO_PIN,
            GPIO.IN
        )

        GPIO.output(
            TRIG_PIN,
            GPIO.LOW
        )

        # Allow the sensor to settle
        time.sleep(0.5)


    def measure_distance(self):

        # Send a 10 microsecond trigger pulse
        GPIO.output(
            TRIG_PIN,
            GPIO.HIGH
        )

        time.sleep(0.00001)

        GPIO.output(
            TRIG_PIN,
            GPIO.LOW
        )


        # Wait for ECHO to go HIGH
        timeout = time.time() + 0.04

        while GPIO.input(ECHO_PIN) == 0:

            if time.time() > timeout:
                return None

        pulse_start = time.time()


        # Wait for ECHO to return LOW
        timeout = time.time() + 0.04

        while GPIO.input(ECHO_PIN) == 1:

            if time.time() > timeout:
                return None

        pulse_end = time.time()


        # Calculate pulse duration
        pulse_duration = (
            pulse_end -
            pulse_start
        )


        # Speed of sound ≈ 34300 cm/s
        # Divide by 2 because the sound travels
        # to the object and back.
        distance = (
            pulse_duration * 34300
        ) / 2


        return round(distance, 1)