a = int(input("enter your fist number here: "))
b = int(input("enter your second number here: "))
c = int(input("enter your third number here: "))

if (a>=b and a>=c):
    print("Greatest number is", a)

elif (b>=c):
    print("Greatest number is", b)

else:
    print("Greatest number is", c)