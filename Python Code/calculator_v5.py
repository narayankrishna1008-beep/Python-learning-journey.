english= float(input("enter your marks in english:"))
hindi= float(input("enter your marks in hindi:"))
science= float(input("enter your marks in science:"))
mathematics= float(input("enter your makrs in matematics:"))
social_science= float(input("enter your marks in S.S.T:"))
sanskrit= float(input("enter your marks in sanskrit"))

marks_scored= (english+hindi+science+mathematics+social_science+sanskrit)
total_marks= 600

percentage=((marks_scored/total_marks)*100)

print("your total percentage is:", round(percentage,2))