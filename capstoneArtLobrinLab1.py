#prompts and receives input#
grade = input("Enter mark from 1 to 100: ")
#assess input is dig. ruling out strings or other than 1-100 scope#
if grade.isdigit() and 1 <= int(grade) <= 100:
#makes var#
    grade = int(grade)
#validation=result#
    if 80 <= grade <= 100:
        print("A")
    elif 70 <= grade <= 79:
        print("B")
    elif 60 <= grade <= 69:
        print("C")
    elif 50 <= grade <= 59:
        print("D")
    elif 1 <= grade <= 49:
        print("F")
#catches everything else+recourse#
else:
    print("start over")