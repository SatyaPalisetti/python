##variable
'''In Python, variables are used to store data that can be referenced and manipulated during program execution.
A variable is essentially a name that is assigned to a value. Unlike many other programming languages, Python variables do not require explicit declaration of type.
The type of the variable is inferred based on the value assigned.
Variables act as placeholders for data. They allow us to store and reuse values in our program.'''

x=5
y="John"
print(x)
print(y)

x=4
x="ram"
print(x)

x=y=z="orange"   #here we can one value to multi variables
print(y)

x="ram","banti","chanti"   #Here we can assings multiple values using one variable at atime
print(x)

x,y,z="ram","banti","chanti"  #Here we can assign multiple values to multiple variables at a time
print(x)
print(y)
print(z)

x="hello"
y="world"
z=x+y
print(z)
print("Answer is:" +z)

x="hello"
y=2
z=x+y
print(z) #shows an error because we cannot add number and word
print("Answer is:" +z)

a="apple"
def sample():
    print(a)
sample()

x="awesome"
def sample():
    x="fantastic"
    print("python is:" +x)
sample()
print("python is:" +x) 

global variable
x="awesome"
def sample():
    print("python is:" +x)
sample()    

x="awesome"
def sample():
    global x    #global is a keyword is used to change the global variables in local as well
    x="fantastic"
    print("python is:" +x)
sample()
print("python is:" +x)       
     
a=10
b=10
print(id(a)) #if the value is same address is also same
print(id(b))   