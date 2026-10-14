# Exercise: Circle Class
import math

class Circle:
    def __init__(self, radius=1.0):
        self.radius = float(radius)

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    def area(self):
        return math.pi * (self.radius ** 2)

    def __str__(self):
        return f"Circle(radius={self.radius}, diameter={self.diameter})"

    def __repr__(self):
        return f"Circle(radius={self.radius})"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        raise TypeError("Can only add two Circle instances")

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented

# Testing the implementation
c1 = Circle(5)
c2 = Circle.from_diameter(20)

print(c1)
print(f"Area of c1: {c1.area():.2f}")
print(f"Diameter of c2: {c2.diameter}")

c3 = c1 + c2
print(f"Combined circle: {c3}")

print(f"Is c1 bigger than c2? {c1 > c2}")

circles = [Circle(3), Circle(1), Circle(5), Circle(2)]
circles.sort()

print("Sorted circles:")
for circle in circles:
    print(circle)