passkey= input("enter your passkey:")

L= len(passkey)

test1= (L > 8)
test2= ( passkey == passkey.lower())

print(f'''correct passkey length: {test1}
passkey in lowercase: {test2} ''')