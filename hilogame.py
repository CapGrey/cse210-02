# This file is for the game itself
def main():
    pass
    user_continue = True
    user_guess = ''
    while user_continue:
        #print the card and current score here
        print("Guess if the next card will be higher or lower then the displayed card.")
        
        user_guess = input('Type "Higher" or "Lower" to make a guess. ').lower()
        #This will loop until a valid input is made.
        while user_guess != 'higher' and user_guess != 'lower':
            #print the card and current score here to make sure the user still sees after a few failed inputs.
            user_guess = input('Type "Higher" or "Lower" or make a guess. ').lower()
        #Pass user_guess to score


        user_continue = ''
        
        #Enable if no other classes are tracking 0 score. Check score before asking to continue.
        #if [score] >= 0:
        #   user_continue = False


        #This code should look until we get a bool to avoid any errors
        while type(user_continue) != bool:
            print("Would you like to continue?")
            user_continue = input("Yes/No: ").lower()
            if user_continue == "yes":
                user_continue = True
            elif user_continue == "no":
                user_continue = False



if __name__ == "__main__":
    main()