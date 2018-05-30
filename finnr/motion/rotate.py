from .motion import Motion


class RotatingMotionGenerator(object):
    def __init__(self, speed, direction):
        self.speed = speed
        self.direction = direction

    def generate(self):
        return Motion(self.speed, self.direction)
