from .camera import Camera
from .distance import BatDistanceSensor

class Position(object):
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def __str__(self):
        return "{ X: " + self.x + ", Y: " + self.y + " }"

class SensorData(object):
    def __init__(self, targetPositionData, backDistance, frontDistance):
        position, visible = targetPositionData
        ((x,y), size) = position
        self.targetPosition = Position(x, y, size)
        self.targetVisible = visible
        self.backDistance = backDistance
        self.frontDistance = frontDistance
    
    def target_visible(self):
        return self.targetVisible

    def __str__(self):
        return "{Pos: " + str(self.targetPosition) + ", Vis: " + self.targetVisible + ", B: " + self.backDistance + ", F: " + self.frontDistance + " }"

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
