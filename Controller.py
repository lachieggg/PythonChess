#!/usr/bin/env python3

import sys
import pygame
import os

from Player import Player
from Board import Board
from Window import Window

from pieces.Piece import Piece
from PieceFactory import PieceFactory

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP
)

class Controller:
    def __init__(self):
        """Initialize the controller"""
        # Piece Factory
        self.piece_factory = PieceFactory()
        pieces = self.piece_factory.get_pieces()
        # Board
        self.board = Board(pieces)
        # Window
        self.window = Window()
        self.window.render_pieces(self.board)
        # Players
        self.setup_players()
        # Main
        self.selected_sq = False
        self.main()


    def setup_players(self, algorithms=None):
        self.players = {'B': Player('B'), 'W': Player('W')}

    def main(self):
        """Main Pygame loop"""
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                elif event.type == QUIT:
                    running = False

                if event.type == MOUSEBUTTONDOWN:
                    if(self.selected_sq):
                        pass
                    x, y = pygame.mouse.get_pos()
                    sq = self.board.get_square_from_pixels(x, y, *self.window.get_screen_dimensions())
                    if not sq:
                        continue

                    self.select_square(sq[0], int(sq[1]))

            pygame.display.flip()

        pygame.quit()

    def select_square(self, char, num):
        """Select a square"""
        if not char or not num:
            return

        if self.selected_sq:
            self.window.remove_prev_highlight(self.board, self.selected_sq)
            if (self.selected_sq.get('char') == char and self.selected_sq.get('num') == num):
                # User selected an already selected square
                self.selected_sq = False
                return
            #if self.board.pieces

        self.selected_sq = {'char': char, 'num': num}
        self.window.highlight_sq(self.board, char, num)


def add_to_sys_path():
    """Add root folder to the path allowing imports from subdirectories"""
    sys.path.append(os.path.abspath('../'))

def main():
    """Main function which creates the controller object"""
    # Sys
    add_to_sys_path()
    # Main
    controller = Controller()

if __name__ == "__main__":
    main()
