class FramePositionMotionConverter(object):
    def __init__(self, frame_width, frame_height, max_size):
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.max_size = max_size

    def convert(self, position):
        halfw = self.frame_width / 2
        steering = abs(halfw - position.x) / halfw
        momentum = abs(self.max_size - position.size) / self.max_size
        motion = Motion(momentum, steering)

        if position.x < halfw:
            motion.steering = -motion.steering
        return motion
