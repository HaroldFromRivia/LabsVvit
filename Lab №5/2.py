class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, newrad):
        self.radius = newrad


c1 = Circle(10)
print(c1.get_radius())
c1.set_radius(115)
print(c1.get_radius())
