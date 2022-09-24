#!/usr/bin/env python3

import sys
import pygame
import os

from Player import Player
from Window import Window
from Game import Game
from Board import Board

from pieces.Piece import Piece
from factories.PieceFactory import PieceFactory

class Controller:
    def __init__(self):
        # Pieces
        self.piece_factory = PieceFactory()
        self.pieces = self.piece_factory.get_pieces()
        # Board
        self.board = Board(self.pieces)
        # Window
        self.window = Window()
        # Game
        self.game = Game(self.window, self.board)
        # Run
        self.run()
    
    def run(self):
        """Run the main PyGame loop in the Game class"""
        try: self.game.main()
        except KeyboardInterrupt as e: print('\nExiting')

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
