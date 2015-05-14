import random
repeat1=1
while repeat1>=1:
    term1=["Kind","Gentle","Brave","Flower","Faultless",
           "All Knowing","Honorable","Pleasant","Tolorable","Educated",
           "Unmatched","Genuinely","Doubtless","Trusting",]
    term2=["Sensible","Classy","Exsquisite","Exuberant","Fashionable",
	   "Stylish","Andventurous","Swift","Decisive","Quick-witted",
	   "Tactful","Amiable","Jovial","Resourceful","Punctual"]
    term3=["Soul","Master","Captain","Magistrate","Teacher",
	   "Guide","Gentleman","Bard","Manager","Elder",
	   "Warrior","Lord","Jarl","Hero","Messenger"]
    statement1=["Oh","Fearless leader, you are a(n)"]
    statement=random.choice(statement1)
    first=random.choice(term1)
    second=random.choice(term2)
    third=random.choice(term3)
    print (statement ,first ,second ,third,".")
    again=input ("Does your excellency wish to receive another compliment? ")
    if again==("yes"):
        print ("-------------------------------------------------------------------")
        repeat1=1
    else:
        print ("Good Bye.")
        print ("-------------------------------------------------------------------")
        repeat1=0
