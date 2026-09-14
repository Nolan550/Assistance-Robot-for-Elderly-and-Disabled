import time


class Navigator:

    def __init__(self, movement, obstacle_avoidance):

        self.movement = movement
        self.obstacle_avoidance = obstacle_avoidance

        self.routes = {

            "kitchen": [
                ("forward", 3.0),
                ("left", 0.8),
                ("forward", 2.0),
            ],

            "bedroom": [
                ("forward", 2.0),
                ("right", 0.8),
                ("forward", 3.0),
            ],

            "living_room": [
                ("forward", 4.0),
            ],
        }


    def go_to(self, destination):

        destination = destination.lower().strip()

        if destination not in self.routes:

            print(
                f"Unknown destination: {destination}"
            )

            return False


        print(
            f"\nNavigating to: "
            f"{destination.upper()}"
        )


        route = self.routes[destination]


        for action, duration in route:

            print(
                f"\nRoute action: {action}"
            )

            if action == "forward":

                self._forward_with_avoidance(
                    duration
                )

            elif action == "backward":

                self.movement.backward_for(
                    duration
                )

            elif action == "left":

                self.movement.turn_left_for(
                    duration
                )

            elif action == "right":

                self.movement.turn_right_for(
                    duration
                )


        self.movement.stop()


        print(
            f"\nARED reached "
            f"{destination.upper()}"
        )

        return True


    def _forward_with_avoidance(self, duration):

        start_time = time.time()

        print(
            f"Moving forward for "
            f"{duration} seconds "
            f"with obstacle detection."
        )


        while (
            time.time() - start_time
            < duration
        ):

            distance = (
                self.obstacle_avoidance
                .get_front_distance()
            )


            if distance is None:

                print(
                    "No ultrasonic reading."
                )

                self.movement.stop()

                time.sleep(0.2)

                continue


            print(
                f"Front distance: "
                f"{distance} cm"
            )


            if (
                distance
                <= self.obstacle_avoidance.safe_distance
            ):

                print(
                    "\nObstacle detected "
                    "during navigation!"
                )

                self.movement.stop()

                time.sleep(0.2)


                self.obstacle_avoidance.avoid_obstacle()


                # Restart timing after obstacle avoidance.
                start_time = time.time()

            else:

                self.movement.motors.forward()


            time.sleep(0.2)


        self.movement.stop()


    def stop(self):

        self.movement.stop()
