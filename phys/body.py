import math

from vector import Vector
from convex import Convex

class Body(object):
    _position = None
    """
        The current position of the body.
    """

    _rotation = None
    """
        The current rotation of the body.
    """

    velocity = None
    torque = None
    source_convex = None
    current_convex = None
    mass = None

    simulation = None

    collision_mask = None
    """
        Bits representing what objects we can collide with.
    """

    def __init__(self, simulation, convex):
        self._position = Vector()

        self.velocity = Vector()
        self.source_convex = convex
        self.current_convex = Convex(convex)

        self.torque = 0

        self.collision_mask = 1

        simulation.bodies.append(self)
        self.simulation = simulation

    def step(self, delta):
        # Step us along on our position and rotation
        self.translate(self._position + (self.velocity * delta))
        self.rotate(self._rotation + (self.torque * delta))

        for body in self.simulation.bodies:
            if (body is self or body.collision_mask & self.collision_mask == 0):
                continue

            # We run this loop for each collision check
            # TODO: Implement collision code. We want to modify positions and rotations accordingly
            # here.
            if self.intersects(body):
                pass

    def contains_point(self, point):
        """
            Determines whether or not the specified point is contained within this body.

            :parameters:
                point - The vector to test for.

            :returns:
                True if the vector is contained. False otherwise.
        """

        left = False
        right = False
        above = False
        below = False

        for vertex in self.convex.vertices:
            if (point.x >= vertex.x):
                right = True
            if (point.x <= vertex.x):
                left = True

            if (point.y >= vertex.y):
                above = True
            if (point.y <= vertex.y):
                below = True

        return not (left is not right or above is not below)

    def intersects(self, other):
        for vertex in self.vertices:
            if (other.contains_point(vertex)):
                return True

        for vertex in other.vertices:
            if (self.contains_point(vertex)):
                return True

    def scale(self, scale):
        pass

    def translate(self, position):
        self._position = position

    def rotate(self, theta):
        self._rotation = theta

        sine = math.sin(theta)
        cosine = math.cos(theta)

        for point in self.convex.vertices:
            result = Vector(point.x * cosine - point.y * sine,
                            point.x * sine + point.y * cosine)

            point.x = result.x
            point.y = result.y

    def __repr__(self):
        return "Body at Position %s with Geometry: %s" % (self.position, self.convex)
