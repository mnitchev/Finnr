class RegulatorChain(object):
    def __init__(self, regulators):
        self.regulators = regulators

    def regulate(self, motion, sensor_data):
        for r in self.regulators:
            motion = r.regulate(motion, sensor_data)
        return motion
