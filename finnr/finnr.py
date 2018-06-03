from .brain import Brain
from .motion import FramePositionMotionConverter, RotatingMotionGenerator
from .brain.regulator import RegulatorChain, BackObstacleRegulator, FrontObstacleRegulator
from .sensor import SensorCollector

MIN_DISTANCE = 3.0
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
SEEK_ROTATION_SPEED = 0.5
ROTATION_DIRECTION = 1.0


class Finnr(object):
    def __init__(self):
        regulators = [BackObstacleRegulator(3.0), FrontObstacleRegulator(3.0)]
        trafficChain = RegulatorChain(regulators)
        converter = FramePositionMotionConverter(FRAME_WIDTH, FRAME_HEIGHT)
        generator = RotatingMotionGenerator(SEEK_ROTATION_SPEED, ROTATION_DIRECTION)

        self.brain = Brain(trafficChain, converter, generator)
        self.sensorCollector = SensorCollector()
        self.engine = Engine((31,33),(35,37))
        self.done = False

    def start(self):
        while not done:
            sensorData = self.sensorCollector.collect()
            motion = self.brain.think()
            self.engine.set_direction(motion)

    def stop(self):
        self.engine.stop()

    def __del__(self):
        self.stop()
