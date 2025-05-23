# from logic.machine_learning.game.game import Game


# from typing import Optional

# class GameStore:
#     def __init__(self):
#         self.games: dict[str, Game] = {}  # Dictionary to store multiple Game instances by game_id

#     def add_game(self, game_id: str) -> None:
#         """Adds a new game if it does not already exist."""
#         if game_id not in self.games:
#             self.games[game_id] = Game(game_id)

#     def get_game(self, game_id: str) -> Optional[Game]:
#         """Retrieves a game instance by ID."""
#         return self.games.get(game_id, None)
    
#     def reset_game(self, game_id: str):
#         game = self.get_game(game_id)
#         if game:
#             game.board.reset()  # Assuming your board has a reset method that resets it to the initial state
#             game.last_move = None
#             print(f"Game {game_id} has been reset.")