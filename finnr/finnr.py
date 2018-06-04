from .brain import Brain
from .motion import FramePositionMotionConverter, RotatingMotionGenerator
from .brain.regulator import RegulatorChain, BackObstacleRegulator, FrontObstacleRegulator
from .sensor import SensorCollector
from .actuator import Engine

MIN_DISTANCE = 3.0
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
SEEK_ROTATION_SPEED = 0.5
ROTATION_DIRECTION = 1.0
MAX_TARGET_SIZE = 100

class Finnr(object):
    def __init__(self):
        regulators = [BackObstacleRegulator(3.0), FrontObstacleRegulator(3.0)]
        trafficChain = RegulatorChain(regulators)
        converter = FramePositionMotionConverter(FRAME_WIDTH, FRAME_HEIGHT, MAX_TARGET_SIZE)
        generator = RotatingMotionGenerator(SEEK_ROTATION_SPEED, ROTATION_DIRECTION)

        self.brain = Brain(trafficChain, converter, generator)
        self.sensorCollector = SensorCollector()
        self.engine = Engine((35,37), (31, 33))
        self.engine.start()
        self.done = False

    def start(self):
        while not self.done:
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
