def shuffle_deck(deck):
    import random
    random.shuffle(deck)

def deal_card(deck):
    return deck.pop() if deck else None

def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    return deck