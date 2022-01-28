from card_generator_class import Card_generator
from scores_class import Score

def get_choice():
    choice = ["h","l"]
    user_input = ""
    while user_input not in choice:
        user_input = input("Higher or Lower? [h/l] ").lower()
        
    return user_input

def play_again():
    replay = ["y","n"]
    user_input = ""
    while user_input not in replay:
        user_input = input("Play again? [y/n] ").lower()

    return True if user_input == "y" else False

def run_game(score,card):
    card.create_card()
    card.show_card_first()
    choice = get_choice()
    card.create_card()
    card.show_card_second()
    if (choice == "l" and card.card1 < card.card2) or (choice == "h" and card.card1 > card.card2):
        score.update_score(True)
    else:
        score.update_score(False)

    print(f"Your score is: {score.score}")
    
    
# This file is for the game itself
def main():
    score = Score()
    card = Card_generator()
    replay = True
    
    while(replay):
        run_game(score,card)
        replay = play_again()
    
if __name__ == "__main__":
    main()