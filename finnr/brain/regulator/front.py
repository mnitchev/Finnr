class FrontObstacleRegulator(object):
    def __init__(self, minFrontDistance):
        self.minDistance = minFrontDistance

    def regulate(self, motion, sensorData):
        if motion.is_forward() and not self.can_move_forward(sensorData):
            return motion.reverse()
        else:
            return motion

    def can_move_forward(self, sensorData):
        return sensorData.frontDistance < self.minDistance
