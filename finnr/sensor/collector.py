from .camera import Camera
from .distance import BatDistanceSensor

class SensorData(object):
    def __init__(self, targetPositionData, backDistance, frontDistance):
        position, visible = targetPositionData
        self.targetPosition = position
        self.targetVisible = visible
        self.backDistance = backDistance
        self.frontDistance = frontDistance
    
    def target_visible(self):
        return self.targetVisible

class SensorCollector(object):
    def __init__(self):
        self.camera = Camera()
        self.camera.start()
        self.backDistanceSensor = BatDistanceSensor(16, 18)
        self.backDistanceSensor.setup_pins()
        self.frontDistanceSensor = BatDistanceSensor(38, 40)
        self.frontDistanceSensor.setup_pins()

    def collect(self):
        targetPositionData = self.camera.get_position()
        backDistance = self.backDistanceSensor.get_distance()
        frontDistance = self.frontDistanceSensor.get_distance()

        return SensorData(targetPositionData, backDistance, frontDistance)
