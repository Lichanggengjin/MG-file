'''
Author: Jinshuo Li
Date: 2025-03-18 18:30:28
LastEditors: Changgeng Li 168347526+Lichanggengjin@users.noreply.github.com
LastEditTime: 2025-03-18 18:59:40
FilePath: /机械赛文件/mecanum-wheel-control/src/motor_driver.py
Description: 
'''
import RPi.GPIO as GPIO

class MotorDriver:
    def __init__(self, motor_pins):
        self.motor_pins = motor_pins
        self.setup_motors()

    def setup_motors(self):
        GPIO.setmode(GPIO.BCM)
        for pin in self.motor_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)

    def set_speed(self, speed1, speed2, speed3, speed4):
        speeds = [speed1, speed2, speed3, speed4]
        for i, pin in enumerate(self.motor_pins):
            pwm = GPIO.PWM(pin, 100)
            pwm.start(abs(speeds[i]))
            if speeds[i] < 0:
                GPIO.output(pin, GPIO.LOW)
            else:
                GPIO.output(pin, GPIO.HIGH)

    def stop(self):
        for pin in self.motor_pins:
            GPIO.output(pin, GPIO.LOW)