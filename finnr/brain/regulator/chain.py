class RegulatorChain(object):
    def __init__(self, regulators):
        self.regulators = regulators

    def regulate(self, motion, sensorData):
        for r in self.regulators:
            print("[DEBUG] Current motion: ", motion)
            motion = r.regulate(motion, sensorData)
        return motion
