import sys
import pygame
import os

from players.Player import Player
from pieces.Piece import Piece
from Board import Board
from Window import Window
from factories.PieceFactory import PieceFactory

from Constants import *

from search.Tree import Tree
from search.Move import Move
from search.Node import Node

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP
)

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
        self.debug = False
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

        self.select_square(sq)

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
                    if(event.button == 1):
                        self.handle_mouse_click()
                    if(event.button == 3):
                        self.debug = not self.debug

                if(self.debug):
                    for player in self.players.values():
                        #print(player.get_possible_moves_for_player(self.board))
                        print("Greedy move for player {} is: ".format(player.colour))
                        print(player.get_greedy_move_for_player(self.board))
                        print(self.board.pieces)

            self.window.render_pieces(list(self.board.pieces.values()))
            pygame.display.flip()

        pygame.quit()

    def setup_players(self, algorithms=None):
        """Creates the initial player objects"""
        self.player = Player(PLAYER_COLOUR)
        self.computer = Player(COMPUTER_COLOUR)
        self.players = {'player': self.player, 'computer': self.computer}
        self.turn = self.player

    def select_square(self, sq):
        """Select a square"""
        if not sq:
            return
        
        if(VERBOSE): print(self.board.score('W'))

        if self.square_selected:
            if(VERBOSE): print("Square already selected.")
            self.window.remove_prev_highlight(self.square_selected)
            if (self.square_selected == sq):
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

                #_char = self.square_selected.get('char')
                #_num = self.square_selected.get('num')

                # Move piece
                #
                # Clear the square we are moving to
                self.window.render_square(sq)
                # Move the piece in the board
                moved = self.board.move_piece(self.square_selected, sq)
                if moved: self.turn = self.player if self.turn == self.computer else self.computer
                # Render the piece
                self.window.render_square(self.square_selected)
                self.square_selected = False
                return

        if(VERBOSE): print("Selecting square")
        if(VERBOSE): print("\n")
        self.square_selected = sq
        if(VERBOSE): print(char + str(num))
        self.window.highlight_sq(sq)