import time

from hardware.motors import Motors


motors = Motors()

try:

    print("\n==============================")
    print("       ARED MOTOR TEST")
    print("==============================")

    motors.set_speed(60)

    print("\nFORWARD")
    motors.forward()
    time.sleep(2)

    motors.stop()
    time.sleep(1)

    print("\nBACKWARD")
    motors.backward()
    time.sleep(2)

    motors.stop()
    time.sleep(1)

    print("\nLEFT")
    motors.turn_left()
    time.sleep(1)

    motors.stop()
    time.sleep(1)

    print("\nRIGHT")
    motors.turn_right()
    time.sleep(1)

    motors.stop()

    print("\nMotor test completed.")

finally:

    motors.cleanup()