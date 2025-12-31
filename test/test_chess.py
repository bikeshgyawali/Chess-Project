import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src/py'))

import unittest
from board import Board  # type: ignore


class TestChessGame(unittest.TestCase):

    def test_pawn_legal_move(self):
        """Test that a pawn can move forward one square from starting position."""
        board = Board()
        # White pawn at [1,4] moves to [2,4]
        success = board.move("Pawn", "White", [2, 4])
        self.assertTrue(success, "Pawn should move forward one square")
        self.assertEqual(board.grid[2][4].name, "Pawn")
        self.assertEqual(board.grid[1][4], 0)

    def test_rook_blocked_by_pawn(self):
        """Test that a rook cannot move through a pawn."""
        board = Board()
        # White rook at [0,0] tries to move to [2,0], blocked by pawn at [1,0]
        success = board.move("Rook", "White", [2, 0])
        self.assertFalse(success, "Rook should not move through blocking pawn")
        self.assertEqual(board.grid[0][0].name, "Rook")
        self.assertEqual(board.grid[2][0], 0)


if __name__ == "__main__":
    unittest.main()
