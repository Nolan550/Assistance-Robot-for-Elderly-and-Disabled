import time

from hardware.scanner_servo import ScannerServo


scanner = ScannerServo()

try:

    print("\n==============================")
    print("      ARED SCANNER TEST")
    print("==============================")

    print("\nMoving to CENTER...")
    scanner.center()
    time.sleep(1)

    print("\nMoving to LEFT...")
    scanner.left()
    time.sleep(1)

    print("\nMoving to CENTER...")
    scanner.center()
    time.sleep(1)

    print("\nMoving to RIGHT...")
    scanner.right()
    time.sleep(1)

    print("\nMoving to CENTER...")
    scanner.center()

    print("\nScanner servo test completed.")

finally:

    scanner.cleanup()