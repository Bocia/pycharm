import random

class BriscolaEnvironment:
    def __init__(self):
        self.deck = self.initialize_deck()
        self.shuffle_deck()
        self.players = ['Player', 'Computer']
        self.hands = {player: [] for player in self.players}
        self.trump_suit = None
        self.current_player = None
        self.tricks = {player: [] for player in self.players}
        self.scores = {player: 0 for player in self.players}

    def initialize_deck(self):
        suits = ['Coppe', 'Bastoni', 'Spade', 'Denari']
        ranks = ['Asso', 'Due', 'Tre', 'Quattro', 'Cinque', 'Sei', 'Sette', 'Fante', 'Cavallo', 'Re']
        deck = [{'suit': suit, 'rank': rank, 'label': f"{rank} di {suit}"} for suit in suits for rank in ranks]
        return deck

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deal_cards(self):
        for _ in range(3):
            for player in self.players:
                card = self.deck.pop()
                self.hands[player].append(card)

    def determine_trump_suit(self):
        self.trump_suit = self.deck[-1]['suit']

    def play_round(self):
        self.current_player = 'Player'
        self.deal_cards()
        self.determine_trump_suit()

        while self.hands['Player'] and self.hands['Computer']:
            self.play_turn('Player')
            self.play_turn('Computer')

        self.calculate_scores()

    def play_turn(self, player):
        if player == 'Player':
            self.display_game_state()

        card = self.choose_card(player)
        self.hands[player].remove(card)
        self.tricks[player].append(card)

    def choose_card(self, player):
        if player == 'Player':
            print(f"\n{player}'s Hand: {[card['label'] for card in self.hands[player]]}")
            selected_index = int(input("Select the index of the card to play: "))
            return self.hands[player][selected_index]
        elif player == 'Computer':
            # Apply the computer player's strategy here
            card = self.computer_strategy(player)
            print(f"\n{player} plays: {card['label']}")
            return card

    def computer_strategy(self, player):
        # Simplified strategy: Computer plays a random card
        return random.choice(self.hands[player])

    def calculate_scores(self):
        for player in self.players:
            # Simplified scoring: 1 point per trick
            self.scores[player] += len(self.tricks[player])

    def display_game_state(self):
        print("\nCurrent Game State:")
        print(f"Briscola: {self.trump_suit}")
        print(f"Player's Hand: {[card['label'] for card in self.hands['Player']]}")
        print(f"Computer's Hand: {[card['label'] for card in self.hands['Computer']]}")
        print(f"Player's Tricks: {[card['label'] for card in self.tricks['Player']]}")
        print(f"Computer's Tricks: {[card['label'] for card in self.tricks['Computer']]}")
        print(f"Scores: Player - {self.scores['Player']}, Computer - {self.scores['Computer']}")

# Example usage
if __name__ == "__main__":
    briscola_game = BriscolaEnvironment()
    briscola_game.play_round()
