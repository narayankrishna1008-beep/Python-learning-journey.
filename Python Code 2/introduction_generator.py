name = input("enter your name here: ")
age = int(input("enter your age here: "))
city = input("enter your city here: ")

statement1 = ("hello, one and all present here, my name is :-  ").capitalize()
statement2 = ("and my current age is :-  ")
statement3 = ("and my hometown is :-  ")
statement4 = ("I'm very proud of my skills, whether it is of technical or martial arts.")

print(f"{statement1}{name.title()}\n{statement2}{age}\n{statement3}{city.upper()}\n{statement4}")