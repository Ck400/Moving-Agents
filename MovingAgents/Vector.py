# Class used for creation of Vector objects
class Vector:

    # Called on initilization
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # String Overload
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    # Addition Overload
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # Subtraction Overload
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    # Dot Product Method
    def dot(self, other):
        return float(self.normalize().x * other.normalize().x + self.normalize().y * other.normalize().y)

    # Scale Method
    def scale(self, scale):
        return Vector(self.x * scale, self.y * scale)

    # Calculate Length Method
    def length(self):
        return (self.x**2 + self.y**2)**0.5

    # Normalize a Vector
    def normalize(self):
        mag = self.length()
        if (mag == 0):            
            return Vector(0,0)
        else:
            return Vector(self.x / mag, self.y / mag)



