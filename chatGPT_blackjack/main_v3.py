import random

# Card values (only rank values)
card_values = {
    'A': 11, '2': 2, '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10
}

# Suits with symbols
suits = ['♠', '♥', '♦', '♣']

# Create a full deck with suits
def create_deck():
    return [f"{rank}{suit}" for rank in card_values for suit in suits]

# Extract rank from a card like "A♠" or "10♦"
def get_rank(card):
    return card[:-1]

# Calculate the value of a hand
def calculate_hand_value(hand):
    value = 0
    aces = 0
    for card in hand:
        rank = get_rank(card)
        value += card_values[rank]
        if rank == 'A':
            aces += 1
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

# Display both hands
def show_hands(player_hand, dealer_hand, hide_dealer=True):
    print("\nPlayer's Hand:", '  '.join(player_hand), "| Value:", calculate_hand_value(player_hand))
    if hide_dealer:
        print("Dealer's Hand: [??]", dealer_hand[1])
    else:
        print("Dealer's Hand:", '  '.join(dealer_hand), "| Value:", calculate_hand_value(dealer_hand))

# Main game logic
def play_blackjack():
    deck = create_deck()
    random.shuffle(deck)

    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    show_hands(player_hand, dealer_hand)

    # Player's turn
    while True:
        choice = input("\nDo you want to 'hit' or 'stand'? ").lower()
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

    # Determine the result
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    if dealer_value > 21 or player_value > dealer_value:
        print("You win!")
    elif player_value < dealer_value:
        print("Dealer wins.")
    else:
        print("It's a tie.")

# Start the game
if __name__ == "__main__":
    play_blackjack()
