import time

from hardware.scanner_servo import ScannerServo
from hardware.ultrasonic import UltrasonicSensor

from navigation.scanner import Scanner


servo = ScannerServo()
sensor = UltrasonicSensor()

scanner = Scanner(
    servo,
    sensor
)


try:

    print("\n==============================")
    print("   ARED SCANNER + ULTRASONIC")
    print("==============================")

    print("\nStarting scan...")

    result = scanner.scan()

    print("Final result:")
    print(result)

    time.sleep(1)


finally:

    servo.cleanup()

    print("\nScanner test completed.")