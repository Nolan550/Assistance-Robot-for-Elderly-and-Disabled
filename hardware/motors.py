import time
import RPi.GPIO as GPIO

from config.pins import (
    ENA,
    IN1,
    IN2,
    ENB,
    IN3,
    IN4,
    PWM_FREQUENCY,
    DEFAULT_SPEED
)


class Motors:

    def __init__(self):

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        # Motor control pins
        motor_pins = [
            ENA, IN1, IN2,
            ENB, IN3, IN4
        ]

        for pin in motor_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)

        # PWM channels
        self.pwm_left = GPIO.PWM(
            ENA,
            PWM_FREQUENCY
        )

        self.pwm_right = GPIO.PWM(
            ENB,
            PWM_FREQUENCY
        )

        self.pwm_left.start(0)
        self.pwm_right.start(0)

        # Current speed
        self.speed = DEFAULT_SPEED


    def set_speed(self, speed):

        self.speed = max(
            0,
            min(100, speed)
        )

        print(f"Motor speed set to {self.speed}%")


    def forward(self):

        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)

        GPIO.output(IN3, GPIO.HIGH)
        GPIO.output(IN4, GPIO.LOW)

        self.pwm_left.ChangeDutyCycle(self.speed)
        self.pwm_right.ChangeDutyCycle(self.speed)


    def backward(self):

        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.HIGH)

        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.HIGH)

        self.pwm_left.ChangeDutyCycle(self.speed)
        self.pwm_right.ChangeDutyCycle(self.speed)


    def turn_left(self):

        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.HIGH)

        GPIO.output(IN3, GPIO.HIGH)
        GPIO.output(IN4, GPIO.LOW)

        self.pwm_left.ChangeDutyCycle(self.speed)
        self.pwm_right.ChangeDutyCycle(self.speed)


    def turn_right(self):

        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)

        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.HIGH)

        self.pwm_left.ChangeDutyCycle(self.speed)
        self.pwm_right.ChangeDutyCycle(self.speed)


    def stop(self):

        self.pwm_left.ChangeDutyCycle(0)
        self.pwm_right.ChangeDutyCycle(0)

        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.LOW)

        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.LOW)


    def cleanup(self):

        self.stop()

        self.pwm_left.stop()
        self.pwm_right.stop()

        GPIO.cleanup()