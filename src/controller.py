class MecanumController:
    def __init__(self, motor_driver):
        self.motor_driver = motor_driver

    def move_forward(self, speed):
        self.motor_driver.set_speed(speed, speed, speed, speed)

    def move_backward(self, speed):
        self.motor_driver.set_speed(-speed, -speed, -speed, -speed)

    def turn_left(self, speed):
        self.motor_driver.set_speed(-speed, speed, -speed, speed)

    def turn_right(self, speed):
        self.motor_driver.set_speed(speed, -speed, speed, -speed)

    def spin_left(self, speed):
        self.motor_driver.set_speed(-speed, speed, speed, -speed)

    def spin_right(self, speed):
        self.motor_driver.set_speed(speed, -speed, -speed, speed)

    def stop(self):
        self.motor_driver.stop()