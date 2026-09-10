# ==============================
# ARED Hardware Pin Configuration
# ==============================

# =================================
# HC-SR04 Ultrasonic Sensor
# =================================

TRIG_PIN = 5
ECHO_PIN = 9


# =================================
# L298N Motor Driver
# =================================

# Left Motor
ENA = 18
IN1 = 17
IN2 = 27

# Right Motor
ENB = 19
IN3 = 22
IN4 = 23


# =================================
# Motor PWM Settings
# =================================

PWM_FREQUENCY = 1000
DEFAULT_SPEED = 70