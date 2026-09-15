import math


class Odometry:

    def __init__(self):

        # Estimated position in metres
        self.x = 0.0
        self.y = 0.0

        # Heading in degrees
        # 0   = forward
        # 90  = left
        # 180 = backward
        # 270 = right
        self.heading = 0.0


    def reset(self, x=0.0, y=0.0, heading=0.0):

        self.x = x
        self.y = y
        self.heading = heading % 360

        print(
            f"Odometry reset: "
            f"x={self.x:.2f} m, "
            f"y={self.y:.2f} m, "
            f"heading={self.heading:.1f}°"
        )


    def update_forward(self, distance):

        radians = math.radians(
            self.heading
        )

        self.x += (
            distance * math.cos(radians)
        )

        self.y += (
            distance * math.sin(radians)
        )


    def update_backward(self, distance):

        radians = math.radians(
            self.heading
        )

        self.x -= (
            distance * math.cos(radians)
        )

        self.y -= (
            distance * math.sin(radians)
        )


    def update_turn_left(self, angle):

        self.heading = (
            self.heading + angle
        ) % 360


    def update_turn_right(self, angle):

        self.heading = (
            self.heading - angle
        ) % 360


    def get_position(self):

        return {
            "x": round(self.x, 3),
            "y": round(self.y, 3),
            "heading": round(self.heading, 1)
        }


    def distance_to(self, target_x, target_y):

        return math.sqrt(
            (target_x - self.x) ** 2
            +
            (target_y - self.y) ** 2
        )


    def direction_to(self, target_x, target_y):

        dx = target_x - self.x
        dy = target_y - self.y

        angle = math.degrees(
            math.atan2(dy, dx)
        )

        return angle % 360