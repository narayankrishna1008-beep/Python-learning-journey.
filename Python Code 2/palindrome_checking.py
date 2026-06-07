l = []

statement = input("enter your word here: ")
statement1 = input("enter your word here: ")
statement2 = input("enter your word here: ")
statement3 = input("enter your word here: ")

l.append(statement)
l.append(statement1)
l.append(statement2)
l.append(statement3)

copy_l = l.copy()
copy_l.reverse

if (l == copy_l):
     print("It is a palindrome.")

else:
     print("It is not a palindrome.")
