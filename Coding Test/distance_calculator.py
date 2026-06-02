position_A= float(input("enter your first coordinate:"))
position_B= float(input("enter your second coordinate:"))

minus=(position_B-position_A)

distance= abs(minus)

message= "absolute spatial distance"
M= message.title()

print(f"{M}: {distance}")