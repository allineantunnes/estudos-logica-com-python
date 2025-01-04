class Card:
    def __init__(self, name, card_type, attack):
        self.name = name
        self.card_type = card_type
        self.attack = attack

    def display_info(self):
        return f'Nome: {self.name}, Tipo: {self.card_type}, Ataque: {self.attack}'