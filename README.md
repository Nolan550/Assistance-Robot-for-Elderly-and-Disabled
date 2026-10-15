# Assistance-Robot-for-Elderly-and-Disabled

# ARED — Assistance Robot for Elderly and Disabled

**ARED (Assistance Robot for Elderly and Disabled)** is a robotics project aimed at developing an assistive robot that can support elderly people and people with disabilities through basic robotic movement, obstacle detection, and navigation.

The project uses a Raspberry Pi 4 Model B as its main controller, Python for robot control, an HC-SR04 ultrasonic sensor for distance measurement, and an L298N motor driver to control the robot's movement.

## 🎯 Project Objectives

- Develop a robot that can assist elderly people and people with disabilities.
- Implement obstacle detection using ultrasonic distance measurement.
- Control robot movement through a Raspberry Pi and motor driver.
- Explore robotics, embedded systems, automation, and intelligent navigation.
- Build a foundation for future assistive robotics features.

## 🛠️ Hardware Components

| Component | Purpose |
|---|---|
| Raspberry Pi 4 Model B | Main processing and control unit |
| HC-SR04 Ultrasonic Sensor | Measures distance to nearby obstacles |
| L298N Motor Driver | Controls the DC motors |
| DC Motors and Wheels | Provide robot movement |
| Battery / Power Supply | Supplies power to the robot |
| Jumper Wires | Connect electronic components |

## 💻 Software and Technologies

- **Programming Language:** Python
- **Operating System:** Raspberry Pi OS / Linux
- **GPIO Control:** Python GPIO library compatible with the Raspberry Pi
- **Development Environment:** Linux terminal and Python virtual environment

## ⚙️ Hardware Connections

### HC-SR04 Ultrasonic Sensor

| Sensor Pin | Raspberry Pi GPIO |
|---|---|
| TRIG | GPIO 5 |
| ECHO | GPIO 9 |

### L298N Motor Driver

| Motor Driver Pin | Raspberry Pi GPIO |
|---|---|
| ENA | GPIO 18 |
| IN1 | GPIO 17 |
| IN2 | GPIO 27 |
| ENB | GPIO 19 |
| IN3 | GPIO 22 |
| IN4 | GPIO 23 |

**Important:** The HC-SR04 ECHO pin typically outputs 5 V, while Raspberry Pi GPIO pins operate at 3.3 V. Use an appropriate voltage divider or level shifter to protect the Raspberry Pi. Ensure the motor supply, driver, and Raspberry Pi have a suitable common ground.

## 📁 Project Structure

```text
Assistance-Robot-for-Elderly-and-Disabled/
├── README.md
├── main.py
├── requirements.txt
├── modules/
│   ├── motor_control.py
│   ├── obstacle_detection.py
│   └── navigation.py
└── tests/
    └── test_robot.py
```

*Note: This is a suggested structure. Adjust the file and directory names to match your actual repository.*

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Assistance-Robot-for-Elderly-and-Disabled.git
cd Assistance-Robot-for-Elderly-and-Disabled
```

Replace `YOUR-USERNAME` with your GitHub username and update the repository URL if necessary.

### 2. Create a Python Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

If a `requirements.txt` file is available, install the dependencies:

```bash
pip install -r requirements.txt
```

Install only the GPIO and other libraries supported by your Raspberry Pi OS and Python version.

### 4. Run the Robot

After connecting the hardware and configuring the GPIO pins, run the project's main Python program:

```bash
python3 main.py
```

The command assumes your main program is named `main.py`. Replace it with the correct entry-point filename if your project uses a different one.

## 🔍 Key Features

- **Obstacle Detection:** Uses ultrasonic distance measurements to detect nearby objects.
- **Motor Control:** Controls motor direction and speed through the L298N motor driver.
- **Embedded Computing:** Uses a Raspberry Pi to execute the robot's control logic.
- **Navigation Foundation:** Provides a starting point for implementing obstacle avoidance and autonomous movement.
- **Extensibility:** Can be expanded with additional sensors, assistive functions, and intelligent control algorithms.

Only features implemented in the current codebase should be considered completed; other capabilities can be added as development progresses.

## 🔮 Future Improvements

- Implement more reliable autonomous navigation.
- Add voice-command functionality.
- Integrate speech recognition and text-to-speech.
- Add camera-based object detection.
- Develop a user-friendly control interface.
- Explore emergency alert and caregiver notification features.
- Improve obstacle avoidance and movement safety.
- Investigate machine learning for intelligent assistance.

## 🧪 Testing and Safety

- Test motor direction and speed with the wheels raised before operating the robot on the ground.
- Verify ultrasonic sensor readings under different conditions.
- Check all wiring and power connections before switching on the system.
- Use appropriate voltage regulation and protection for GPIO pins.
- Keep emergency motor shutdown available during testing.
- Do not rely on the prototype as a replacement for human care or as a safety-critical mobility device.

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Implement and test your changes.
4. Submit a pull request describing your improvements.

## 👨‍💻 Author

**Nolan Davis**

Computer Systems and Networks Student  
Ardhi University


## ⭐ Acknowledgements

Developed as a robotics and embedded-systems learning project focused on assistive technology, automation, and improving the independence of elderly people and people with disabilities.
