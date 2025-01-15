import random

# import art

logo = r'''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
'''

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def blackjack():
    print(logo)
    ask_player = input("Do you want to play blackjack? type 'y' or 'n' ").lower()
    if 'y' in ask_player:
        print("\n" * 100)
        play_blackjack = True
    else:
        print("Goodbye!")
        play_blackjack = False
    
    player_hand = []
    computer_hand = []
    while play_blackjack:
        player_first_card = random.choice(cards)
        player_second_card = random.choice(cards)
        player_card_value = player_first_card + player_second_card
        player_hand.append(player_first_card)
        player_hand.append(player_second_card)
        print(f"Your Card is: {player_hand} current score: {player_card_value}")  # harusnya langsung di sini

        computer_current_card = random.choice(cards)
        computer_hand.append(computer_current_card)
        print(f"Computer's card: {computer_hand}")
        computer_current_card_value = computer_current_card

        while player_card_value <= 21:
            ask_player_if_hit_or_pass = input("Type 'y' to hit, 'n' to pass: ").lower()
            if 'y' in ask_player_if_hit_or_pass:
                player_hit_card = random.choice(cards)
                player_card_value += player_hit_card
                player_hand.append(player_hit_card)
                print("\n" * 100)
                print(f"Your Card is: {player_hand} current score: {player_card_value}")
                print(f"Computer's card: {computer_hand}")
            elif 'n' in ask_player_if_hit_or_pass:
                print("\n" * 100)
                computer_hit_card = random.choice(cards)
                computer_hit_value = computer_current_card_value + computer_hit_card
                computer_hand.append(computer_hit_card)
                while computer_hit_value <= 17:
                    plus_one = random.choice(cards)
                    computer_hit_value_hit_another = computer_hit_value + plus_one
                    computer_hand.append(plus_one)
                    computer_hit_value = computer_hit_value_hit_another
                if player_card_value > computer_hit_value and not player_card_value > 21 or computer_hit_value > 21:
                    print(f"Your Card is: {player_hand}, score: {player_card_value}")
                    print(f"Computer's card: {computer_hand}, score: {computer_hit_value} ")
                    print("You Win!")
                    blackjack()
                elif player_card_value < computer_hit_value and not computer_hit_value > 21:
                    print(f"Your Card is: {player_hand}, score: {player_card_value}")
                    print(f"Computer's card: {computer_hand}, score: {computer_hit_value} ")
                    print("You Lose")
                    blackjack()
                elif player_card_value == computer_hit_value:
                    print(f"Your Card is: {player_hand}, score: {player_card_value}")
                    print(f"Computer's card: {computer_hand}, score: {computer_hit_value} ")
                    print("It's a Draw!")
                    blackjack()
        else:
            print("Busted!")
            blackjack()
    
blackjack()