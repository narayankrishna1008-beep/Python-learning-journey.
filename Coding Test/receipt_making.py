name= input("enter your account name: ")
num= float(input("enter the total number of text words processed: "))

N= name.upper()

wc= 0.05

cost= round(num * wc,2)

message= "compute session receipt"
M= message.upper()
message2= "account user:"
M2= message2.title()
message3= "words scanned:"
M3= message3.title()
message4= "total cost:"
M4= message4.title()

print(f"=== {M} ===\n{M2} [{N}]\n{M3} [{num}]\n{M4} [{cost}] INR \n=============================================")  