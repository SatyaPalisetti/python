a=10.7
print(a)
print(type(a))
print(id(a))

a="satya"
print(a)
print(type(a))
print(id(a))

x=8
y=2.8
z=1j
print(type(x))
print(type(y))
print(type(z))

x=1
y=2.8
z=1+10j
a=float(x)
b=int(y)
c=complex(x)
print(z.real)
print(z.imag)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))


##some IMP INBUILT FUNCTIONS before concept:
#Random Number
'''python does not have a random() function to make a random number , but python has a built in module called random that can be used to make random numbers'''
##Example
import random
print(random.randrange(1,10))


#input function
a=int(input("enter the input:"))
print(a)

#If suppose if we give specific data type it will take that type of data only as input.
a=int(input("Enter the input:"))
print(a)
print(type(a))

#But the input() default type is string.

# Types to print the output

# 1.Print with the print function
X=10
print(X)

#print with string formatting%
name="satya"
age=20
print(f"My name is %s and my age is %d"%(name,age))

##print with the str.format() method
name="gopi"
age=20
print("my name is {} and my age is {}".format(name,age))
name1="raj"
print("my name is {name} and my age is{age}".format(name=name1,age=age))
course="Python"
price=2.99 #print this is dollar format
print("My course is {} and the price is ${price:.1f}".format(course,price=price))


##4.print with f string
name="satya"
print(f"My name is {name}")

salary=10000
tax=0.2
print(f"my monthly salary is ${salary-tax}")

## 5.Print to a file or a stream
##printing to a file
with open('result.txt',w) as f:
    print("this will return to a file", file=f)

#printing to a stream  
import sys
print("This will return to a stream", file=sys.stderr)