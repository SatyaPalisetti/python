##identity operatot
'''
used to compare the memory locations of two objects.it determine two different variables it contains same object in memory.
there are two identity operators "is" and "is not"
is--same object is true otherwise false
is not--do not refer to the same object is true,otherwise false 
'''

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)
# returns False because z is the same object as x

print(x is not y)
# # returns True because x is not the same object as y, even if they have the same content

print(x != y)
# # to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y.

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
# # returns True because z is the same object as x

print(x is y)
# # returns False because x is not the same object as y, even if they have the same content

print(x == y)
# # to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y