class Shape:
    def area(self):
        raise NotImplementedError(print("Derived classes need to override this method."))
    
class Rectangle:
    
    def area(self, length, width):
        return length * width
    
class Circle:
    def area(self, radius):
        import math
        return math.pi * (radius * radius)
    