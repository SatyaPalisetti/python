##control statements
'''
control statements manage the order in which code is executed . they enable decision making, repettion and flow control within programms
'''
##conditional statements
'''fundamental programming constructs that allow you to control the flow of your program based on conditions that you specify.(if,els,elif)
progrmas to execute different code blocks based on whether a certain condition is true or false'''

##if
'''
the block of code only specified condition is true
'''
if 5>2:
    print("This is if")

# Write a program to print largest number
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
c=int(input("Enter c value:"))
# Here checks all the conditions
if a>b & a>c:
    print("a is big")
    
if b>c & b>a:
    print("b is big")
    
if c>b & c>a:
    print("c is big")