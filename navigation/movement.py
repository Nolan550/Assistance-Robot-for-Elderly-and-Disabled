import time


class MovementController:

    def __init__(self, motors):
        self.motors = motors

    def forward_for(self, duration):
        print(f"Moving forward for {duration} seconds")

        self.motors.forward()

        time.sleep(duration)

        self.motors.stop()

    def backward_for(self, duration):
        print(f"Moving backward for {duration} seconds")

        self.motors.backward()

        time.sleep(duration)

        self.motors.stop()

    def turn_left_for(self, duration):
        print(f"Turning left for {duration} seconds")

        self.motors.turn_left()

        time.sleep(duration)

        self.motors.stop()

    def turn_right_for(self, duration):
        print(f"Turning right for {duration} seconds")

        self.motors.turn_right()

        time.sleep(duration)

        self.motors.stop()

    def stop(self):
        self.motors.stop()