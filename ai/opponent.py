from stockfish import Stockfish

stockfish = Stockfish(
    path="stockfish.exe"
)

stockfish.set_skill_level(5)

def get_ai_move(board):

    stockfish.set_fen_position(
        board.fen()
    )

    return stockfish.get_best_move()
