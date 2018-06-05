from ..motion import FramePositionMotionConverter
from ..motion import RotatingMotionGenerator
from ..motion import Motion

class Brain(object):

    def __init__(self, traffic_chain, converter, generator):
        self.traffic_chain = traffic_chain
        self.motion_converter = converter
        self.seek_motion_generator = generator
        self.previous = Motion(0, 0)

    def think(self, sensorData):
        if(sensorData.target_visible()):
            target = sensorData.targetPosition
            motion = self.convert_to_motion(target)
        else:
            motion = self.get_seek_motion()
            if self.previous.steering < 0:
                motion.steering = -motion.steering
        motion = self.traffic_chain.regulate(motion, sensorData)
        self.previous = motion
        return motion
    

    def convert_to_motion(self, target):
        return self.motion_converter.convert(target)

    def get_seek_motion(self):
        return self.seek_motion_generator.generate()
