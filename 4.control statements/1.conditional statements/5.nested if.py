##nestedif
'''
if statement placed inside another if statement. it allows for more complex decision making processes by evaluating multiple conditions sequentiallly
'''
x=int(input("Enter a sample number:"))

if x > 10:
    print("Above ten")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
else:
    print("above all cases failed")