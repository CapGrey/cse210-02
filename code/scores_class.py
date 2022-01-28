class Score:
    
    def __init__(self):


        self.guess = ""
        self.new_card = 0
        self.old_card = 0


    def determine_guess(self):
        """This function calls other functions to determine if
        the guess of the user is correct.
        Returns True if the guess si correct
        """

        def guess_is_higher(self):
            """Determines if the user's guess is greater than
            the value of the card.
            returns true if the new_card is greater than the old_card.
            """
            if self.new_card > self.old_card:
                return True
            
            else:
                return False

        def guess_is_lower(self):
            """Determines if the user's guess is less than
            the value of the card.
            returns true if the new_card is less than the old_card.
            """
            if self.new_card < self.old_card:
                return True
            
            else:
                return False
        
        def guess_is_equal_to(self):
            """Determines if the user's guess is equal to
            the value of the card.
            returns true if the new_card is equal to the old_card.
            """
            if self.new_card == self.old_card:
                return True

            else:
                return False

        
        # Determine if the guess is higher, lower, or equal to.
        # Determine if the guess is correct. 
        if self.guess.lower() == "higher":
            if guess_is_higher(self):
                return True
        
        elif self.guess.lower() == "lower":
            if guess_is_lower(self):
                return True
        
        elif self. guess.lower() == "equal to":
            if guess_is_equal_to(self):
                return True
        
        else:
            return False