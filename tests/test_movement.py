import time

from hardware.motors import Motors
from navigation.movement import MovementController


motors = Motors()
movement = MovementController(motors)


try:

    print("\n==============================")
    print("     ARED MOVEMENT TEST")
    print("==============================")

    movement.forward_for(2)

    time.sleep(1)

    movement.backward_for(2)

    time.sleep(1)

    movement.turn_left_for(1)

    time.sleep(1)

    movement.turn_right_for(1)

    movement.stop()

    print("\nMovement test completed successfully.")


finally:

    movement.stop()
    motors.cleanup()