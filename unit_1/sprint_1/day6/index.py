# 📌 Day 6: Object-Oriented Programming (OOP)
# Topics:

# Classes & objects (class, self)

# Constructors (__init__)

# Inheritance (class Child(Parent))

# Encapsulation (private/public attributes)

# Polymorphism & Method overriding


class Animal:
    def add(self,a,b):
        return a+b
    
s1 = Animal()
p1 = s1.add(10,20)
print("sum :",p1)

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

# Inheritance (class Child(Parent))


# single inheritance 

class parent:
    def show(self):
        print("this is parent class")

class child(parent):
    def display(self):
        print("this is child class")

s1 = child()
s1.display()
s1.show()



# # multiple inheritance    

class Grandfather:
    def g_property(self):
        print("Grandfather’s Property")

class Father(Grandfather):
    def f_property(self):
        print("Father’s Property")

class Son(Father):
    def s_property(self):
        print("Son’s Property")



# Multiple Inheritance

class Father:
    def dad(self):
        print("Father’s feature")

class Mother:
    def mom(self):
        print("Mother’s feature")

class Child(Father, Mother):
    def child(self):
        print("Child’s feature")

c = Child()
c.dad()
c.mom()
c.child()




# Encapsulation (private/public attributes)


class student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks  # private attribute
    def display(self):
        print(f"Name: {self.name}, Marks: {self.__marks}")

s1 = student("Nitish",99)
s1.display()




class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def show_salary(self):
        print(f"{self.name}'s Salary: ₹{self.__salary}")

emp = Employee("John", 50000)
print(emp.name)          # ✅
emp.show_salary()        # ✅
# print(emp.__salary)    ❌ will cause error


#  Polymorphism & Method overriding

class car:
    def drive(self):
        print("Driving a car")  

class boat:
    def drive(self):
        print("Sailing a boat") 

class plane:
    def drive(self):
        print("FLying in the sky")


def start_journey(vehicle):
    vehicle.drive()
start_journey(car())
start_journey(boat())
start_journey(plane())


# Method Overriding Example 

import math

class Shape:
    def area(self):
        pass  # abstract behavior

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Polymorphism in action
shapes = [Square(4), Circle(3)]

for s in shapes:
    print("Area:", s.area())
