import math
test=1
print ("Find your score with Grade Converter 2.0!")
while test>=1:
    score=input("points earned: ")
    possible=input("total possible points: ")
    gradedecimal= float(score)/float(possible)
    grade= gradedecimal*100
    print (grade)
    if grade>=100:
        print ("A+")
        test=0
    elif grade>=91 and grade<100:
        print ("A")
        test=0
    elif grade>=81 and grade<91:
        print ("B")
        test=0
    elif grade>=71 and grade<81:
        print ("C")
        test=0
    elif grade>=61 and grade<71:
        print ("D")
        test=0
    else:
        print ("F")
        test=0
    again=input("Enter another score? 1:yes; 2:no ")
    if again==("1"):
        print("\n")
        test=1
    else:
        test=0
    

