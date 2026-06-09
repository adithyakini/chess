import chess.engine

engine = chess.engine.SimpleEngine.popen_uci(
    "stockfish"
)

def get_ai_move(board):

    result = engine.play(
        board,
        chess.engine.Limit(time=0.1)
    )

    return result.move
