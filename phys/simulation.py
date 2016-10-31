from body import Body
from vector import Vector

class RaycastResult(object):
    body = None
    """
        The body that was struck. If none, no body was struck.
    """

    position = None
    """
        The last position the raytrace was at before something was hit or the distance requested
        was exhausted.
    """

    def __init__(self, position, body):
        self.body = body
        self.position = position

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

    def raycast(self, start, normal, distance, steps=25):
        """
            Performs a raycast from the starting position in the direction specified by the normal vector.
            If normal is a float, then it is considered the angle in radians to calculate a normal vector from.

            :parameters:
                start - The starting position to raycast from.
                normal - The normal vector to move in relation to the starting point. If this is a float, then it is
                considered the angle in radians to calculate a normal vector from. If the normal vector is not normalized,
                then this function will normalize it.
                distance - How far the raycast should travel before considering the current operation a bust.
                steps - The number of steps to take when performing the raytrace. The higher this is, the more accurate the trace.
        """

        # Convert to a normal angle if necessary
        if type(normal) is float:
            normal = Vector.normal_from_angle(normal)
        else:
            normal.normalize()

        step_distance = float(distance) / steps
        current_position = Vector(copy_from=start)
        for step in range(steps):
            # Check if we collide with anything
            # FIXME: We can organize the scene better to make this less expensive.
            for body in self.bodies:
                if body.contains_point(current_position):
                    return RaycastResult(position=current_position, body=body)

            # Advance the position
            current_position += normal * step_distance

        return RaycastResult(positon=current_position, body=None)
