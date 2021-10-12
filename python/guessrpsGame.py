import random, sys

print("Rock, Paper, Scissors")
#The variable keep track of the number of wins, loose, and ties
wins=0
losses=0
ties=0

while True:
    print(wins, "wins,",losses, "Losses", ties, "Ties")
    while True:
        print("Enter your move: (r)ock, (p)aper, (s)cissprs or (q)uit")
        playerMove=input()
        if playerMove=="q":
            sys.exit()
        if playerMove=="r" or playerMove=="p" or playerMove=="s":
            break # break out of the player input loop.
        print("Type one of r,p,s or ,q.")
    if playerMove=="r":
        print("Rock versus...")

    elif playerMove=="p":
        print("Paper versus...")

    elif playerMove=="s":
        print("Scissors versus...")

#Display what the computer choose:
    randomNumber= random.randint(1,3)
    if randomNumber ==1:
        computerMove="r"
        print("Rock")
    elif randomNumber ==2:
        computerMove="p"
        print("Paper")
    elif randomNumber ==3:
        computerMove="s"
        print("SCissors")

    #Display and Record win/loss/tie
    if playerMove==computerMove:
        print("Ties!!")
        ties+=1
    elif playerMove=="r" or computerMove=="s":
        print("You win")
        wins+=1
    elif playerMove=="p" or computerMove=="r":
        print("You win")
        wins+=1
    elif playerMove=="s" or computerMove=="p":
        print("You win")
        wins+=1
    elif playerMove=="r" or computerMove=="p":
        print("You lose")
        losses+=1
    elif playerMove=="p" or computerMove=="s":
        print("You lose")
        losses+=1
    elif playerMove=="s" or computerMove=="r":
        losses+=1