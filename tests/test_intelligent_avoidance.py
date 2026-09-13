import time

from hardware.motors import Motors
from hardware.scanner_servo import ScannerServo
from hardware.ultrasonic import UltrasonicSensor

from navigation.scanner import Scanner
from navigation.obstacle_avoidance import ObstacleAvoidance


motors = Motors()
servo = ScannerServo()
sensor = UltrasonicSensor()

scanner = Scanner(
    servo,
    sensor
)

avoidance = ObstacleAvoidance(
    motors,
    scanner
)


try:

    print("\n==============================")
    print("  ARED INTELLIGENT AVOIDANCE")
    print("==============================")

    print("\nStarting test...")
    print("Place an object in front of ARED.")
    print("Press CTRL+C to stop.\n")

    while True:

        avoidance.run_once()

        time.sleep(0.5)


except KeyboardInterrupt:

    print("\nTest stopped by user.")


finally:

    avoidance.stop()
    servo.cleanup()
    motors.cleanup()

    print("Hardware cleaned up.")