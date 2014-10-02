
import random

print "Hello!  Welcome to our guessing game!"
name=raw_input("What is your name? ")
if name == "":
    name = "Jerkface"

print "%s, I am thinking of a number between 1 and 100.\nTry to guess the number I am thinking of." %name
 
gameno=random.randrange(1,101)
gamewins=0
scorecard=[]
guess_int=0
tries=0


while True: #change to count down from 10 tries
     
    if tries == 10 or guess_int == gameno:
        if guess_int == gameno:   
            gamewins=1
            scorecard.append((name, tries, gamewins))
            print "Great job %s you finished the game in %d tries. Awesome!" % (name, tries)
        elif tries == 10:
            scorecard.append((name, tries, gamewins))
            print "You have 0 tries left. Game over!"
            print "Tough luck %s try harder next time." % name

        newgame = raw_input("Would you like to play again? (Y/N): \n")
        
        if newgame in ["y","Y","yes","Yes","sure","ok","YES"]:
            gameno=random.randrange(1,101)
            tries=0
            continue
            
        elif newgame in ["N","NO","no","n","No","q"]:
            print "Bye %s let's play again soon!" % name 
            break
        else:
            print "Huh? Did you want to play again? (Y/N)"

    guess = raw_input("Guess the number I am thinking:")

    try:
        guess_int = int(guess)
        if guess_int > 100:
            tries+=1
            print "You fool! Your number is bigger than 100! Guess a number between 1-100"
            
        elif guess_int < 1:
            tries+=1
            print "Pitiful. Your number is lower than 1! Guess a number between 1-100"
            
        elif guess_int < gameno:
            tries+=1
            print "Your number is too low, try again"
            
        elif guess_int > gameno:
            tries+=1
            print "Your number is too high, try again"
            
            #4 cases: player wins, plays again, player loses, plays again, player wins or loses, doesn't play again


    except ValueError:
        print "Oops. Enter a number 1-100"
        tries+=1

    print "You have %d tries left. \n" % (10 - tries)

        #finally statement


