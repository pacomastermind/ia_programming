import random
import time

# Constants
SUITS = ['♥', '♦', '♣', '♠']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

# Function to create a deck of cards
def create_deck():
    return [(rank, suit) for suit in SUITS for rank in RANKS]

# Function to shuffle the deck
def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

# Function to deal a card from the deck
def deal_card(deck):
    return deck.pop()

# Function to calculate the value of a hand
def calculate_hand_value(hand):
    value = sum(VALUES[card[0]] for card in hand)
    # Adjust for Aces
    num_aces = sum(1 for card in hand if card[0] == 'A')
    while value > 21 and num_aces > 0:
        value -= 10  # Convert an Ace from 11 to 1
        num_aces -= 1
    return value

# Function to display a card
def display_card(card):
    rank, suit = card
    return f"{rank}{suit}"

# Function to display a hand
def display_hand(hand, hide_first=False):
    if hide_first and len(hand) > 0:
        return ["🂠"] + [display_card(card) for card in hand[1:]]
    else:
        return [display_card(card) for card in hand]

# Function to check if a hand is a blackjack
def is_blackjack(hand):
    return len(hand) == 2 and calculate_hand_value(hand) == 21

# Function to check if a hand is busted
def is_busted(hand):
    return calculate_hand_value(hand) > 21

# Function for dealer's turn
def dealer_play(hand, deck):
    while calculate_hand_value(hand) < 17:
        hand.append(deal_card(deck))
    return hand

# Function to determine the winner
def determine_winner(player_hand, dealer_hand):
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    
    if is_busted(player_hand):
        return "Dealer", "Player busted!"
    elif is_busted(dealer_hand):
        return "Player", "Dealer busted!"
    elif is_blackjack(player_hand) and not is_blackjack(dealer_hand):
        return "Player", "Blackjack!"
    elif is_blackjack(dealer_hand) and not is_blackjack(player_hand):
        return "Dealer", "Dealer has Blackjack!"
    elif player_value > dealer_value:
        return "Player", f"Player: {player_value}, Dealer: {dealer_value}"
    elif dealer_value > player_value:
        return "Dealer", f"Dealer: {dealer_value}, Player: {player_value}"
    else:
        return "Push", "It's a tie!"

# Main game function
def play_blackjack():
    print("\n===== WELCOME TO BLACKJACK =====\n")
    
    # Initialize game variables
    player_money = 1000
    min_bet = 10
    
    while player_money >= min_bet:
        # Create and shuffle deck
        deck = shuffle_deck(create_deck())
        
        # Place bet
        print(f"\nYou have ${player_money}")
        valid_bet = False
        bet = 0
        
        while not valid_bet:
            try:
                bet_input = input(f"Enter your bet (minimum ${min_bet}): ")
                bet = int(bet_input)
                if bet < min_bet:
                    print(f"Minimum bet is ${min_bet}")
                elif bet > player_money:
                    print(f"You only have ${player_money}")
                else:
                    valid_bet = True
            except ValueError:
                print("Please enter a valid number")
        
        # Deal initial cards
        player_hand = [deal_card(deck), deal_card(deck)]
        dealer_hand = [deal_card(deck), deal_card(deck)]
        
        # Display initial hands
        print("\nDealing cards...")
        time.sleep(1)
        print(f"Dealer's hand: {' '.join(display_hand(dealer_hand, hide_first=True))}")
        print(f"Your hand: {' '.join(display_hand(player_hand))} (Value: {calculate_hand_value(player_hand)})")
        
        # Check for blackjack
        if is_blackjack(player_hand) and is_blackjack(dealer_hand):
            print("\nBoth have Blackjack! Push!")
            winner, reason = "Push", "Both have Blackjack!"
        elif is_blackjack(player_hand):
            print("\nBLACKJACK! You win 3:2 on your bet!")
            player_money += int(bet * 1.5)
            winner, reason = "Player", "Blackjack!"
        elif is_blackjack(dealer_hand):
            print("\nDealer has Blackjack! You lose your bet.")
            player_money -= bet
            winner, reason = "Dealer", "Dealer has Blackjack!"
        else:
            # Player's turn
            player_turn = True
            while player_turn and not is_busted(player_hand):
                action = input("\nDo you want to (h)it or (s)tand? ").lower()
                
                if action == 'h':
                    player_hand.append(deal_card(deck))
                    print(f"You drew: {display_card(player_hand[-1])}")
                    print(f"Your hand: {' '.join(display_hand(player_hand))} (Value: {calculate_hand_value(player_hand)})")
                    
                    if is_busted(player_hand):
                        print("Busted! You lose your bet.")
                        player_money -= bet
                        player_turn = False
                        winner, reason = "Dealer", "Player busted!"
                elif action == 's':
                    player_turn = False
                else:
                    print("Invalid input. Please enter 'h' for hit or 's' for stand.")
            
            # Dealer's turn (only if player hasn't busted)
            if not is_busted(player_hand):
                print("\nDealer's turn...")
                print(f"Dealer's hand: {' '.join(display_hand(dealer_hand))} (Value: {calculate_hand_value(dealer_hand)})")
                time.sleep(1)
                
                dealer_hand = dealer_play(dealer_hand, deck)
                
                print(f"Dealer's final hand: {' '.join(display_hand(dealer_hand))} (Value: {calculate_hand_value(dealer_hand)})")
                
                # Determine winner
                winner, reason = determine_winner(player_hand, dealer_hand)
                
                if winner == "Player":
                    print(f"\nYou win! {reason}")
                    player_money += bet
                elif winner == "Dealer":
                    print(f"\nDealer wins. {reason}")
                    player_money -= bet
                else:  # Push
                    print(f"\nPush! {reason}")
        
        # Ask to play again
        if player_money < min_bet:
            print(f"\nYou don't have enough money to continue (minimum bet is ${min_bet}).")
            break
        
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break
    
    print(f"\nGame over! You leave with ${player_money}")
    print("Thanks for playing!")

# Start the game if this script is run directly
if __name__ == "__main__":
    play_blackjack()
