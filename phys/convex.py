import errors
from vector import Vector

class Convex(object):
    vertices = None
    edges = None

    vertex_normals = None

    def __init__(self, payload):
        if (type(payload) is Convex):
            self.vertices = list(payload.vertices)
            self.edges = list(payload.edges)
            self.vertex_normals = list(payload.vertex_normals)
        elif(type(payload) is list):
            # We should have at least 3 vertices
            if (len(payload) < 3):
                raise errors.InvalidGeometryError("Hulls must have at least 3 vertices!")

            self.vertices = list(payload)

            # Our average distance should be ~= distance from 0,0
            # FIXME: Compare floats with tolerance
            if (Vector.average_distance(self.vertices, Vector.zero) != self.vertices[0].distance(Vector.zero)):
                raise errors.InvalidGeometryError("Got concave hull data!")

            # Calculate edges
            self.edges = [ ]
            self.vertex_normals = [ ]

            # First & Last vertices are always an edge
            self.edges.append((payload[0], payload[-1]))

            for index, vertex in enumerate(payload):
                # Calculate the vertex normals
                self.vertex_normals.append((vertex.normal(), vertex.length()))

                # We can't grab the next vertex and we've already connected first and last
                if (index == len(payload) - 1):
                    break

                next_vertex = payload[index + 1]
                self.edges.append((vertex, next_vertex))

        else:
            raise errors.InvalidGeometryError("Expecting a list of vectors!")

    def __repr__(self):
        return "Convex with Vertices %s" % self.vertices
