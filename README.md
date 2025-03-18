# Mecanum Wheel Control

This project provides a Python program to control a mecanum wheel robot using a Raspberry Pi. The program allows for movement in various directions and is designed to be user-friendly.

## Project Structure

```
mecanum-wheel-control
├── src
│   ├── main.py          # Entry point of the program
│   ├── controller.py    # Contains the MecanumController class for movement control
│   ├── motor_driver.py  # Interfaces with motor hardware
│   └── utils.py         # Utility functions for user input
├── requirements.txt     # Python libraries and dependencies
└── README.md            # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd mecanum-wheel-control
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Connect the Raspberry Pi to the mecanum wheel robot hardware.
2. Run the main program:
   ```
   python src/main.py
   ```

3. Follow the on-screen instructions to control the robot's movement.

## Functions

- **Move Forward**: Move the robot forward.
- **Move Backward**: Move the robot backward.
- **Turn Left**: Rotate the robot to the left.
- **Turn Right**: Rotate the robot to the right.
- **Spin Left**: Spin the robot to the left.
- **Spin Right**: Spin the robot to the right.
- **Stop**: Stop all movements.
- **Stop**: Stop all movements.
- **X** button: Forward
- **Circle button** : Back up
- **Triangle button** : Left
- **Square button** : To the right
- **L1 button** : left spin
- **R1 button** : Right spin
- **Option button** : Stop

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.