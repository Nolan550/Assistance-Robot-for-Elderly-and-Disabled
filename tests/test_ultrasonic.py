import time
import RPi.GPIO as GPIO

from hardware.ultrasonic import UltrasonicSensor


sensor = UltrasonicSensor()


try:

    print("\n==============================")
    print("     ARED ULTRASONIC TEST")
    print("==============================")

    print("\nPlace an object in front of the sensor.")
    print("Press CTRL+C to stop.\n")

    while True:

        distance = sensor.measure_distance()

        if distance is None:

            print("No echo detected")

        else:

            print(
                f"Distance: {distance} cm"
            )

        time.sleep(0.5)


except KeyboardInterrupt:

    print("\nTest stopped.")


finally:

    GPIO.cleanup()
    print("GPIO cleaned up.")