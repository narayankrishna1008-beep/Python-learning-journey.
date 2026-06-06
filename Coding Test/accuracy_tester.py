benchmark= 0.85

new= float(input("enter your current model's accuracy rating:"))

result= (new>= benchmark)

message= "Your current model is greater or equal to benchmark,"

print(f"{message}: {result}")
