f=open("Adventure.txt","w")
user=input ("What is your name?")
print ("""Welcome, %s, to an interactive and entirely hypothetical story written
       by me and completed by you.""" %(user))
print ("""Our story begins on a miserable spring day in rainy Seattle. You find
yourself seated in a local coffeeshop with a friend; in total there are 8
people in the shop. In the far corner the members of a band from your school
are discussing an upcoming show, near the front window facing away from you
is the librarian that lives down the street from you, and a hipster college
student is at the counter ordering her coffee. You glance out the window and
notice that a windowless white van has pulled up and 3 unidentifiable figures
are approaching the door.""")
run=("""You manage to slip out the back door unseen, but your friend wasn't quite as lucky as you and was forced to stay inside.""") 
hide=("""You and your friend quietly reach the restroom before the door opens and after a few seconds hear shouting followed by silence.""")
scream=("""You alert the coffeeshop employee to the approaching threat and he activates a silent alarm""")
stay=("""You casusally continue drinking your coffee.""")

areyousure=("Do you want to prove your loyalty to your friend by going back inside? Choose 'yes' or 'no' ")
areyousure2=("Not everyone is fit to be a hero, maybe next time.")
reenter=("""You find a metal garbage can lid and make for the door. Once inside you can hear a man talkng, but no one replies to him. Do you enter the room
nonchalantly or peek in to see what's going on?""")
peek=("""You see the figures standing by the counter, one has a gun pointed at the employee, another is putting coffee grounds in a backpack and the third is
watching the rest of the room's occupants. You decide your best options are to leave and let them have their coffee(I mean it's just coffee) or create a
distraction by knocking on the wall with the lid.""")
enter=("""You walk blindly into the room with the lid. You only have enough time to see a gun pointed in your direction before you hear a loud crack
followed by a streak of white...""")
sorrymate=("""Concerned only with your own safety, you quickly distance yourself from the shop. After a few minutes you decide to call your friend to make
sure everything's ok. He doesn't answer, but calls back a few hours later telling you what happened after your escape.""")
distract=("""You knock on the wall a few times and after a few seconds you hear footsteps coming your way, when the figure gets around the corner and when you
see the gun you put the lid down and surrender. """)

reaction2=("""Curious to the cause of the silence, your friend motions to open the door.""")
leavebathroom1=("""You allow your friend to open the door and see the figures standing by the counter, one has a gun pointed at the employee, another is putting coffee in a backpack and the third is
watching the rest of the room's occupants, and is now aware of your presence and shouts at you to open the door and come out.""")
stay2=("""You move in fromt of the door and shake your head no. After a few minutes of continued silence, you decide it's worth checking and signal your friend to open the door.""")
leavebathroom2=("""After opening the door you see that the figures have left and been replaced by Police Officers who are rather shocked to see you and your friend stumble out of the restroom.""")
leave=("""You step out with your hands up in surrender and sit down at a table as directed. A few minutes later, after the figures are satisfied with their coffee, they leave and the employee calls the Police.""")
closethedoor=("""Stubbornly you close the door and retreat to a stall. As soon as the door is closed one of the figures shoots the door 3 times and then enters the restroom. The last thing you see is the silver barrel of the gun as you
stand quivering on a toilet.""")

END=("GAME OVER")
WINkinda=("CONGRATULATIONS! You, have survived along with everyone else!")
END2=("Well... At least you aren't dead..")
WIN=("CONGRATULATIONS! You survived and saved the coffee!")
print("""Assuming the figures are armed, you realize that you can run and escape through the back door, hide and hope they don't find you, alert the others to the threat, or stay where you are and see what happens.""")
repeat=1
while repeat>=1:
    reaction1=input ("How do you react? Choose 'run' 'hide' 'scream' or 'stay': ")
#run
    if reaction1== ("run"):
        print ("%s" %(run))
        repeat2=1
        while repeat2>=1:
            reaction1a=input("%s" %(areyousure))
            if reaction1a==("yes"):
                print("%s"%(reenter))
                reaction1aa=input ("Do you 'peek' or 'enter'? ")
                if reaction1aa==("peek"):
                    print("%s"%(peek))
                    reaction1aaa=input ("Will you 'leave' or 'distract'? ")
                    if reaction1aaa==("leave"):
                        print ("%s"%(sorrymate))
                        print("%s"%(WINkinda))
                        repeat=0
                        repeat2=0
                    elif reaction1aaa==("distract"):
                        print ("%s"%(distract))
                        print ("%s"%(END2))
                        print ("%s"%(END))
                        repeat=0
                        repeat2=0
                elif reaction1aa==("enter"):
                    print("%s"%(enter))
                    print("%s"%(END))
                    repeat=0
                    repeat2=0
            elif reaction1a==("no"):
                print("%s"%(sorrymate))
                print("%s"%(WINkinda))
                repeat=0
                repeat2=0
        else:
            repeat2+=1
#hide
    elif reaction1==("hide"):
        print (hide)
        repeat3=1
        while repeat3>=1:
            reaction2=input ("Do you 'allow' him to open it or do you 'stop' him?")
            if reaction2==("allow"):
                print("%s" %(leavebathroom1))
                reaction2a=input("Do you 'leave' the bathroom or 'close the door' and make them come in after you?")
                if reaction2a==("leave"):
                    print ("%s" %(leave))
                    print ("%s"%(END2))
                    repeat=0
                    repeat2=0
                    repeat3=0
                elif reaction2a==("close the door"):
                    print ("%s" %(closethedoor))
                    print("%s"%(END))
                    repeat=0
                    repeat2=0
                    repeat3=0
            elif reaction2==("stop"):
                print ("%s%s" %(stay2,leavebathroom2))
                print ("%s"%(WINkinda))
                repeat=0
                repeat2=0
                repeat3=0
                
        else:
            repeat3+=1
#scream
    elif reaction1==("scream"):
        print("%s" %(scream))
#stay
    elif reaction1==("stay"):
        print ("%s" %(stay))
    else:
        repeat+=1
