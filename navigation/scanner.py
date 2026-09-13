import time


class Scanner:

    def __init__(
        self,
        scanner_servo,
        ultrasonic_sensor
    ):

        self.servo = scanner_servo
        self.sensor = ultrasonic_sensor


    def scan_left(self):

        print("Scanning LEFT...")

        self.servo.left()

        distance = (
            self.sensor.measure_distance()
        )

        if distance is None:
            distance = 999

        print(
            f"LEFT distance: {distance} cm"
        )

        return distance


    def scan_center(self):

        print("Scanning CENTER...")

        self.servo.center()

        distance = (
            self.sensor.measure_distance()
        )

        if distance is None:
            distance = 999

        print(
            f"CENTER distance: {distance} cm"
        )

        return distance


    def scan_right(self):

        print("Scanning RIGHT...")

        self.servo.right()

        distance = (
            self.sensor.measure_distance()
        )

        if distance is None:
            distance = 999

        print(
            f"RIGHT distance: {distance} cm"
        )

        return distance


    def scan(self):

        print("\n==============================")
        print("        ARED SCANNING")
        print("==============================")

        left = self.scan_left()

        time.sleep(0.2)

        center = self.scan_center()

        time.sleep(0.2)

        right = self.scan_right()

        time.sleep(0.2)

        # Return scanner to center
        self.servo.center()

        print("\n--------- SCAN RESULT ---------")

        print(
            f"Left   : {left} cm"
        )

        print(
            f"Center : {center} cm"
        )

        print(
            f"Right  : {right} cm"
        )

        print("-------------------------------\n")

        return {
            "left": left,
            "center": center,
            "right": right
        }