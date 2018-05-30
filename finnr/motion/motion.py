
class Motion(object):
    def __init__(self, momentum, steering):
        self.momentum = momentum
        self.steering = steering

    def reverse(self):
        return Motion(-self.momentum, -self.steering)

    def stop(self):
        return Motion(0, 0)
