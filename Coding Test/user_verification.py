master_username= "admin_user"

text= input("enter your current login username: ")
con= text.lower()

test= (master_username == con)

message= "you are verified as a authentic user"
M= message.upper()

print(f"{M}: {test}")