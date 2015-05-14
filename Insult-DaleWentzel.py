import random
import time
f=open("Insult.txt","w")
a= "Rendering insults"
print (a) 
f.write(a +"\n")
time.sleep(.5)
b= ". . ."
print (b)
f.write(b + "\n")
time.sleep(.5)
c= "Almost there"
print (c)
f.write(c +"\n")
time.sleep(.5)
print (b)
f.write (b + "\n")
time.sleep(.5)

repeat=1
while repeat>=1:

    term1=["Dalcop","Gnashgabing","Snoutbandish","Bobolyne","Bespaling",
           "Manky","Barmy","Dodgy","Scullion","Rank",
           "Lumpish","errant","droning","Wayward","Frothy"]
    term2=["Fopdoodle","Loiter-slack","Yaldson","Tallowcatch","Stampcrab",
           "Quisby","Pillock","Naff","Maggot","fustilarion",
           "Idle-headed","Half-faced","pox-marked","rump-fed","hobby-horse"]
    term3=["Cumberworld","Gobermouch","Mumblecrust","sorner","Smell-feast",
           "Klazomaniac","Muppet","Scrubber","Stewed Prune","Dewberry",
           "Tosser", "lout","Giglet","Lewdster","Clotpole"]
    statement1=["Thou art a","Thou","Hast thee any sense, you",]
    statement=random.choice(statement1)
    first=random.choice(term1)
    second=random.choice(term2)
    third=random.choice(term3)
    output="%s %s %s %s." % (statement, first, second, third)
    print (output )
    f.write(output + "\n" +"\n")
    again=input ("Dost thou desire to be insulted yet again? 1:yes 2:no   ")
    if again== "1":
        repeat+=1
        print ("\n")
    else:
        repeat=0
        time.sleep(5)
        
f.close()
