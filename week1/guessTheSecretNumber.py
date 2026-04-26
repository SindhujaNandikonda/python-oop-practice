import random 

secretNumber = random.randint(1, 20)
print("I am thinking of a number between 1 and 20.")
for guessesTaken in range(1, 7):
    print("Take a guess.")
    guessedNumber = int(input('>'))
    if guessedNumber < secretNumber:
        print("Your guess is too low.")
    elif guessedNumber > secretNumber:
        print("Your guess is too high.")
    else:
        break
if guessedNumber == secretNumber:
    print("Good job! You guessed my number in " + str(guessesTaken) + " guesses!")
else:    
    print("Nope. The number I was thinking of was " + str(secretNumber))