from ..motion import FramePositionMotionConverter
from ..motion import RotatingMotionGenerator


class Brain(object):

    def __init__(self, traffic_chain, config):
        self.traffic_chain = traffic_chain
        self.min_distance = config.min_distance
        self.motion_converter = FramePositionMotionConverter(
            config.frame_width, config.frame_height)
        self.seek_motion_generator = RotatingMotionGenerator(
            config.seek_rotation_speed, config.rotation_direction)

    def think(self, sensor_data):
        if(sensor_data.target_visible()):
            target = sensor_data.target_position
            motion = self.convert_to_motion(target)
            return self.traffic_chain.regulate(motion)
        return self.get_seek_motion()

    def convert_to_motion(self, target):
        return self.motion_converter.convert(target)

    def get_seek_motion(self):
        self.seek_motion_generator.generate()
