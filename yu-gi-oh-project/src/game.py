class Game:
    def __init__(self):
        self.players = []
        self.current_turn = 0

    def add_player(self, player):
        self.players.append(player)

    def next_turn(self):
        self.current_turn = (self.current_turn + 1) % len(self.players)

    def check_victory(self):
        for player in self.players:
            if player.life_points <= 0:
                return f"{player.name} foi derrotado!"
        return None

    def start_game(self):
        while True:
            current_player = self.players[self.current_turn]
            print(f"É a vez de {current_player.name}.")
            # Lógica do turno do jogador
            victory_message = self.check_victory()
            if victory_message:
                print(victory_message)
                break
            self.next_turn()