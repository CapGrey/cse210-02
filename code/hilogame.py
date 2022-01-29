from scores_class import Score
from card_generator_class import Card_generator

class controler:

    def __init__(self):
        score = Score()
        card = Card_generator()
        card.create_card()
        self.gameplay_loop(True, card, score)

    def set_card(self, card, score):
        #sets up the cards, shifting the new card to the old and giving a new value to the new card.
        card.create_card()
        score.old_card = card.new_card
        score.new_card = card.top_card

    def display_start_info(self, card, score):
        #Displays info before the user guesses
        card.show_top_card()
        print(f"Your current score is: {score.score}")

    def check_guess(self, score):
        #Checks if the player's guess is correct and adjusts the score accordingly
        is_correct = score.determine_guess()
        score.update_score(is_correct)

    def user_guess(self, score):
        #Gets the user input for guess
        print("Guess if the next card will be higher or lower then the displayed card.")
        
        score.guess = input('Type "Higher" or "Lower" to make a guess. ').lower()
        #This will loop until a valid input is made.
        while score.guess != 'higher' and score.guess != 'lower':
            score.guess = input('Type "Higher" or "Lower" or make a guess. ').lower()
        
        self.check_guess(score)

    

    def display_end_info(self, card, score):
        #Displays info after a guess and before the player is asked if they want to continue
        card.show_bottom_card()
        print(f"Your score is now: {score.score}")

    def check_loop(self, score):
        #Controls if the game should continue to loop
        user_continue = ''
        
        if score.score <= 0:
           return False

        #This code should look until we get a bool to avoid any errors
        while type(user_continue) != bool:
            print("Would you like to continue?")
            user_continue = input("Yes/No: ").lower()
            if user_continue == "yes":
                return True
            elif user_continue == "no":
                print(f"Your final score is: {score.score}")
                return False




    def gameplay_loop(self, loop, card, score):
        #Loops the game until it is told to stop
        while loop:
            self.set_card(card, score)
            
            self.display_start_info(card, score)
            
            self.user_guess(score)

            self.display_end_info(card, score)

            loop = self.check_loop(score)






            
            

    


# This file is for the game itself
def main():

    director = controler()


    print("Thank you for playing.")

   

if __name__ == "__main__":
    main()