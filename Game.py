import sys
import pygame
import os

from players.Player import Player
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

from search.Tree import Tree
from search.Move import Move
from search.Node import Node

class Game:
    def __init__(self, window, board):
        """Initializer for the Game"""
        # Board
        self.board = board
        # Window
        self.window = window
        self.window.render_pieces(self.board.pieces.values())
        # Players
        self.setup_players()
        
        self.square_selected = False
        # Main
        self.main()
        # Search
        #self.node = Node()
        #self.tree = Tree()

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
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                elif event.type == QUIT:
                    running = False

                if event.type == MOUSEBUTTONDOWN:
                    self.handle_mouse_click()

                for player in self.players.values():
                    print(player.get_possible_moves_for_player(self.board))

            self.window.render_pieces(list(self.board.pieces.values()))
            pygame.display.flip()

        pygame.quit()

    def setup_players(self, algorithms=None):
        """Creates the initial player objects"""
        self.player = Player(PLAYER_COLOUR)
        self.computer = Player(COMPUTER_COLOUR)
        self.players = {'player': self.player, 'computer': self.computer}
        self.turn = self.player

    def select_square(self, char, num):
        """Select a square"""
        if not char or not num:
            return
        
        if(VERBOSE): print(self.board.score('W'))

        if self.square_selected:
            if(VERBOSE): print("Square already selected.")
            self.window.remove_prev_highlight(self.square_selected)
            if (self.square_selected.get('char') == char and self.square_selected.get('num') == num):
                # User selected
                # already selected square
                if(VERBOSE): print("Deselecting square")
                if(VERBOSE): print("\n")
                self.square_selected = False
                return
            else:
                # We are going to move a piece
                #
                # Save the piece's previous position
                _char = self.square_selected.get('char')
                _num = self.square_selected.get('num')

                # Move piece
                #
                # Clear the square we are moving to
                self.window.render_square(char, num)
                # Move the piece in the board
                moved = self.board.move_piece(self.player, self.turn, _char, _num, char, num)
                if moved: self.turn = self.player if self.turn == self.computer else self.computer
                # Render the piece
                self.window.render_square(_char, _num)
                self.square_selected = False
                return

        if(VERBOSE): print("Selecting square")
        if(VERBOSE): print("\n")
        self.square_selected = {'char': char, 'num': num}
        if(VERBOSE): print(char + str(num))
        self.window.highlight_sq(char, num)