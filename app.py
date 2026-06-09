import streamlit as st
import chess
import chess.svg
import streamlit.components.v1 as components

from chess_engine.board import (
    initialize_board,
    make_move
)

from ai.coach import ask_coach
from ai.opponent import get_ai_move

# --------------------------------------------------
# Page Setup
# --------------------------------------------------

st.set_page_config(
    page_title="AI Chess Tutor",
    layout="wide"
)

# --------------------------------------------------
# Session State
# --------------------------------------------------

if "board" not in st.session_state:
    st.session_state.board = initialize_board()

if "moves" not in st.session_state:
    st.session_state.moves = []

if "chat" not in st.session_state:
    st.session_state.chat = []

# --------------------------------------------------
# Layout
# --------------------------------------------------

left, right = st.columns([3, 2])

# ==================================================
# LEFT PANEL - CHESS GAME
# ==================================================

with left:

    st.title("♟️ AI Chess Tutor")

    st.subheader("Current Position")
    #st.text(st.session_state.board)
    svg_board = chess.svg.board(
        st.session_state.board,
        size=500
    )
    
    components.html(
        svg_board,
        height=520
    )


    move = st.text_input(
        "Enter Move (UCI)",
        placeholder="e2e4"
    )

    if st.button("Play Move"):

        success = make_move(
            st.session_state.board,
            move
        )

        if success:

            # Save human move
            st.session_state.moves.append(
                f"Human: {move}"
            )

            # Check if game ended before AI moves
            if not st.session_state.board.is_game_over():

                try:

                    ai_move = get_ai_move(
                        st.session_state.board
                    )

                    if ai_move:

                        st.session_state.board.push(
                            ai_move
                        )

                        st.session_state.moves.append(
                            f"AI: {ai_move.uci()}"
                        )

                except Exception as e:

                    st.error(
                        f"AI move failed: {e}"
                    )

            st.rerun()

        else:

            st.error("Illegal Move")

    # ----------------------------------------------
    # Game Status
    # ----------------------------------------------

    st.subheader("Game Status")

    if st.session_state.board.is_checkmate():
        st.success("Checkmate!")

    elif st.session_state.board.is_stalemate():
        st.warning("Stalemate")

    elif st.session_state.board.is_insufficient_material():
        st.warning("Draw - Insufficient Material")

    elif st.session_state.board.is_check():
        st.warning("Check!")

    # ----------------------------------------------
    # Move History
    # ----------------------------------------------

    st.subheader("Move History")

    if len(st.session_state.moves) == 0:
        st.write("No moves yet.")

    for move_text in st.session_state.moves:
        st.write(move_text)

# ==================================================
# RIGHT PANEL - COACH
# ==================================================

with right:

    st.subheader("🧠 Chess Coach")

    question = st.text_input(
        "Ask your coach"
    )

    if st.button("Send"):

        if question.strip():

            try:

                answer = ask_coach(
                    st.session_state.board.fen(),
                    st.session_state.moves,
                    question
                )

                st.session_state.chat.append(
                    ("You", question)
                )

                st.session_state.chat.append(
                    ("Coach", answer)
                )

            except Exception as e:

                st.error(
                    f"Coach error: {e}"
                )

    # ----------------------------------------------
    # Chat History
    # ----------------------------------------------

    for speaker, message in st.session_state.chat:

        st.markdown(
            f"**{speaker}:** {message}"
        )

# ==================================================
# RESET BUTTON
# ==================================================

st.divider()

if st.button("🔄 New Game"):

    st.session_state.board = initialize_board()
    st.session_state.moves = []
    st.session_state.chat = []

    st.rerun()


#-------------------------
#DEBUG
#------------------------
if st.button("Test AI"):

    try:

        ai_move = get_ai_move(
            st.session_state.board
        )

        st.success(
            f"AI says {ai_move}"
        )

    except Exception as e:

        st.error(str(e))
