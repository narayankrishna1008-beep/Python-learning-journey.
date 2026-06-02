master_username= "Krishna/1008"
master_passcode= "K1230"

text_1= input("enter your username here:")
text_2= input("enter your passcode here:")

test= (master_username==text_1) and (master_passcode==text_2)

message= "these two inputs are equal"

print(f"{message}: {test}")