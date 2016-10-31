from body import Body

class Simulation(object):
    bodies = None
    def __init__(self):
        self.bodies = [ ]

    def step(self, delta):
        for body in self.bodies:
            body.step(delta)

    def create_body(self, convex):
        result = Body(self, convex)
        return result

    def raycast(self, start, normal):
        pass
