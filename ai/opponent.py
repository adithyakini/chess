import chess.engine

ENGINE_PATH = "./stockfish/stockfish-ubuntu-x86-64"

engine = chess.engine.SimpleEngine.popen_uci(
    ENGINE_PATH
)

def get_ai_move(board):

    result = engine.play(
        board,
        chess.engine.Limit(time=0.1)
    )

    return result.move
