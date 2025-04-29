from logic.api.entity.board import Board

class BoardFactory:
    
  def create_boards(self, board_count:int):
    boards = {i: Board(i) for i in range(1, (board_count + 1))}
    return boards