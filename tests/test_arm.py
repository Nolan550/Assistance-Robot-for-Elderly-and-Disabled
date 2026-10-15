from hardware.arm import RoboticArm


# ==========================================
# ARED ARM CALIBRATION
# ==========================================

CHANNELS = {
    3: "RIGHT SHOULDER",
    4: "RIGHT ELBOW",
    5: "RIGHT WRIST",
    0: "LEFT SHOULDER",
    1: "LEFT ELBOW",
    2: "LEFT WRIST",
}

POSITIONS = ["min", "max", "rest"]

calibration = {
    channel: {
        "min": None,
        "max": None,
        "rest": None,
    }
    for channel in CHANNELS
}


def print_calibration():
    """Print all calibration values collected so far."""

    print("\n" + "=" * 76)
    print("              ARED ARM CALIBRATION RESULTS")
    print("=" * 76)

    print(
        f"{'CHANNEL':<10}"
        f"{'JOINT':<22}"
        f"{'MIN (DEG)':<14}"
        f"{'MAX (DEG)':<14}"
        f"{'REST (DEG)':<14}"
    )

    print("-" * 76)

    for channel, joint in CHANNELS.items():
        values = calibration[channel]

        minimum = (
            str(values["min"])
            if values["min"] is not None
            else "-"
        )

        maximum = (
            str(values["max"])
            if values["max"] is not None
            else "-"
        )

        rest = (
            str(values["rest"])
            if values["rest"] is not None
            else "-"
        )

        print(
            f"CH{channel:<8}"
            f"{joint:<22}"
            f"{minimum:<14}"
            f"{maximum:<14}"
            f"{rest:<14}"
        )

    print("=" * 76)


def calibrate_position(arm, channel, joint, position):
    """Move a joint to a requested angle and record it."""

    while True:
        print("\n" + "-" * 50)
        print(f"Joint: {joint} (CH{channel})")
        print(f"Position to calibrate: {position.upper()}")
        print("-" * 50)

        print("Enter an angle between 0 and 180 degrees.")
        print("Type 'n' to skip this position.")
        print("Type 'q' to stop and print the results.")

        user_input = input("Angle > ").strip().lower()

        if user_input == "q":
            return "quit"

        if user_input == "n":
            print(f"Skipped {position.upper()} for {joint}.")
            return "skip"

        try:
            angle = float(user_input)
        except ValueError:
            print("Invalid input. Enter an angle, n, or q.")
            continue

        if not 0 <= angle <= 180:
            print("Angle must be between 0 and 180 degrees.")
            continue

        # Move only the selected servo.
        try:
            arm.move_channel(channel, angle)
        except Exception as error:
            print(f"Servo movement error: {error}")
            return "quit"

        print(f"\nThe servo is now commanded to {angle} degrees.")
        print("Check the joint's physical position carefully.")

        print("\nChoose:")
        print("  y = Accept and save this angle")
        print("  n = Try this position again")
        print("  q = Stop calibration and print results")

        confirmation = input("Confirm > ").strip().lower()

        if confirmation == "q":
            return "quit"

        if confirmation == "n":
            continue

        if confirmation == "y":
            calibration[channel][position] = angle

            print(
                f"Saved CH{channel} {position.upper()} "
                f"= {angle} degrees."
            )

            return "saved"

        print("Please enter y, n, or q.")


def main():
    arm = None

    try:
        arm = RoboticArm()

        print("\n" + "=" * 60)
        print("           ARED ARM CALIBRATION")
        print("=" * 60)

        print("\nCalibration order:")

        for channel, joint in CHANNELS.items():
            print(f"CH{channel}: {joint} — MIN, MAX, REST")

        print("\nSafety instructions:")
        print("- Keep hands clear of moving joints.")
        print("- Begin near the current safe position.")
        print("- Use small angle changes when exploring limits.")
        print("- Never force a joint against a mechanical stop.")
        print("- Stop if a servo strains, grinds, or binds.")
        print("- MIN and MAX mean safe mechanical limits,")
        print("  not necessarily 0 and 180 degrees.")

        input("\nPress ENTER when the robot is ready...")

        for channel, joint in CHANNELS.items():

            print("\n\n" + "=" * 60)
            print(f"CALIBRATING {joint} — CH{channel}")
            print("=" * 60)

            for position in POSITIONS:

                result = calibrate_position(
                    arm,
                    channel,
                    joint,
                    position,
                )

                if result == "quit":
                    print("\nCalibration stopped by user.")
                    return

            print(f"\nFinished calibrating {joint}.")

            print(
                "Press ENTER to continue to the next joint, "
                "or type q to stop."
            )

            next_action = input("Continue > ").strip().lower()

            if next_action == "q":
                print("\nCalibration stopped by user.")
                return

        print("\nAll six joints have been processed.")

    except KeyboardInterrupt:
        print("\nCalibration interrupted.")

    except Exception as error:
        print(f"\nCalibration error: {error}")

    finally:
        if arm is not None:
            arm.cleanup()

        print_calibration()
        print("\nCalibration program ended.")


if __name__ == "__main__":
    main()
