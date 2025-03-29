#1. IS-A Relationship / Inheritance
'''
Inheritance is a mechanism for creating a new class from an existing class.
Here the old class is called Base class and the new class is called Derived class.
'''

#Example:
'''
class A -->Old class/ Base Class/ Parent Class
  ..
  ..
  ..
  ..
  ..
class B(A) -->New Class/ Derived Class/ Child Class/ Sub Class/ Extended Class.
'''

#Example:
'''
            Person
            *    *
     IS-A  *      * IS-A
          *        *
         *          *
    Employee        Student
    
In the above 
    Employee IS-A Person.
    Student IS-A Person           
'''

#Example:
class A:
    def method1(self):
        print("A class Method1")
    def method2(self):
        print("A class method2")
class B:
    def method3(self):
        print("B class method3")

b=B()
b.method3()
b.method1() #Here B object has no attribute 'method1'

#Example:
class A:
    def method1(self):
        print("A class Method1")
    def method2(self):
        print("A class method2")
class B(A):    #Here B extends a
    def method3(self):
        print("B class method3")

b=B()
b.method3()
b.method1() #Here it works

'''
B class method3
A class Method1
'''
