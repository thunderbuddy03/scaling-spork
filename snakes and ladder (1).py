import random

ctr=0
print("WELCOME!!LET'S BEGIN THE GAME OF SNAKE AND LADDER")
print("YOUR CURRENT POSITION IS ",ctr)
while(ctr<100):
    i=random.randint(1,6)
    j=input("PRESS ENTER TO ROLL THE DICE")
    ctr=ctr+i
    print("YOUR CURRENT POSITION IS ",ctr)
    if ctr==8:
        ctr=37
        print("YOU CLIMBED THE LADDER FROM 8 TO 37")
    elif ctr==11:
        ctr=2
        print("SNAKE BIT YOU..:( MOVE DOWN TO 2")
    elif ctr==25:
        ctr=4
        print("SNAKE BIT YOU..:( MOVE DOWN TO 4")
    elif ctr==13:
        ctr=34
        print("YOU CLIMBED THE LADDER FROM 13 TO 34")
    elif ctr==38:
        ctr=9
        print("SNAKE BIT YOU..:( MOVE DOWN TO 9")
    elif ctr==40:
        ctr=68
        print("YOU CLIMBED THE LADDER FROM 40 TO 68")
    elif ctr==52:
        ctr=81
        print("YOU CLIMBED THE LADDER FROM 52 TO 81")
    elif ctr==65:
        ctr=46
        print("SNAKE BIT YOU..:( MOVE DOWN TO 46")
    elif ctr==76:
        ctr=97
        print("YOU CLIMBED THE LADDER FROM 76 TO 97")
    elif ctr==89:
        ctr=70
        print("SNAKE BIT YOU..:( MOVE DOWN TO 70")
    elif ctr==93:
        ctr=64
        print("SNAKE BIT YOU..:( MOVE DOWN TO 64")
    elif ctr>=100:
        print("You won")


