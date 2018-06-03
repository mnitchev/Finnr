class FrontObstacleRegulator(object):
    def __init__(self, minFrontDistance):
        self.minDistance = minFrontDistance

    def regulate(self, motion, sensor_data):
        if (motion.is_forward() and self.can_move_forward(sensorData)):
            return motion.reverse()
        else:
            return motion.stop()

    def can_move_forward(self, sensorData):
        return sensorData.frontDistance < self.minDistance
