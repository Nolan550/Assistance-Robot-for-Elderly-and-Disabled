import time


class ObstacleAvoidance:

    def __init__(
        self,
        motors,
        scanner,
        safe_distance=30,
        clear_distance=35
    ):

        self.motors = motors
        self.scanner = scanner

        self.safe_distance = safe_distance
        self.clear_distance = clear_distance

        # Movement timing
        self.reverse_time = 0.5
        self.turn_time = 0.8
        self.escape_reverse_time = 1.0


    def get_front_distance(self):

        return self.scanner.sensor.measure_distance()


    def avoid_obstacle(self):

        print("\n==============================")
        print("     OBSTACLE DETECTED")
        print("==============================")

        # Stop immediately
        self.motors.stop()

        time.sleep(0.2)

        # Initial reverse
        print(
            f"Reversing for "
            f"{self.reverse_time} seconds..."
        )

        self.motors.backward()

        time.sleep(
            self.reverse_time
        )

        self.motors.stop()

        time.sleep(0.3)

        # Scan environment
        scan_result = self.scanner.scan()

        left = scan_result["left"]
        right = scan_result["right"]

        print("\nComparing available space...")

        print(f"LEFT  : {left} cm")
        print(f"RIGHT : {right} cm")

        # If both directions are blocked
        if (
            left < self.clear_distance
            and
            right < self.clear_distance
        ):

            print(
                "\nBoth sides are blocked."
            )

            print(
                "Performing escape reverse..."
            )

            self.motors.backward()

            time.sleep(
                self.escape_reverse_time
            )

            self.motors.stop()

            time.sleep(0.3)

            # Scan again
            scan_result = self.scanner.scan()

            left = scan_result["left"]
            right = scan_result["right"]


        # Choose LEFT
        if left > right:

            print(
                "\nLEFT has more available space."
            )

            print(
                f"Turning LEFT for "
                f"{self.turn_time} seconds..."
            )

            self.motors.turn_left()

            time.sleep(
                self.turn_time
            )

            self.motors.stop()


        # Choose RIGHT
        else:

            print(
                "\nRIGHT has more available space."
            )

            print(
                f"Turning RIGHT for "
                f"{self.turn_time} seconds..."
            )

            self.motors.turn_right()

            time.sleep(
                self.turn_time
            )

            self.motors.stop()


        print(
            "\nObstacle avoidance completed."
        )


    def run_once(self):

        distance = self.get_front_distance()

        if distance is None:

            print(
                "No ultrasonic reading."
            )

            self.motors.stop()

            return


        print(
            f"Front distance: "
            f"{distance} cm"
        )


        if distance > self.safe_distance:

            print(
                "Path clear → moving forward."
            )

            self.motors.forward()

        else:

            self.avoid_obstacle()


    def stop(self):

        self.motors.stop()