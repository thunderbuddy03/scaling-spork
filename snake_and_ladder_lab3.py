#inserting the random function
import random

#assuming ctr as 0
ctr=0
print("WELCOME!!LET'S PLAY THE GAME OF SNAKE AND LADDER")
print("YOUR CURRENT POSITION IS ",ctr)
#while condition repeating the set of statements assuming ctr=0 till it reaches 100
while(ctr<100):
    r=random.randint(1,6)
    j=input("PRESS ENTER TO ROLL THE DICE")
    ctr=ctr+r
    print("YOUR CURRENT POSITION IS ",ctr)
    #ifcondition ctr moves from 8 to 37
    if ctr==8:
        ctr=37
        print("YOU CLIMBED THE LADDER FROM 8 TO 37")
        #elifconditon ctr moves from 11 to 2
    elif ctr==11:
        ctr=2
        print("SNAKE BIT YOU..:( MOVE DOWN TO 2")
        #elifcondition ctr moves from 25 to 4
    elif ctr==25:
        ctr=4
        print("SNAKE BIT YOU..:( MOVE DOWN TO 4")
        #elifcondition ctr moves from 13 to 34
    elif ctr==13:
        ctr=34
        print("YOU CLIMBED THE LADDER FROM 13 TO 34")
        #elif condition ctr moves from 38 to 9
    elif ctr==38:
        ctr=9
        print("SNAKE BIT YOU..:( MOVE DOWN TO 9")
        #elif condition ctr moves from 40 to 68
    elif ctr==40:
        ctr=68
        print("YOU CLIMBED THE LADDER FROM 40 TO 68")
        #elif condition ctr moves from 52 to 81
    elif ctr==52:
        ctr=81
        print("YOU CLIMBED THE LADDER FROM 52 TO 81")
        #elif condition ctr moves from 65 to 46
    elif ctr==65:
        ctr=46
        print("SNAKE BIT YOU..:( MOVE DOWN TO 46")
        #elif condition ctr moves from 76 to 97
    elif ctr==76:
        ctr=97
        print("YOU CLIMBED THE LADDER FROM 76 TO 97")
        #elif condition ctr moves from 89 to 70
    elif ctr==89:
        ctr=70
        print("SNAKE BIT YOU..:( MOVE DOWN TO 70")
        #elif condition ctr moves from 93 to 64
    elif ctr==93:
        ctr=64
        print("SNAKE BIT YOU..:( MOVE DOWN TO 64")
        #elif condition ctr moves to 100 game over.
    elif ctr>100:
            ctr=ctr-r
    elif ctr>=100:
        print("You won")
