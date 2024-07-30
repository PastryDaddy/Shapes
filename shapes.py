import abc
class Shape:
    @abc.abstractmethod
    def __init__(self, color):
        self.color = color

    @abc.abstractmethod
    def Area(self):
        return NotImplementedError
    

    def Perimeter(self):
        return NotImplementedError
    
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color

class Circle(Shape):
    def __init__(self, radius, color):
        self.radius = float(radius)
        self.color = color

    def Area(self):
        return 3.14 * self.radius ** 2
    
    def Perimeter(self):
        return 2 * 3.14 * self.radius
    
    def getRadius(self):
        return self.radius
    
    def setRadius(self, radius):
        self.radius = float(radius)

    def getColor(self):
        return self.color
    
    def setColor(self, color):
        self.color = color


class Rectangle(Shape):
    def __init__(self, length, width, color):
        self.length = float(length)
        self.width = float(width)
        self.color = color

    def Area(self):
        return self.length * self.width
    
    def Perimeter(self):
        return 2 * (self.length + self.width)
    
    def getLength(self):
        return self.length
    
    def setLength(self, length):
        self.length = float(length)

    def getWidth(self):
        return self.width
    
    def setWidth(self, width):
        self.width = float(width)

    def getColor(self):
        return self.color
    
    def setColor(self, color):
        self.color = color


class Triangle(Shape):
    def __init__(self, side1, side2, side3, color):
        self.side1 = float(side1)
        self.side2 = float(side2)
        self.side3 = float(side3)
        self.color = color

    def Area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5
    
    def Perimeter(self):
        return self.side1 + self.side2 + self.side3
    
    def getSide1(self):
        return self.side1
    
    def setSide1(self, side1):
        self.side1 = float(side1)

    def getSide2(self):
        return self.side2
    
    def setSide2(self, side2):
        self.side2 = float(side2)

    def getSide3(self):
        return self.side3
    
    def setSide3(self, side3):
        self.side3 = float(side3)

    def getColor(self):
        return self.color
    
    def setColor(self, color):
        self.color = color

def Shaper():
    circle = Circle(7, "red")
    rectangle = Rectangle(9, 3, "blue")
    triangle = Triangle(7, 15, 12, "green")
    shapes = [circle, rectangle, triangle]
   
    for shape in shapes:
        print(f"Shape: {type(shape).__name__}")
        print(f"Area: {shape.Area()}")
        print(f"Perimeter: {shape.Perimeter()}")
        print(f"Color: {shape.getColor()}")
        print()

if __name__ == "__main__":
    Shaper()

   
   
    