from .brain import Brain
from .motion import FramePositionMotionConverter, RotatingMotionGenerator
from .brain.regulator import RegulatorChain, BackObstacleRegulator, FrontObstacleRegulator
from .sensor import SensorCollector
from .actuator import Engine
from time import sleep

MIN_DISTANCE = 10.0
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
SEEK_ROTATION_SPEED = 0.5
ROTATION_DIRECTION = 1.0
MAX_TARGET_SIZE = 150

class Finnr(object):
    def __init__(self):
        regulators = [BackObstacleRegulator(MIN_DISTANCE), FrontObstacleRegulator(MIN_DISTANCE)]
        trafficChain = RegulatorChain(regulators)
        converter = FramePositionMotionConverter(FRAME_WIDTH, FRAME_HEIGHT, MAX_TARGET_SIZE)
        generator = RotatingMotionGenerator(SEEK_ROTATION_SPEED, ROTATION_DIRECTION)

        self.brain = Brain(trafficChain, converter, generator)
        self.sensorCollector = SensorCollector()
        self.engine = Engine((37,35), (31, 33))
        self.engine.start()
        self.done = False

    def start(self):
        while not self.done:
            sleep(0.1)
            sensorData = self.sensorCollector.collect()
            print("[INFO] Sensor data: ", sensorData)
            motion = self.brain.think(sensorData)
            print("[INFO] Motion: ", motion)
            self.engine.set_direction(motion)

    def stop(self):
        self.done = True
        self.engine.stop()

    def __del__(self):
        self.stop()
