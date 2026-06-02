low_safe= 20.0
high_safe= 75.0

temp= float(input("enter the lowest temperature:"))

test= (low_safe < temp) and (high_safe >= temp)

message= "processor thermal safety status"
M= message.title()

print(f"{M}: {test}")