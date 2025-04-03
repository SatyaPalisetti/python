#file handling
'''
file handling is an essential concept that allows you to read from and write to files. python provides buillt in functions to handle files in an easy and efficient way
'''

#Create a sample file sample1.py and create the below text
# Hello Welcome to python.

#Now do operations on demo.txt
#Example:
#1. ''' reading from a file'''
s=open('sample.py',mode='r')
print(s.read())
s.close()

#using with 
with open("sample1.py","r") as file:
    content=file.read()
    print(content)
    
    
#2.''' file in write mode'''
s=open('sample1.py',mode='w')
s.write("Bye Bye")
s.close()

#use with
with open("sample1.py","w") as file:
    file.write("this is a file handling example")
    print("data written successfully")

#Example
#3.''' open append close'''
s=open('sample1.py',mode='a')
s.write("Bye Bye append")
s.close()

#use with
with open("sample1.py",'a') as file:
    file.write("new content to the file")
    print("data append successfully")

#4.reading a file line by line
with open('sample1.py','r') as file:
    for line in file:
        print(line.strip())  #strip()removes extra newlines

#5.copying a file
with open('sample1.py','r') as source,open('sample2.py','w') as destination:
    for line in source:
        destination.write(line)  #or destination.write(source.read())
print('file copied successfully')  


with open('sample1.py','r') as source:
 with open('sample2.py','w') as destination:
     destination.write(source.read())
print('file copied successfully')  
                         

#Example:
''' open read and write close'''
s=open('sample1.py',mode='r+')
print(s.read())
s.write("r+ mode")
s.close()

#Example:
''' open write and read close'''
s=open('sample1.py',mode='w+')
print(s.tell()) #tell is used to know the current cursor pointer place
s.write("w+ mode")
print(s.tell())
s.seek(0) #seek is used to Move the file pointer to a specific position.
print(s.tell())
print(s.read())
s.close()

#example
file=open('sample1.py','w+')
s.write("satyadevi")
s.seek(0)   #index
print(file.read())
file.close()

#6.Using with statement
'''In Python, it's a good practice to use the with statement when working with files. This ensures that the file is properly closed after its block is executed, even if an exception occurs.'''

#Example: Using with to read a file
# Using 'with' ensures the file is automatically closed
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
    
#Example: Using with to write to a file
with open('example.txt', 'w') as file:
    file.write("This is written using the 'with' statement.\n")
    file.write("It will automatically close the file when done.")

#7.Checking if a File Exists
#You might want to check if a file exists before opening it. You can use the os module for this:
import os

if os.path.exists('example.txt'):
    with open('example.txt', 'r') as file:
        print(file.read())
else:
    print("The file does not exist.")

#8. count the number of words in file
with open('sample1.py','r') as file:
    text=file.read()
    words=text.split()
    print('number of words', len(words))

#9.deleting a file
import os
if os.path.exists('sample1.py'):
    os.remove('sample1.py')
    print('file deleted successfully')
else:
    print('file does not exist')    

#10.writing and reading binary files
#writing a binary file
with open('sample.py','wb') as file:
    file.write(b"hello, binary world")
    print('binary file written successfully')

#reading a binary file
with open('sample.py','rb') as file:
    content=file.read()
    print('binary content',content)
    
    