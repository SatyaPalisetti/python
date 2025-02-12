'''
__str__ method is dunder method or magic method used to represent the object as string.used to print the out as string to end users.
'''
##without __str__method
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=Student("sri",20)
print(s1) 

##with __str__ it converts out put to string
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"My name is {self.name} and My age is {self.age}" 
s1=Student("ram",19)  
print(s1)            


'''
__repr__ method is dunder method or magic method used to represent the object as detailed string. Used to print the out as detailed string to developers. Simply It is used to inspect the object.
'''

#############with __repr__ method#############################################################
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __repr__(self):
        return f"My name is {self.name} and my age is {self.age}"
s1=Student("gopi",20)
print(s1)

'''
Note:
    If both methods are defined and if we call print() on this case python will use only __str__ method. If __str__ not present then only it fall back to __repr__ method.
'''

#############using both __str__ and __repr__  
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __repr__(self):
        print("__repr__ method executes")
        return f"My name is {self.name} and my age is {self.age}"
    def __str__(self):
        print("__str__ method executes")
        return f"My name is {self.name} and My age is {self.age}" 
s1=Student("ram",19)  
print(s1) 


##We said that __repr__ method used to inspect the object and gives detailed string output
##we can learn with following example(How the __repr__ used by developer)

#Example:
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def __repr__(self):
        print("__repr__method Executes")
        return f"My name is {self.name} and my age is {self.age}"
    
    def __str__(self):
        print("__str__method Executes")
        return f"My name is {self.name} and my age is {self.age}"
    
s1=Student("Ram",30)
s2=Student("Gopal",25)
print(s1)  #Here executes __str__ method because it is individual object
print(s2)  #Here executes __str__ method because it is individual object

StudentList=[Student("Ram",30),Student("Gopal",25)]
print(StudentList) #Here executes __repr__ method because it is group object. Without __repr__ we cannot print the group objects.           


      