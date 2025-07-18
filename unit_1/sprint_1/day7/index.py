
# 📌 Day 7: Advanced OOP & Magic Methods
# Topics:

# Class methods (@classmethod) & Static methods (@staticmethod)

# Magic methods (__str__, __repr__, __add__)

# Abstract Base Classes (ABC, @abstractmethod)

# Property decorators (@property, @x.setter)


# class MathTools:
    
#     @staticmethod
#     def add(x, y):
#         return x + y

#     @staticmethod
#     def multiply(x, y):
#         return x * y

# # Call without creating object
# print(MathTools.add(10, 5))       # 15
# print(MathTools.multiply(4, 3))   # 12



# class MathTools:
    
#     @staticmethod
#     def add(x, y):
#         return x + y

#     @staticmethod
#     def multiply(x, y):
#         return x * y

# # Call without creating object
# print(MathTools.add(10, 5))       # 15
# print(MathTools.multiply(4, 3))   # 12


# class Box:
#     def __init__(self, items):
#         self.items = items

#     def __add__(self, other):
#         return Box(self.items + other.items)

#     def __str__(self):
#         return f"Box with items: {self.items}"

# box1 = Box(["pen", "book"])
# box2 = Box(["eraser", "scale"])

# box3 = box1 + box2
# print(box3)  # Box with items: ['pen', 'book', 'eraser', 'scale']

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def perimeter(self):
#         pass



class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)
r = Rectangle(10, 5)
print("Area:", r.area())          # 50
print("Perimeter:", r.perimeter())  # 30



class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return 3.14 * self._radius ** 2

c = Circle(5)
print(c.area)  # Output: 78.5 (no parentheses!)


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)
