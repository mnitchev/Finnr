class BackObstacleRegulator(object):
    def __init__(self, config):
        self.min_distance = config.min_back_distance

    def regulate(self, motion, sensor_data):
        if (motion.is_forward() and self.can_move_back(sensor_data)):
            return motion.reverse()
        else:
            return motion.stop()

    def can_move_back(self, sensor_data):
        return sensor_data.front_distance < self.min_distance
