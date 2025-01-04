# Conteúdo do arquivo: /yu-gi-oh-project/yu-gi-oh-project/src/main.py

class Card:
    def __init__(self, name, card_type, attack):
        self.name = name
        self.card_type = card_type
        self.attack = attack

    def display_info(self):
        return f'Nome: {self.name}, Tipo: {self.card_type}, Ataque: {self.attack}'


class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def shuffle_deck(self):
        import random
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop() if self.cards else None


class Game:
    def __init__(self):
        self.deck = Deck()
        self.players = []

    def add_player(self, player_name):
        self.players.append(player_name)

    def start_game(self):
        print("O jogo começou!")
        self.deck.shuffle_deck()
        for player in self.players:
            drawn_card = self.deck.draw_card()
            print(f'{player} comprou a carta: {drawn_card.display_info() if drawn_card else "Nenhuma carta disponível."}')


if __name__ == "__main__":
    game = Game()
    game.add_player("Jogador 1")
    game.add_player("Jogador 2")

    # Adicionando algumas cartas ao baralho
    game.deck.add_card(Card("Dragão Branco de Olhos Azuis", "Dragão", 3000))
    game.deck.add_card(Card("Mago do Feitiço", "Mago", 2500))
    game.deck.add_card(Card("Guerreiro", "Guerreiro", 1500))

    game.start_game()