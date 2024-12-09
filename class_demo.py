import math
class Shape:
    def __init__(self,l):
        self.length=l


class Circle(Shape):
    def __init__(self, l):
        Shape.__init__(self,l)
    
    def area(self):
        return math.pi*self.length**2

class Rect(Shape):
    def __init__(self,l,b):
        Shape.__init__(self, l)
        self.breadth=b

    def area(self):
        return self.length*self.breadth

def main():
    c=Circle(7)
    r=Rect(7, 10)
    print('Area of circle = ',c.area())
    print('Area of rectangle = ',r.area())

main()