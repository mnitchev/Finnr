import RPi.GPIO as GPIO
import time

class BatDistanceSensor(object):
    def __init__(self, triggerPin, echoPin):
        GPIO.setmode(GPIO.BOARD)
        self.triggerPin = triggerPin
        self.echoPin = echoPin

    def setup_pins(self):
        print("[INFO] Initializing distance sensor...")
        GPIO.setup(self.triggerPin, GPIO.OUT)
        GPIO.setup(self.echoPin, GPIO.IN)
        GPIO.output(self.triggerPin, GPIO.LOW)
        print("[INFO] Waiting for sensor to settle")
        time.sleep(2)

    def get_distance(self):
        GPIO.output(self.triggerPin, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(self.triggerPin, GPIO.LOW)

        while GPIO.input(self.echoPin)==0:
            pulse_start_time = time.time()
        while GPIO.input(self.echoPin)==1:
            pulse_end_time = time.time()

        pulse_duration = pulse_end_time - pulse_start_time
        distance = round(pulse_duration * 17150, 2)
        return distance

