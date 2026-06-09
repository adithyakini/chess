import streamlit as st
import chess

from streamlit_chessboard import chessboard

board = chess.Board()

move = chessboard(
    board.fen(),
    key="board"
)

st.write(move)
