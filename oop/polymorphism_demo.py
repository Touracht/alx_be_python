class Shape:
    def area(self):
        raise NotImplementedError(print("Derived classes need to override this method."))
    
class Rectangle(Shape):
    
    def area(self, length, width):
        return length * width
    
class Circle(Shape):
    def area(self, radius):
        import math
        return math.pi * (radius * radius)
    