class Circle:
    # class attributes
    pi = 3.14
    all_circles = [] # list
    
    def __init__(self, radius):
		# Constructor
        self.radius = radius
        self.__class__.all_circles.append(self)
        
    def area(self):
        return self.__class__.pi * (self.radius ** 2)
    
    @staticmethod # remark1
    def total_area(): # remark2
        total = 0
        for circle in Circle.all_circles:
            total += circle.area()
        return total
    
    @classmethod # remark1
    def total_area2(cls): # remark2
        total = 0
        for circle in cls.all_circles:
            total += circle.area()
        return total
    
    
c1 = Circle(10)
c2 = Circle(15)
print(c1.total_area())
print(c1.total_area2())