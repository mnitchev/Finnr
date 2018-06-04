from multiprocessing import Process, Value, Array
from time import sleep
import RPi.GPIO as GPIO


def start_engine(momentum, steering, pins):
    frontPositive = pins[0]
    frontNegative = pins[1]
    rearPositive = pins[2]
    rearNegative = pins[3]
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(frontPositive, GPIO.OUT)
    GPIO.setup(frontNegative, GPIO.OUT)
    GPIO.setup(rearPositive, GPIO.OUT)
    GPIO.setup(rearNegative, GPIO.OUT)

    forward = GPIO.PWM(rearPositive, 100)
    back = GPIO.PWM(rearNegative, 100)
    left = GPIO.PWM(frontPositive, 100)
    right = GPIO.PWM(frontNegative, 100)
    forward.start(0)
    back.start(0)
    left.start(0)
    right.start(0)
    
    while True:
        if steering.value >= 0:
            left.ChangeDutyCycle(0)
            right.ChangeDutyCycle(int(steering.value * 100))
        else:
            right.ChangeDutyCycle(0)
            left.ChangeDutyCycle(int(-steering.value * 100))

        if momentum.value>= 0:
            back.ChangeDutyCycle(0)
            forward.ChangeDutyCycle(int(momentum.value * 100))
        else:
            forward.ChangeDutyCycle(0)
            back.ChangeDutyCycle(int(-momentum.value * 100))


class Engine(object):
    def __init__(self, frontMotorPins, rearMotorPins):
        rearPositive, rearNegative = rearMotorPins
        self.rearPositive = rearPositive
        self.rearNegative = rearNegative

        frontPositive, frontNegative = frontMotorPins
        self.frontPositive = frontPositive
        self.frontNegative = frontNegative
        self.momentum = Value('d', 0.0)
        self.steering = Value('d', 0.0)
        pins = Array('i', [self.frontPositive, self.frontNegative, self.rearPositive, self.rearNegative])
        self.engineProcess = Process(target=start_engine, args=(self.momentum, self.steering, pins))


    def set_direction(self, direction):
        self.momentum.value = direction.momentum
        self.steering.value = direction.steering

    def start(self):
        self.engineProcess.start()

    def stop(self):
        self.engineProcess.terminate()

    def __del__(self):
        self.stop()

