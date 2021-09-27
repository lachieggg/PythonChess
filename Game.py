import sys
import pygame
import os

from Player import Player
from Board import Board
from Window import Window

from pieces.Piece import Piece
from factories.PieceFactory import PieceFactory

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP
)

from Constants import *

class Game:
    def __init__(self, window, pieces, board):
        """Initializer for the Game"""
        # Window
        self.window = window
        self.window.render_pieces(pieces.values())
        # Pieces
        self.pieces = pieces
        # Board
        self.board = board
        # Players
        self.setup_players()

        self.square_selected = False
        # Main
        self.main()

    def move_piece(self):
        pass

    def handle_mouse_click(self):
        """Determines what to do when the user clicks the mouse"""
        if(self.square_selected):
            pass

        x, y = pygame.mouse.get_pos()
        dimensions = self.window.get_screen_dimensions()
        sq = self.window.get_square_from_pixels(x, y, *dimensions)

        if not sq:
            return

        self.select_square(sq[0], int(sq[1]))

    def main(self):
        """Main PyGame loop - renders game and registers user input"""
        running = True

        while running:
            self.window.render_pieces(list(self.pieces.values()))
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                elif event.type == QUIT:
                    running = False

                if event.type == MOUSEBUTTONDOWN:
                    self.handle_mouse_click()

            pygame.display.flip()

        pygame.quit()

    def setup_players(self, algorithms=None):
        """Creates the initial player objects"""
        self.user = Player(WHITE)
        self.computer = Player(BLACK)
        self.players = {'user': self.user, 'computer': self.computer}

    def select_square(self, char, num):
        """Select a square"""
        if not char or not num:
            return

        if self.square_selected:
            self.window.remove_prev_highlight(self.board, self.square_selected)
            if (self.square_selected.get('char') == char and self.square_selected.get('num') == num):
                # User selected
                # already selected square
                self.square_selected = False
                return
            else:
                # Old square selected
                _char = self.square_selected.get('char')
                _num = self.square_selected.get('num')

                piece = self.board.get_squares_piece(_char, _num)
                if piece:
                    print("Moving piece")
                    print(piece)
                    print("Square of moving piece: " + _char + str(_num))
                    print("Square moving piece to: " + char + str(num))
                    print("\n")
                    # Move piece
                    self.board.move_piece(piece, char, num, _char, _num)
                    self.window.render_square(char, num)
                    self.window.render_pieces(list(self.pieces.values()))


        self.square_selected = {'char': char, 'num': num}
        self.window.highlight_sq(char, num)
