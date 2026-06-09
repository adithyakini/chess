import chess.engine
import streamlit as st

@st.cache_resource
def get_engine():
    return chess.engine.SimpleEngine.popen_uci(
        "stockfish"
    )

def get_ai_move(board):

    engine = get_engine()

    result = engine.play(
        board,
        chess.engine.Limit(time=0.1)
    )

    return result.move
