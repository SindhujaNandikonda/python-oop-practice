import random

def getUserOption():
    print("Lets play rock paper scissors! Type your choice: (r)ock, (p)aper, (s)cissors or (q)uit")
    userOption = input('>')
    return userOption

def getComputerOption():
    computerOption = random.choice(['r', 'p', 's'])
    return computerOption

computerOption = getComputerOption()
userOption = getUserOption()
wins = 0
losses = 0
ties = 0
while True:
    userOption = getUserOption()
    if userOption == 'q':
        break
    if userOption not in ['r', 'p', 's']:
        print("Invalid option. Please choose r, p, s or q.")
        continue
        
    computerOption = getComputerOption()
    if userOption == computerOption:
        print("It's a tie! Computer also chose " + computerOption)
        ties += 1
        #print("Lets play again! Type your choice: (r)ock, (p)aper, (s)cissors or (q)uit")
        
    elif (userOption == 'r' and computerOption == 's') or (userOption == 'p' and computerOption == 'r') or (userOption == 's' and computerOption == 'p'):
        print("You win! Computer chose " + computerOption)
        wins += 1
        #print("Lets play again! Type your choice: (r)ock, (p)aper, (s)cissors or (q)uit")
        
    else:
        print("You lose! Computer chose " + computerOption)
        losses += 1
        #print("Lets play again! Type your choice: (r)ock, (p)aper, (s)cissors or (q)uit")

print("Thanks for playing! Your final score is: " + str(wins) + " wins, " + str(losses) + " losses and " + str(ties) + " ties.")
print("computer's final score is: " + str(losses) + " wins, " + str(wins) + " losses and " + str(ties) + " ties.")
print("Goodbye!")