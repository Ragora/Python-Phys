import phys

class Application(object):
    def main(self):
        # Build a simple square
        top_left = phys.Vector(-1, -1)
        top_right = phys.Vector(1, -1)
        bottom_right = phys.Vector(1, 1)
        bottom_left = phys.Vector(-1, 1)
        square = [top_left, top_right, bottom_right, bottom_left]

        # Create the convex definition for it
        convex = phys.Convex(square)

        sim = phys.Simulation()
        body = sim.create_body(convex)

        sim.step(1)


if __name__ == "__main__":
    Application().main()
