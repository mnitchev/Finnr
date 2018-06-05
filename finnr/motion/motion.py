class Motion(object):
    def __init__(self,  momentum, steering):
        self.momentum = momentum
        self.steering = steering

    def reverse(self):
        return Motion(-self.momentum, -self.steering)

    def stop(self):
        return Motion(0, 0)

    def is_forward(self):
        return self.momentum >= 0

    def __str__(self):
        return "{ Momentum: " + str(self.momentum) + ", Steering: " + str(self.steering) + " }"
