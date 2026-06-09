import { useState } from "react";
import { Chessboard } from "react-chessboard";
import { Chess } from "chess.js";

function App() {

  const [game, setGame] = useState(
    () => new Chess()
  );

  const chessboardOptions = {

    position: game.fen(),

    onPieceDrop: (moveData) => {

      const gameCopy = new Chess(
        game.fen()
      );

      const move = gameCopy.move({
        from: moveData.sourceSquare,
        to: moveData.targetSquare,
        promotion: "q"
      });

      if (!move) {
        return false;
      }

      setGame(
        new Chess(
          gameCopy.fen()
        )
      );

      return true;
    }
  };

  return (
    <div
      style={{
        width: "700px",
        margin: "40px auto"
      }}
    >
      <h2>♟️ AI Chess Tutor</h2>

      <Chessboard
        options={chessboardOptions}
      />

    </div>
  );
}

export default App;