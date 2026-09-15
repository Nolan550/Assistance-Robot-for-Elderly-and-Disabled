import time


class NavigationController:

    IDLE = "IDLE"
    MOVING = "MOVING"
    AVOIDING = "AVOIDING"
    ARRIVED = "ARRIVED"
    STOPPED = "STOPPED"


    def __init__(
        self,
        movement,
        obstacle_avoidance,
        odometry
    ):

        self.movement = movement
        self.obstacle_avoidance = obstacle_avoidance
        self.odometry = odometry

        self.state = self.IDLE


    def set_state(self, state):

        self.state = state

        print(
            f"Navigation state: {state}"
        )


    def start(self):

        self.set_state(
            self.MOVING
        )


    def move_forward(self):

        distance = (
            self.obstacle_avoidance
            .get_front_distance()
        )


        if distance is None:

            print(
                "No ultrasonic reading."
            )

            self.stop()

            return False


        print(
            f"Front distance: "
            f"{distance} cm"
        )


        if (
            distance
            <= self.obstacle_avoidance.safe_distance
        ):

            self.set_state(
                self.AVOIDING
            )

            self.obstacle_avoidance.avoid_obstacle()

            self.set_state(
                self.MOVING
            )

            return False


        self.movement.motors.forward()

        return True


    def stop(self):

        self.movement.stop()

        self.set_state(
            self.STOPPED
        )


    def arrived(self):

        self.movement.stop()

        self.set_state(
            self.ARRIVED
        )


    def get_state(self):

        return self.state


    def get_status(self):

        return {
            "state": self.state,
            "position": self.odometry.get_position()
        }