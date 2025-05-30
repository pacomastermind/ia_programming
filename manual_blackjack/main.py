import random
import time

deck = []
deck_player = []
deck_crupier = []
symbols = ['♠','♥','◆','♣']
numbers = list(range(1, 11))
figures = ['J','Q','K']
numbers.extend(figures)


def suffle_deck():
    for symbol in symbols:
        for number in numbers:
            deck.append([number,symbol])
    random.shuffle(deck)

def hit_card(is_player):
    card = deck.pop(0)
    if is_player:
        deck_player.append(card)
    else:
        deck_crupier.append(card)

def deal_cards():
    for i in range(2):
        hit_card(True)
        hit_card(False)

def turn(is_player=True):
    print("Croupier cards --> ",end=' ')
    if is_player:
        print(deck_crupier[0])
    else:
        print(deck_crupier)
        print(f"Crupier points --> {points_deck(deck_crupier)}")
    print("Player cards --> ",end=' ')
    print(deck_player)
    print(f"Player points --> {points_deck(deck_player)}")

def points_deck(deck):
    total_points = 0
    point_in_card = 0
    number_ones = 0
    #Sum all points in deck
    for card in deck:
        if card[0] in figures:
            point_in_card = 10
        elif card[0] > 1:
            point_in_card = card[0]
        else:
            point_in_card = 11
            number_ones =+ 1
        total_points += point_in_card
    #Check for number ones
    while number_ones > 0 and total_points > 21:
        total_points -= 10
        number_ones -= 1
    #Return number points
    return total_points


# Main program
if __name__=="__main__":
    suffle_deck()
    deal_cards()
    print("------ PLAYER TURN ------")
    while True:
        turn()
        if points_deck(deck_player) > 21:
            print("------ PLAYER LOSES ------")
            exit()
        choice = input("HIT/STAND [H/S]").upper()
        while choice != "H" and choice != "S":
            choice = input("HIT/STAND [H/S]").upper()
        if choice == "S":
            break
        hit_card(True)

    print("------ CRUPIER TURN ------")
    while True:
        turn(False)
        if points_deck(deck_crupier) > 21:
            print("------ CRUPIER LOSES ------")
            exit()
        elif points_deck(deck_crupier) > 17:
            break
        hit_card(False)
    
    print("------ WINNER ------")
    if points_deck(deck_crupier) > points_deck(deck_player):
        print("------ CRUPIER WIN ------")
    else:
        print("------ PLAYER WIN ------")