from utils import create_deck, shuffle_deck, deal_card

SUIT_SYMBOLS = {
    'Hearts': '♥',
    'Diamonds': '♦',
    'Clubs': '♣',
    'Spades': '♠'
}

def card_value(card):
    rank, _ = card
    if rank in ['Jack', 'Queen', 'King']:
        return 10
    elif rank == 'Ace':
        return 11
    else:
        return int(rank)

def hand_value(hand):
    value = sum(card_value(card) for card in hand)
    # Ajustar por ases
    aces = sum(1 for card in hand if card[0] == 'Ace')
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def format_card(card):
    rank, suit = card
    return f"{rank}{SUIT_SYMBOLS[suit]}"

def print_hand(name, hand, hide_first=False):
    if hide_first:
        visible = [format_card(card) for card in hand[1:]]
        print(f"{name}: [??] {visible}")
    else:
        formatted = [format_card(card) for card in hand]
        print(f"{name}: {formatted} (Valor: {hand_value(hand)})")

def main():
    deck = create_deck()
    shuffle_deck(deck)
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]

    print_hand("Crupier", dealer_hand, hide_first=True)
    print_hand("Jugador", player_hand)

    # Turno del jugador
    while True:
        if hand_value(player_hand) == 21:
            print("¡Blackjack! Ganaste.")
            return
        move = input("¿Quieres pedir carta (p) o plantarte (s)? ").lower()
        if move == 'p':
            player_hand.append(deal_card(deck))
            print_hand("Jugador", player_hand)
            if hand_value(player_hand) > 21:
                print("Te pasaste de 21. Pierdes.")
                return
        elif move == 's':
            break

    # Turno del crupier
    print_hand("Crupier", dealer_hand)
    while hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))
        print_hand("Crupier", dealer_hand)

    player_score = hand_value(player_hand)
    dealer_score = hand_value(dealer_hand)

    if dealer_score > 21 or player_score > dealer_score:
        print("¡Ganaste!")
    elif player_score < dealer_score:
        print("Perdiste.")
    else:
        print("Empate.")

if __name__ == "__main__":
    main()