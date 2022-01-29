import random

class Card_generator:

    def __init__(self, top_card = 0, new_card = 0):
        self.top_card = top_card
        self.new_card = new_card

    def create_card(self):
        self.new_card = self.top_card
        self.top_card = random.randint(1,13)

    def show_top_card(self):
        print(f"The card is: {self.new_card}")

    def show_bottom_card(self):
        print(f"Next card was: {self.top_card}")
         