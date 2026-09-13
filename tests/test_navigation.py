from hardware.motors import Motors
from navigation.movement import MovementController
from navigation.navigation import Navigator


motors = Motors()
movement = MovementController(motors)
navigator = Navigator(movement)


try:

    print("\n==============================")
    print("       ARED NAVIGATION TEST")
    print("==============================")

    print("\nAvailable destinations:")
    print("- kitchen")
    print("- bedroom")
    print("- living_room")

    destination = input(
        "\nEnter destination: "
    ).strip()

    result = navigator.go_to(
        destination
    )

    if result:

        print(
            "\nNavigation test completed."
        )

    else:

        print(
            "\nNavigation failed."
        )


finally:

    movement.stop()
    motors.cleanup()