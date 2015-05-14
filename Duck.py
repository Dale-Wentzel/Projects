import time
print("Welcome to my little game of Duck Duck Goose.")
name=input ("What is your name? ")
print ("%s, prepare to be amazed." % (name))
time.sleep(.5)
repeat=150
while repeat>=1:
    print ("duck")
    repeat-=1
    time.sleep(.05)
    while repeat==0:
        again=input("Shall there be more ducking, %s? " %(name))
        if again=="yes":
                repeat=repeat+150
                time.sleep(.4)
        elif again=="no":
            repeat=repeat+150
            print ("Too bad" +"\n" +"Learn to grammar")
            time.sleep(1)
        else:
            print("Goose")
            repeat=-1
            time.sleep(3)
