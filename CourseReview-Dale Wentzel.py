f=open("CourseReview_DaleWentzel.txt", "w")
Q1=input("What did you like/dislike about Code Academy? ")
f.write(Q1+"\n")
Q2=input("What did you enjoy most about the class? ")
f.write(Q2+"\n")
Q3=input("How was the pace of the class? (good, too fast, too slow) ")
f.write(Q3+"\n")
Q4=input("What would you change about the class? ")
f.write(Q4+"\n")
Q5=input("Would you recommend this class to a friend? Why/why not? ")
f.write(Q5+"\n")
f.close()
