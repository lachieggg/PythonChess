import unittest
from Board import Board
from factories.PieceFactory import PieceFactory
from pieces.Pawn import Pawn
from pieces.Knight import Knight
from pieces.Rook import Rook
from pieces.Bishop import Bishop
from pieces.Queen import Queen
from pieces.King import King
from Constants import *

class TestMovement(unittest.TestCase):
    def setUp(self):
        self.factory = PieceFactory()
        # Clear factory pieces for isolated tests
        self.factory.pieces = {}

    def create_board(self, piece_data):
        """Helper to create a board with specific pieces"""
        self.factory.pieces = {}
        for ptype, colour, col, row in piece_data:
            self.factory.create_piece(ptype, colour, col, row)
        return Board(self.factory.get_pieces())

    def test_pawn_movement(self):
        # White Pawn at A2
        board = self.create_board([('P', 'W', 'A', 2)])
        pawn = board.get_squares_piece('A', 2)
        
        # Legal
        self.assertTrue(pawn.moveable(board, 'A3'))
        self.assertTrue(pawn.moveable(board, 'A4'))
        
        # Illegal: Distance
        self.assertFalse(pawn.moveable(board, 'A5'), "Pawn moved 3 squares")
        # Illegal: Teleport/Distance
        self.assertFalse(pawn.moveable(board, 'A7'), "Pawn teleported to A7")
        # Illegal: Horizontal without capture
        self.assertFalse(pawn.moveable(board, 'B3'), "Pawn moved horizontally without victim")
        # Illegal: Backward
        self.assertFalse(pawn.moveable(board, 'A1'), "Pawn moved backward")

    def test_pawn_capture(self):
        # White Pawn at C4, Black Pawn at D5 and E5
        board = self.create_board([
            ('P', 'W', 'C', 4),
            ('P', 'B', 'D', 5),
            ('P', 'B', 'E', 5)
        ])
        pawn = board.get_squares_piece('C', 4)
        
        # Legal Capture
        self.assertTrue(pawn.moveable(board, 'D5'), "Pawn should capture diagonal D5")
        # Illegal Capture: Range
        self.assertFalse(pawn.moveable(board, 'E5'), "Pawn should NOT capture E5 (too far)")

    def test_knight_movement(self):
        # White Knight at D4
        board = self.create_board([('H', 'W', 'D', 4)])
        knight = board.get_squares_piece('D', 4)
        
        # Legal Knight moves
        legal_moves = ['C2', 'E2', 'B3', 'F3', 'B5', 'F5', 'C6', 'E6']
        for move in legal_moves:
            self.assertTrue(knight.moveable(board, move), f"Knight should move to {move}")
            
        # Illegal moves
        illegal_moves = ['D5', 'E4', 'D7', 'A4', 'H8']
        for move in illegal_moves:
            self.assertFalse(knight.moveable(board, move), f"Knight should NOT move to {move}")

    def test_rook_collision(self):
        # White Rook at A1, White Piece at A3
        board = self.create_board([
            ('R', 'W', 'A', 1),
            ('P', 'W', 'A', 3)
        ])
        rook = board.get_squares_piece('A', 1)
        
        # Legal
        self.assertTrue(rook.moveable(board, 'A2'))
        # Illegal: Blocked
        self.assertFalse(rook.moveable(board, 'A4'), "Rook jumped over A3")
        self.assertFalse(rook.moveable(board, 'A3'), "Rook tried to take own piece")

    def test_bishop_collision(self):
        # White Bishop at C1, White Piece at E3
        board = self.create_board([
            ('B', 'W', 'C', 1),
            ('P', 'W', 'E', 3)
        ])
        bishop = board.get_squares_piece('C', 1)
        
        # Legal
        self.assertTrue(bishop.moveable(board, 'D2'))
        # Illegal: Blocked
        self.assertFalse(bishop.moveable(board, 'F4'), "Bishop jumped over E3")

    def test_queen_teleport(self):
        # White Queen at D1, pieces at B1, C1
        board = self.create_board([
            ('Q', 'W', 'D', 1),
            ('P', 'W', 'C', 1),
            ('P', 'W', 'B', 1)
        ])
        queen = board.get_squares_piece('D', 1)
        
        # Illegal: Blocked Horizontally
        self.assertFalse(queen.moveable(board, 'A1'), "Queen jumped over B1/C1")
        
        # Blocked Vertically
        self.factory.create_piece('P', 'W', 'D', 3)
        board = Board(self.factory.get_pieces())
        queen = board.get_squares_piece('D', 1)
        self.assertFalse(queen.moveable(board, 'D8'), f"Queen at D1 cannot move to D8 if D3 is blocked")
        self.assertFalse(queen.moveable(board, 'D4'), "Queen jumped over D3")

    def test_king_range(self):
        # White King at E1
        board = self.create_board([('K', 'W', 'E', 1)])
        king = board.get_squares_piece('E', 1)
        
        # Legal
        self.assertTrue(king.moveable(board, 'D1'))
        self.assertTrue(king.moveable(board, 'E2'))
        self.assertTrue(king.moveable(board, 'F2'))
        
        # Illegal: Range
        self.assertFalse(king.moveable(board, 'E3'), "King moved 2 squares")
        self.assertFalse(king.moveable(board, 'G1'), "King moved 2 squares (castling not implemented yet/specifically tested as illegal range here)")

    # ===== NEW EDGE CASE TESTS =====

    def test_pawn_already_moved(self):
        """Test that pawn can only move 1 square after first move"""
        board = self.create_board([('P', 'W', 'A', 2)])
        pawn = board.get_squares_piece('A', 2)
        
        # Simulate pawn has moved
        pawn.moved = True
        
        # Legal: 1 square
        self.assertTrue(pawn.moveable(board, 'A3'))
        # Illegal: 2 squares after already moved
        self.assertFalse(pawn.moveable(board, 'A4'), "Pawn moved 2 squares after first move")

    def test_black_pawn_movement(self):
        """Test black pawn moves downward (decreasing row numbers)"""
        board = self.create_board([('P', 'B', 'D', 7)])
        pawn = board.get_squares_piece('D', 7)
        
        # Legal: Move down
        self.assertTrue(pawn.moveable(board, 'D6'))
        self.assertTrue(pawn.moveable(board, 'D5'))
        
        # Illegal: Move up
        self.assertFalse(pawn.moveable(board, 'D8'), "Black pawn moved up")
        
        # Illegal: Sideways
        self.assertFalse(pawn.moveable(board, 'E6'), "Black pawn moved diagonally without capture")

    def test_pawn_edge_of_board(self):
        """Test pawn at edge files can't capture off-board"""
        board = self.create_board([
            ('P', 'W', 'A', 2),
            ('P', 'B', 'B', 3)
        ])
        pawn = board.get_squares_piece('A', 2)
        
        # Legal: Capture right
        self.assertTrue(pawn.moveable(board, 'B3'))
        
        # Note: Can't test left capture as A-file has no left side
        # This would require checking bounds in the piece logic

    def test_pawn_blocked_forward(self):
        """Test pawn cannot move forward if blocked"""
        board = self.create_board([
            ('P', 'W', 'E', 2),
            ('P', 'B', 'E', 3)
        ])
        pawn = board.get_squares_piece('E', 2)
        
        # Illegal: Blocked by enemy piece directly ahead
        self.assertFalse(pawn.moveable(board, 'E3'), "Pawn moved through enemy piece")
        self.assertFalse(pawn.moveable(board, 'E4'), "Pawn jumped over enemy piece")

    def test_knight_at_board_edge(self):
        """Test knight movement from corner/edge positions"""
        board = self.create_board([('H', 'W', 'A', 1)])
        knight = board.get_squares_piece('A', 1)
        
        # Legal moves from A1
        self.assertTrue(knight.moveable(board, 'B3'))
        self.assertTrue(knight.moveable(board, 'C2'))
        
        # Illegal: Off-board or invalid L-shape
        self.assertFalse(knight.moveable(board, 'A2'), "Not an L-shape")
        self.assertFalse(knight.moveable(board, 'B1'), "Not an L-shape")

    def test_knight_blocked_by_own_piece(self):
        """Test knight cannot land on square occupied by own piece"""
        board = self.create_board([
            ('H', 'W', 'D', 4),
            ('P', 'W', 'E', 6)
        ])
        knight = board.get_squares_piece('D', 4)
        
        # Illegal: Own piece at destination
        self.assertFalse(knight.moveable(board, 'E6'), "Knight captured own piece")
        
        # Legal: Other moves still work
        self.assertTrue(knight.moveable(board, 'C6'))

    def test_knight_can_capture_enemy(self):
        """Test knight can capture enemy pieces"""
        board = self.create_board([
            ('H', 'W', 'D', 4),
            ('P', 'B', 'E', 6)
        ])
        knight = board.get_squares_piece('D', 4)
        
        # Legal: Capture enemy piece
        self.assertTrue(knight.moveable(board, 'E6'), "Knight should capture enemy")

    def test_rook_can_capture_enemy(self):
        """Test rook can capture enemy pieces"""
        board = self.create_board([
            ('R', 'W', 'A', 1),
            ('P', 'B', 'A', 5)
        ])
        rook = board.get_squares_piece('A', 1)
        
        # Legal: Capture enemy
        self.assertTrue(rook.moveable(board, 'A5'), "Rook should capture enemy")
        
        # Illegal: Jump over enemy
        self.assertFalse(rook.moveable(board, 'A6'), "Rook jumped over enemy")

    def test_bishop_can_capture_enemy(self):
        """Test bishop can capture enemy pieces"""
        board = self.create_board([
            ('B', 'W', 'C', 1),
            ('P', 'B', 'F', 4)
        ])
        bishop = board.get_squares_piece('C', 1)
        
        # Legal: Capture enemy
        self.assertTrue(bishop.moveable(board, 'F4'), "Bishop should capture enemy")
        
        # Illegal: Jump over enemy
        self.assertFalse(bishop.moveable(board, 'G5'), "Bishop jumped over enemy")

    def test_queen_diagonal_vs_straight(self):
        """Test queen can move both diagonally and straight"""
        board = self.create_board([('Q', 'W', 'D', 4)])
        queen = board.get_squares_piece('D', 4)
        
        # Legal: Straight moves
        self.assertTrue(queen.moveable(board, 'D8'))
        self.assertTrue(queen.moveable(board, 'A4'))
        
        # Legal: Diagonal moves
        self.assertTrue(queen.moveable(board, 'A1'))
        self.assertTrue(queen.moveable(board, 'H8'))
        
        # Illegal: Knight move
        self.assertFalse(queen.moveable(board, 'E6'), "Queen moved like knight")

    def test_piece_same_square(self):
        """Test pieces cannot move to their current square"""
        board = self.create_board([('R', 'W', 'A', 1)])
        rook = board.get_squares_piece('A', 1)
        
        # Illegal: Same position
        self.assertFalse(rook.moveable(board, 'A1'), "Rook 'moved' to same square")

    def test_king_capture_enemy(self):
        """Test king can capture enemy pieces"""
        board = self.create_board([
            ('K', 'W', 'E', 1),
            ('P', 'B', 'E', 2)
        ])
        king = board.get_squares_piece('E', 1)
        
        # Legal: Capture enemy
        self.assertTrue(king.moveable(board, 'E2'), "King should capture enemy")

    def test_king_blocked_by_own_piece(self):
        """Test king cannot capture own pieces"""
        board = self.create_board([
            ('K', 'W', 'E', 1),
            ('P', 'W', 'E', 2)
        ])
        king = board.get_squares_piece('E', 1)
        
        # Illegal: Own piece
        self.assertFalse(king.moveable(board, 'E2'), "King captured own piece")

    def test_rook_horizontal_and_vertical(self):
        """Test rook can only move horizontally or vertically"""
        board = self.create_board([('R', 'W', 'D', 4)])
        rook = board.get_squares_piece('D', 4)
        
        # Legal: Horizontal
        self.assertTrue(rook.moveable(board, 'A4'))
        self.assertTrue(rook.moveable(board, 'H4'))
        
        # Legal: Vertical
        self.assertTrue(rook.moveable(board, 'D1'))
        self.assertTrue(rook.moveable(board, 'D8'))
        
        # Illegal: Diagonal
        self.assertFalse(rook.moveable(board, 'E5'), "Rook moved diagonally")
        self.assertFalse(rook.moveable(board, 'A1'), "Rook moved diagonally")

    def test_bishop_only_diagonal(self):
        """Test bishop can only move diagonally"""
        board = self.create_board([('B', 'W', 'D', 4)])
        bishop = board.get_squares_piece('D', 4)
        
        # Legal: Diagonal
        self.assertTrue(bishop.moveable(board, 'A1'))
        self.assertTrue(bishop.moveable(board, 'G7'))
        
        # Illegal: Straight
        self.assertFalse(bishop.moveable(board, 'D8'), "Bishop moved vertically")
        self.assertFalse(bishop.moveable(board, 'A4'), "Bishop moved horizontally")

    def test_multiple_pieces_interaction(self):
        """Test complex scenario with multiple pieces blocking paths"""
        board = self.create_board([
            ('Q', 'W', 'D', 4),
            ('P', 'W', 'D', 6),
            ('P', 'B', 'F', 4),
            ('H', 'W', 'E', 5)
        ])
        queen = board.get_squares_piece('D', 4)
        
        # Legal: Can capture enemy
        self.assertTrue(queen.moveable(board, 'F4'))
        
        # Illegal: Blocked by own pawn
        self.assertFalse(queen.moveable(board, 'D7'), "Queen jumped over own pawn")
        
        # Illegal: Can't jump to occupied square (own piece)
        self.assertFalse(queen.moveable(board, 'D6'), "Queen captured own piece")

if __name__ == '__main__':
    unittest.main()