class Navigator:

    def __init__(self, movement):
        self.movement = movement

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

        destination = destination.lower()

        if destination not in self.routes:
            print(
                f"Unknown destination: {destination}"
            )
            return False

        print(
            f"\nNavigating to: {destination.upper()}"
        )

        route = self.routes[destination]

        for action, duration in route:

            print(
                f"Action: {action} "
                f"for {duration} seconds"
            )

            if action == "forward":
                self.movement.forward_for(duration)

            elif action == "backward":
                self.movement.backward_for(duration)

            elif action == "left":
                self.movement.turn_left_for(duration)

            elif action == "right":
                self.movement.turn_right_for(duration)

        print(
            f"\nARED arrived at {destination.upper()}"
        )

        return True