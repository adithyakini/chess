import streamlit as st
import chess
from ai.opponent import get_ai_move

from chess_engine.board import (
    initialize_board,
    make_move
)

from ai.coach import ask_coach


st.set_page_config(
    page_title="AI Chess Tutor",
    layout="wide"
)

if "board" not in st.session_state:
    st.session_state.board = initialize_board()

if "moves" not in st.session_state:
    st.session_state.moves = []

if "chat" not in st.session_state:
    st.session_state.chat = []

left,right = st.columns([3,2])

with left:

    st.title("AI Chess Tutor")

    st.text(st.session_state.board)

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

        # Store human move
        st.session_state.moves.append(
            f"Human: {move}"
        )

        # AI thinks
        ai_move = get_ai_move(
            st.session_state.board
        )

        if ai_move:

            st.session_state.board.push_uci(
                ai_move
            )

            st.session_state.moves.append(
                f"AI: {ai_move}"
            )

        st.success("Move Played")

    else:

        st.error("Illegal Move")

    st.subheader("Move History")

    for m in st.session_state.moves:
        st.write(m)

with right:

    st.subheader("Coach")

    question = st.text_input(
        "Ask your coach"
    )

    if st.button("Send"):

        answer = ask_coach(
            st.session_state.board.fen(),
            st.session_state.moves,
            question
        )

        st.session_state.chat.append(
            ("You",question)
        )

        st.session_state.chat.append(
            ("Coach",answer)
        )

    for speaker,msg in st.session_state.chat:

        st.markdown(
            f"**{speaker}:** {msg}"
        )
