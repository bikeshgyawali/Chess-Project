import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src/py'))

import unittest
from board import Board  # type: ignore


class TestChessGame(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_pawn_legal_move(self):
        """Test that a pawn can move forward one square from starting position."""
        success = self.board.move("Pawn", "White", [2, 4])
        self.assertTrue(success, "Pawn should move forward one square")
        self.assertEqual(self.board.grid[2][4].name, "Pawn")
        self.assertEqual(self.board.grid[1][4], 0)

    def test_rook_blocked_by_pawn(self):
        """Test that a rook cannot move through a pawn."""
        success = self.board.move("Rook", "White", [2, 0])
        self.assertFalse(success, "Rook should not move through blocking pawn")
        self.assertEqual(self.board.grid[0][0].name, "Rook")
        self.assertEqual(self.board.grid[2][0], 0)

    def test_check(self):
        """Test that the king is in check."""
        # Set up a check scenario
        queen = self.board.grid[0][3]
        queen.position = [5, 4]
        self.board.grid[5][4] = queen  # Move White Queen to e6
        self.board.grid[0][3] = 0
        self.board.grid[6][4] = 0  # Remove blocking black pawn
        self.assertTrue(self.board.is_in_check("Black"), "Black king should be in check")

    def test_checkmate(self):
        """Test for a checkmate scenario (Fool's Mate)."""
        # Fool's Mate sequence
        self.board.move("Pawn", "White", [3, 5]) # f4
        self.board.move("Pawn", "Black", [4, 4]) # e5
        self.board.move("Pawn", "White", [3, 6]) # g4
        self.board.move("Queen", "Black", [3, 7]) # Qh4
        
        self.assertTrue(self.board.is_in_checkmate("White"), "White should be in checkmate")

if __name__ == "__main__":
    unittest.main()
