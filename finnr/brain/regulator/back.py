class BackObstacleRegulator(object):
    def __init__(self, minBackDistance):
        self.minDistance = minBackDistance

    def regulate(self, motion, sensorData):
        if not motion.is_forward() and not self.can_move_back(sensorData):
            return motion.reverse()
        else:
            return motion.stop()

    def can_move_back(self, sensorData):
        return sensorData.backDistance < self.minDistance
