import time

import board
import busio

from adafruit_pca9685 import PCA9685
from adafruit_motor import servo


class ScannerServo:

    def __init__(self, channel=6):

        # Initialize I2C
        self.i2c = busio.I2C(
            board.SCL,
            board.SDA
        )

        # Initialize PCA9685
        self.pca = PCA9685(
            self.i2c,
            address=0x40
        )

        # Servo frequency
        self.pca.frequency = 50

        # Create servo object
        self.servo = servo.Servo(
            self.pca.channels[channel],
            min_pulse=500,
            max_pulse=2500
        )

        # Scanner positions
        self.LEFT = 30
        self.CENTER = 90
        self.RIGHT = 150

        # Start centered
        self.center()


    def move_to(self, angle):

        # Keep angle within safe servo range
        angle = max(
            0,
            min(180, angle)
        )

        self.servo.angle = angle

        time.sleep(0.5)


    def left(self):

        print("Scanner: LEFT")

        self.move_to(
            self.LEFT
        )


    def center(self):

        print("Scanner: CENTER")

        self.move_to(
            self.CENTER
        )


    def right(self):

        print("Scanner: RIGHT")

        self.move_to(
            self.RIGHT
        )


    def cleanup(self):

        self.pca.deinit()