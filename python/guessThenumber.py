# This is a guess the number game
import random
secretNumber = random.randint(1, 20)
print("I am thinking of a number between 1 to 20")


# Ask the player to guess five times
for i in range(1, 6):
    print("Guess a number")
    ans = int(input())

    if ans < secretNumber:
        print("Your gues is too low")
    elif ans > secretNumber:
        print("Your guess is too high")
    else:
        print("You win!")
        break
if ans == secretNumber:
    print("Good Job! You guessed my number in "+str(i)+"guess!")
else:
    print("Nope. The number I was thinking of was "+str(secretNumber))
