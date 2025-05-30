import random

# Card values
cards = {
    'A': 11, '2': 2, '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10
}

# Create a deck of cards
def create_deck():
    return list(cards.keys()) * 4

# Calculate the value of a hand
def calculate_hand_value(hand):
    value = sum(cards[card] for card in hand)
    aces = hand.count('A')
    while value > 21 and aces:
        value -= 10  # Convert an Ace from 11 to 1
        aces -= 1
    return value

# Display hands
def show_hands(player, dealer, hide_dealer=True):
    print("\nPlayer's Hand:", player, "| Value:", calculate_hand_value(player))
    if hide_dealer:
        print("Dealer's Hand: [?,", dealer[1], "]")
    else:
        print("Dealer's Hand:", dealer, "| Value:", calculate_hand_value(dealer))

# Main game logic
def play_blackjack():
    deck = create_deck()
    random.shuffle(deck)

    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    show_hands(player_hand, dealer_hand)

    # Player's turn
    while True:
        choice = input("Do you want to 'hit' or 'stand'? ").lower()
        if choice == 'hit':
            player_hand.append(deck.pop())
            show_hands(player_hand, dealer_hand)
            if calculate_hand_value(player_hand) > 21:
                print("You busted. Dealer wins.")
                return
        elif choice == 'stand':
            break
        else:
            print("Invalid option. Please choose 'hit' or 'stand'.")

    # Dealer's turn
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())

    show_hands(player_hand, dealer_hand, hide_dealer=False)

    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    # Determine the outcome
    if dealer_value > 21 or player_value > dealer_value:
        print("You win!")
    elif player_value < dealer_value:
        print("Dealer wins.")
    else:
        print("It's a tie.")

# Start the game
if __name__ == "__main__":
    play_blackjack()
