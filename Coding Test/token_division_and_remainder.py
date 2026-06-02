tokens= int(input("enter the total count of text tokens:"))
nodes= int(input("enter the number of worker nodes:"))

share= tokens//nodes
leftover= tokens%nodes

print(f'''each worker gets {share} tokens
      remaining tokens = {leftover} ''')
