from navigation.odometry import Odometry


odom = Odometry()


print("\n==============================")
print("       ARED ODOMETRY TEST")
print("==============================")


print("\nInitial position:")

print(
    odom.get_position()
)


print("\nMoving forward 1 metre:")

odom.update_forward(1.0)

print(
    odom.get_position()
)


print("\nTurning left 90 degrees:")

odom.update_turn_left(90)

print(
    odom.get_position()
)


print("\nMoving forward 1 metre:")

odom.update_forward(1.0)

print(
    odom.get_position()
)


print("\nDistance to (2, 2):")

print(
    odom.distance_to(2.0, 2.0)
)


print("\nDirection to (2, 2):")

print(
    odom.direction_to(2.0, 2.0)
)


print("\nOdometry test completed.")