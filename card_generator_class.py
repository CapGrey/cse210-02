import random

class Card_generator:

    def __init__(self, card1 = 0, card2 = 0):
        self.card1 = card1
        self.card2 = card2
        
    def create_card(self):
        self.card2 = self.card1
        self.card1 = random.randint(1,13)
        
    def show_card_first(self):
        print(f"The card is: {self.card1}")
        
    def show_card_second(self):
        print(f"Next card is: {self.card1}")