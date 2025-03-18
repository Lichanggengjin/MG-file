'''
Author: Jinshuo Li
Date: 2025-03-18 18:30:24
LastEditors: Changgeng Li 168347526+Lichanggengjin@users.noreply.github.com
LastEditTime: 2025-03-18 18:59:31
FilePath: /机械赛文件/mecanum-wheel-control/src/main.py
Description: 
'''
import RPi.GPIO as GPIO
from controller import MecanumController
from motor_driver import MotorDriver
from pyPS4Controller.controller import Controller

class MyController(Controller):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def on_x_press(self):
        self.controller.move_forward(50)

    def on_circle_press(self):
        self.controller.move_backward(50)

    def on_triangle_press(self):
        self.controller.turn_left(50)

    def on_square_press(self):
        self.controller.turn_right(50)

    def on_L1_press(self):
        self.controller.spin_left(50)

    def on_R1_press(self):
        self.controller.spin_right(50)

    def on_options_press(self):
        self.controller.stop()

def main():
    GPIO.setmode(GPIO.BCM)
    motor_pins = [17, 18, 27, 22]  
    motor_driver = MotorDriver(motor_pins)
    controller = MecanumController(motor_driver)
    
    ps2_controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
    ps2_controller.set_controller(controller)
    ps2_controller.listen(timeout=60)

if __name__ == "__main__":
    main()
