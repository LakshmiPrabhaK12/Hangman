import random
def print_design(guesses,word):
    if(guesses == 0):
        print("----------\n"
               "|     |\n"
               "|\n"
               "|\n"
               "|\n"
               "|\n"
               "|----------\n")
    elif(guesses == 1):
        print("----------\n"
               "|     |\n"
               "|     0\n"
               "|\n"
               "|\n"
               "|\n"
               "|----------\n")
    elif(guesses == 2):
        print("----------\n"
               "|     |\n"
               "|     0\n"
               "|     |\n"
               "|\n"
               "|\n"
               "|----------\n")
    elif(guesses == 3):
        print("----------\n"
               "|     |\n"
               "|     0\n"
               "|    /|\n"
               "|\n"
               "|\n"
               "|-----------\n")
    elif(guesses == 4):
        print("----------\n"
               "|     |\n"
               "|     0\n"
               "|    /|\ \n"
               "|\n"
               "|\n"
               "|----------\n")
    elif(guesses == 5):
        print("----------\n"
               "|     |\n"
               "|     0\n"
               "|    /|\ \n"
               "|     | \n"
               "|    /  \n"
               "|---------\n")
    elif(guesses == 6):
        print("----------\n"
               "|     |\n"
               "|     0\n"
               "|    /|\ \n"
               "|     | \n"
               "|    / \ \n"
               "|---------\n")
        print("\n")
        print("The word is %s.\n" % word)
        print("\n You lost! Try again ")
        print("Do you want to play again? if so,press 1 for yes and 2 for no")
        again = input("> ")
        again = again.lower()
        if again == "1" :
             hangman()
        return()
def randomword():
    words=["computer","laptop","windows","desktop"]
    myword = random.choice(words)
    myword = myword.lower()
    return myword
def hangman():
    guesses = 0
    word=randomword()
    wordlist = list(word)
    blanks = '_' * len(word)
    blanks_list = list(blanks)
    guess_list= []
    new_blanks_list = list(blanks)
    print("lets play Hangman!\n")
    print_design(guesses,word)
    print("\n"+''.join(blanks_list))
    print("GUESS A LETTER:")
    while guesses < 6:
        guess = input("> ")
        guess = guess.lower()
        if len(guess) > 1:
            print("Please enter one letter at a time!")
        elif guess == "":
            print("enter a letter ")
        elif guess in guess_list:
            print("Already guessed!Here is what you have guessed:")
            print(''.join(guess_list))
        else:
            guess_list.append(guess)
            i = 0
            while i<len(word):
                if guess == word[i]:
                    new_blanks_list[i] = wordlist[i]
                i=i+1
            if new_blanks_list == blanks_list:
                print("oops!your letter is in here")
                guesses = guesses+1
                print_design(guesses,word)
                
                if guesses<6:
                    print("Guess again")
                    print(''.join(blanks_list))
            elif wordlist!= blanks_list:
                blanks_list = new_blanks_list[:]
                print(''.join(blanks_list))
                
                if wordlist == blanks_list:
                    print("\n YOU WIN\n")
                    print("Do you want to play again? if so,press 1 for yes and 2 for no")
                    again=input("> ")
                    if again == "yes" :
                        hangman()
                    quit()
                    
                else:
                    print("Great guess!Guess the next")
hangman()
                    
