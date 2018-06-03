from ..motion import FramePositionMotionConverter
from ..motion import RotatingMotionGenerator


class Brain(object):

    def __init__(self, traffic_chain, converter, generator):
        self.traffic_chain = traffic_chain
        self.motion_converter = converter
        self.seek_motion_generator = generator

    def think(self, sensorData):
        if(sensorData.target_visible()):
            target = sensorData.targetPosition
            motion = self.convert_to_motion(target)
            return self.traffic_chain.regulate(motion, sensorData)
        return self.get_seek_motion()

    def convert_to_motion(self, target):
        return self.motion_converter.convert(target)

    def get_seek_motion(self):
        self.seek_motion_generator.generate()
