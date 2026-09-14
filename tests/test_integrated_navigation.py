from hardware.motors import Motors
from hardware.ultrasonic import UltrasonicSensor
from hardware.scanner_servo import ScannerServo

from navigation.movement import MovementController
from navigation.scanner import Scanner
from navigation.obstacle_avoidance import ObstacleAvoidance
from navigation.navigation import Navigator


motors = Motors()

sensor = UltrasonicSensor()

servo = ScannerServo()

movement = MovementController(
    motors
)

scanner = Scanner(
    servo,
    sensor
)

obstacle_avoidance = ObstacleAvoidance(
    motors,
    scanner
)

navigator = Navigator(
    movement,
    obstacle_avoidance
)


try:

    print("\n==============================")
    print("   ARED INTEGRATED NAVIGATION")
    print("==============================")

    print("\nAvailable destinations:")
    print("1. kitchen")
    print("2. bedroom")
    print("3. living_room")

    destination = input(
        "\nEnter destination: "
    ).strip()


    result = navigator.go_to(
        destination
    )


    if result:

        print(
            "\nNavigation completed successfully."
        )

    else:

        print(
            "\nNavigation failed."
        )


finally:

    navigator.stop()

    servo.cleanup()

    motors.cleanup()

    print(
        "\nARED hardware safely stopped."
    )
