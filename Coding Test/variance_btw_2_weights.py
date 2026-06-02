ow= float(input("enter your original weight here:"))
nw= float(input("enter your new weight here:"))

diff= (ow - nw)
D= abs(diff)

product= round(D*100,1)

message= "variance between both weights is"
M= message.upper()

print(f"{M}: {product}")
