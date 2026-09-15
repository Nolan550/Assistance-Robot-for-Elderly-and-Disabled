import time

from hardware.motors import Motors
from hardware.ultrasonic import UltrasonicSensor
from hardware.scanner_servo import ScannerServo

from navigation.movement import MovementController
from navigation.scanner import Scanner
from navigation.obstacle_avoidance import ObstacleAvoidance
from navigation.odometry import Odometry
from navigation.navigation_controller import NavigationController


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

odometry = Odometry()

controller = NavigationController(
    movement,
    obstacle_avoidance,
    odometry
)


try:

    print("\n==============================")
    print("  ARED NAVIGATION CONTROLLER")
    print("==============================")


    print("\nInitial status:")

    print(
        controller.get_status()
    )


    print("\nStarting navigation:")

    controller.start()


    print("\nController state:")

    print(
        controller.get_state()
    )


    print("\nTesting forward movement:")

    controller.move_forward()

    odometry.update_forward(
        0.1
    )


    print("\nCurrent status:")

    print(
        controller.get_status()
    )


    time.sleep(1)


    controller.stop()


    print("\nFinal status:")

    print(
        controller.get_status()
    )


finally:

    controller.stop()

    servo.cleanup()

    motors.cleanup()

    print(
        "\nHardware cleaned up."
    )