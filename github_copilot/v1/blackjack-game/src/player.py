class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def get_score(self):
        score = 0
        aces = 0
        for card in self.hand:
            if card.rank in ['J', 'Q', 'K']:
                score += 10
            elif card.rank == 'A':
                aces += 1
                score += 11
            else:
                score += card.rank
        
        while score > 21 and aces:
            score -= 10
            aces -= 1
        
        return score