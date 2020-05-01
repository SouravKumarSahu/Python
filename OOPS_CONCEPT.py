#Inheritance in Python

#Try online at https://code.sololearn.com/cn4xU92kJpQv

class EmployeesList(list): #Inheritance in Python
    def search(self, name):
        print('inside search')
        matching_employees = []
        for emp in self:
            if name in emp.fname:
                matching_employees.append(emp.fname)
        return matching_employees
    
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

class Employee(Person): #Inheritance in Python
    all_employees = EmployeesList()
    def __init__(self, fname, lname, empid):
        Person.__init__(self, fname, lname)
        self.__empid = empid #Abstraction in Python (strong private Attribute, can't be accessed directly)
        self.all_employees.append(self)

    def getEmpid(self): #Abstraction in Python
        return self.__empid

    def getSalary(self): #Polymorphism in Python
        return 'You get Monthly salary.'

    def getBonus(self): #Polymorphism in Python
        return 'You are eligible for Bonus.'

print('#Inheritance in Python')
p1 = Person('George','Smith')
print(p1, ' : ', p1.fname, ' ', p1.lname)

e1 = Employee('Jack', 'simmons', 456342)
print(e1, ' : ', ':',e1.fname, ' ', e1.lname)
print(e1.all_employees)

e2 = Employee('John', 'williams', 123656)
print(e2, ' : ', ':',e2.fname, ' ', e2.lname)
print(e2.all_employees)
print(e1.all_employees)

print(e1.all_employees.search('J'))
print(e2.all_employees.search('o'))
print('#Inheritance in Python')


#Polymorphism in Python

class ContractEmployee(Employee): #Polymorphism in Python
    def getSalary(self):
        return 'You will not get Salary from this Organization.'

    def getBonus(self):
        return 'You are not eligible for Bonus.'

print('#Polymorphism in Python')
own_e1 = Employee('Jack', 'simmons', 456342)
contract_e2 = ContractEmployee('John', 'williams', 123656)
print(own_e1, ' : ', own_e1.getSalary())
print(own_e1, ' : ', own_e1.getBonus())
print(contract_e2, ' : ', contract_e2.getSalary())
print(contract_e2, ' : ', contract_e2.getBonus())
print('#Polymorphism in Python')

print('#Abstraction in Python')
e1 = Employee('Jack', 'simmons', 456342)
print(e1.fname, ' ', e1.lname)
print(e1.getEmpid())
#print(e1.__empid) #AttributeError: 'Employee' object has no attribute 'empid'
print('#Abstraction in Python')



print('What is the output of the following code?')
class A:
    def __init__(self, x = 5, y = 4):
        self.x = x
        self.y = y

    def __str__(self):
        return 'A(x: {}, y: {})'.format(self.x, self.y)

    def __eq__(self, other):
        return self.x * self.y == other.x * other.y

def f1():
    a = A(12, 3)
    b = A(3, 12)

    if (a == b):
        print( b != a)
        print(a)

f1()
print('What is the output of the following code?')


print('What is the output of the following code?')
class grandpa(object):
    pass

class father(grandpa):
    pass

class mother(object):
    pass

class child(mother, father):
    pass

print(child.__mro__)
print('What is the output of the following code?')
print('What is the output of the following code?')
class class1():
    a = 1
    def f1(self):
        a = 2
        class1.a += 1
        print(class1.a, end=" ")
        print(a, end=" " )

class1().f1()
class1().f1()
print('\n')
print('What is the output of the following code?')



#Define the class Point that represents x, y, and z coordinates of 3D coordinate system.
#Hint : Define the initializer method, __init__ that takes three values and assigns them to attributes x, y and z respectively.


import math
class Point():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    #Improvise the class definition of Point such that any Point object is displayed in the format point : (x, y, z).
    #Hint : Define the method __str__ inside the class Point.Execute your code and observe the output of statement print(p1).
    def __str__(self):
        return "point : ({0},{1},{2})".format(self.x,self.y,self.z)

    #Determine distance between two point Objects.
    #Hint : Define the method distance, which determines distance between two points. Use formula distance = sqrt( (x1-x2)**2 + (y1-y2)**2 + (z1 -z2)**2 ).
    #Now create two Point objects p1 = Point(4, 5, 6) and p2 = Point(-2, -1, 4) and distance of p1 from p2 using defined distance method.
    def distance(self,other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)

    #Improvise Point class definition such that, adding any two Point objects using + operator, results in a new Point object with corresponding x, y and z values being added.
    #Hint : Define __add__ method inside the class Point.Try executing print(p1 + p2) and view the result.
    def __add__(self,other):
        return Point((self.x + other.x),(self.y + other.y),(self.z + other.z))

        
p1 = Point(4,2,9)
print(p1)

p2 = Point(4, 5, 6)
p3 = Point(-2, -1, 4)
print("distance of ", p2, " from ", p3, " is", "{0:4.3f}".format(p2.distance(p3)))

print("Sum of ", p2, " and ", p3, " is ", p2 + p3)

#two similar classes using same function
class Point2():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return "point : ({0},{1},{2})".format(self.x,self.y,self.z)
    def distance(self,other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)
    def __add__(self,other):
        return Point2((self.x - other.x),(self.y - other.y),(self.z - other.z))

p4 = Point(1,1,1)
p5 = Point2(1,1,1)

print(p4 + p5)
print(p5 + p4)




#Define the function isEven which returns True, if a given number is even and returns False, if the number is odd. Define a simple class TestIsEvenMethod derived from unittest.TestCase class.
#Hint : Import unittest module and use TestCase utility of it.
#Hint : Use assertEqual method to verify the function output with expected output.
import unittest
class TestIsEvenMethod(unittest.TestCase):
    n = 0
    def isEven(self,n):
        self.n = n
        return (self.n % 2 == 0)

    #Define a test test_isEven1, that checks if isEven(5) returns False or not.
    def test_isEven1(self):
            self.assertEqual(self.isEven(5),False,'test isEven(5) failed')

    #Define another test test_isEven2, inside TestIsEvenMethod, that checks if isEven(10) returns True or not.
    def test_isEven2(self):
             self.assertEqual(self.isEven(10),True,'test isEven(10) failed')

    #Define one more test test_isEven3, inside TestIsEvenMethod, that checks if isEven function raises TypeError when a string hello is passed as argument.
    def test_isEevn3(self):
        self.assertEqual(self.isEven('hello'),True,'test isEven(hello) failed')
        with self.assertRaises(TypeError):
            print('output of isEven(hello) gives TypeError')

if __name__ == '__main__':
    unittest.main()
