import chess

def initialize_board():

    return chess.Board()


def make_move(board, move_uci):

    try:

        move = chess.Move.from_uci(move_uci)

        if move in board.legal_moves:

            board.push(move)

            return True

    except:
        pass

    return False
