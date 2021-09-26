#!/usr/bin/env python3

import sys
import pygame
import os

from Player import Player
from Board import Board
from Window import Window
from Game import Game

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
        game = Game()

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
