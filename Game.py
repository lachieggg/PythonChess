import sys
import pygame
import os
import time
import copy

from Player import Player
from pieces.Piece import Piece
from Board import Board
from Window import Window
from factories.PieceFactory import PieceFactory

from Constants import *
from typing import Optional

from search.MinimaxSearch import MinimaxSearch

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP
)

class Game:
    # Type hints for attributes created in setup_players()
    player: Optional['Player']
    computer: Optional['Player']
    players: dict
    turn: Optional['Player']
    
    def __init__(self, window, board, ai_mode=False):
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
        self.ai_mode = ai_mode
        self.last_move = None
        self.paused = False
        self.clock = pygame.time.Clock()
        # Animation state
        self.anim_piece = None
        self.anim_start_pix = None
        self.anim_end_pix = None
        self.anim_end_pix = None
        self.anim_progress = 0
        self.history = []

    def handle_mouse_click(self):
        """Determines what to do when the user clicks the mouse"""
        x, y = pygame.mouse.get_pos()
        
        # Check for quit button click
        if self.window.is_quit_clicked((x, y)):
            pygame.quit()
            sys.exit()
            
        # Check for pause button click
        if self.window.is_pause_clicked((x, y)):
            self.paused = not self.paused
            return

        if self.paused:
            return

        dimensions = self.window.get_screen_dimensions()
        sq = self.window.get_square_from_pixels(x, y, *dimensions)

        if not sq:
            return

        self.select_square(sq)

    def process_events(self, events):
        """Unified event handling for clicks and keyboard"""
        for event in events:
            if event.type == QUIT:
                return False
            
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return False
            
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                # Check for quit button click
                if self.window.is_quit_clicked((x, y)):
                    pygame.quit()
                    sys.exit()
                    
                # Check for pause button click
                if self.window.is_pause_clicked((x, y)):
                    self.paused = not self.paused
                    return True

                # Check for undo button click
                if self.window.is_undo_clicked((x, y)):
                    self.undo_move()
                    return True
                
                # Check for reset button click
                if self.window.is_reset_clicked((x, y)):
                    self.reset_game()
                    return True

                if self.paused:
                    return True

                # Process square selection
                dimensions = self.window.get_screen_dimensions()
                sq = self.window.get_square_from_pixels(x, y, *dimensions)
                if sq:
                    self.select_square(sq)
                    
            if event.type == MOUSEBUTTONDOWN and event.button == 3:
                # Right click debug
                self.debug = not self.debug
                for player in self.players.values():
                    print(player.get_possible_moves_for_player(self.board))
                    print("Minimax move for player {} is: ".format(player.colour))
                    print(player.get_minimax_best_move_for_player(self.board, self.window))
                    print("\n")
                    
        return True

    def main(self):
        """Main PyGame loop - renders game and registers user input"""
        running = True

        try:
            while running:
                events = pygame.event.get()
                running = self.process_events(events)
                
                if not running:
                    break

                if not running:
                    break

                # AI Logic: 
                # 1. AI vs AI mode: Always trigger AI turn
                # 2. Human vs AI mode: Trigger AI turn if it's the computer's turn
                is_computer_turn = (self.turn == self.computer)
                if (self.ai_mode or is_computer_turn) and running and not self.paused:
                    running = self.ai_turn()

                self.render()
                self.clock.tick(60)
        except KeyboardInterrupt:
            print("\nKeyboard Interrupt detected. Exiting gracefully...")
        finally:
            pygame.quit()

    def ai_turn(self):
        """Execute one AI turn. Returns False if the game should end."""
        # AI Pacing: slight delay to make moves feel more natural
        pygame.time.wait(500)

        player_name = "White" if self.turn.colour == 'W' else "Black"
        print(f"\n{player_name}'s turn: ")

        move = self.turn.get_minimax_best_move_for_player(self.board, self.window)

        if not move:
            print(f"{player_name} has no moves available. Game over!")
            return False

        _from, _to = move[0], move[1]
        piece = self.board.get_squares_piece(_from, int(_from[1]) if _from[1].isdigit() else 0) # Helper needed or direct access
        # actually board.pieces is a dict keyed by 'A1', so:
        piece = self.board.pieces.get(_from)
        piece_name = piece.get_type_name() if piece else "Unknown"
        print(f"{player_name} {piece_name} moves: {_from} -> {_to}")

        # Trigger animation
        start_pix = self.window.get_pixels_from_square(_from[0], int(_from[1]))
        end_pix = self.window.get_pixels_from_square(_to[0], int(_to[1]))
        self.anim_piece = piece
        self.anim_start_pix = start_pix
        self.anim_end_pix = end_pix
        self.anim_progress = 0

        # Save state before moving
        self.save_state()

        # Render the move visually (logically update board)
        if not self.board.move_piece(_from, _to):
            print(f"CRITICAL ERROR: AI attempted illegal move {_from} -> {_to}. Board rejected it.")
            return False

        self.last_move = (_from, _to)

        # Switch turns
        self.turn = self.player if self.turn == self.computer else self.computer

        # Render updated board (animation will start here)
        self.render()

        # Wait 2 seconds, but keep processing quit events
        wait_start = pygame.time.get_ticks()
        while pygame.time.get_ticks() - wait_start < 2000:
            events = pygame.event.get()
            running = self.process_events(events)
            if not running:
                return False
            
            # If paused, we stay in this loop and reset the wait timer to "resume" later
            if self.paused:
                wait_start = pygame.time.get_ticks() 
                self.render()
                self.clock.tick(60)
                continue

            self.render()
            self.clock.tick(60)

        return True

    def save_state(self):
        """Save the current state to history for undo"""
        state = {
            'pieces': copy.deepcopy(self.board.pieces),
            'turn': self.turn,
            'last_move': self.last_move
        }
        self.history.append(state)

    def undo_move(self):
        """Revert to the previous state. In Human vs AI, undoes twice."""
        if not self.history:
            print("Nothing to undo.")
            return

        # If in Human vs AI mode and it's the human's turn, 
        # undoing once just brings it back to AI's turn (who will move again).
        # So we undo TWICE to get back to the human's previous turn.
        undo_count = 2 if (not self.ai_mode and self.turn == self.player and len(self.history) >= 2) else 1
        
        for _ in range(undo_count):
            if not self.history:
                break
            state = self.history.pop()
            self.board.pieces = state['pieces']
            self.turn = state['turn']
            self.last_move = state['last_move']
        
        # Reset selection and animation
        self.square_selected = False
        self.anim_piece = None
        print("Undo successful.")

    def reset_game(self):
        """Reset the game to the starting state"""
        print("Resetting game...")
        factory = PieceFactory()
        self.board.pieces = factory.get_pieces()
        self.history = []
        self.turn = self.player
        self.last_move = None
        self.square_selected = False
        self.anim_piece = None
        self.paused = False
        print("Game reset.")

    def render(self):
        """Unified render method that includes highlights and pieces"""
        self.window.draw_board()
        
        # Handle piece animation
        animating_now = False
        if self.anim_piece and self.anim_start_pix and self.anim_end_pix:
            self.anim_progress += ANIMATION_SPEED
            if self.anim_progress >= 1.0:
                self.anim_piece = None
            else:
                animating_now = True
                # Linear interpolation
                px = self.anim_start_pix[0] + (self.anim_end_pix[0] - self.anim_start_pix[0]) * self.anim_progress
                py = self.anim_start_pix[1] + (self.anim_end_pix[1] - self.anim_start_pix[1]) * self.anim_progress
                
                # Render all pieces EXCEPT the one animating
                self.window.render_pieces(list(self.board.pieces.values()), exclude_piece=self.anim_piece)
                # Render the animating piece at its current interpolation
                self.window.render_piece_at(self.anim_piece, px, py)

        if not animating_now:
            self.window.render_pieces(list(self.board.pieces.values()))
        
        # Highlight last move
        if self.last_move and SHOW_MOVE_HIGHLIGHTS:
            _from, _to = self.last_move
            self.window.highlight_sq(_from, GREEN_RGB)
            self.window.highlight_sq(_to, RED_RGB)
            
        # Highlight current selection (human)
        if self.square_selected:
            self.window.highlight_sq(self.square_selected, BLUE_RGB)
            
        # Draw buttons
        self.window.draw_quit_button()
        self.window.draw_pause_button(self.paused)
        self.window.draw_undo_button()
        self.window.draw_reset_button()
        
        # Draw scores
        white_score = self.board.get_material_score('W')
        black_score = self.board.get_material_score('B')
        self.window.draw_scores(white_score, black_score)
            
        pygame.display.flip()

    def setup_players(self, algorithms=None):
        """Creates the initial player objects"""
        self.player = Player(PLAYER_COLOUR)
        self.computer = Player(COMPUTER_COLOUR)
        self.players = {'player': self.player, 'computer': self.computer}
        self.turn = self.player

    def select_square(self, sq):
        """Select a square or move a piece"""
        if not sq:
            return
        
        piece = self.board.pieces.get(sq)

        # 1. No square selected yet: handle selection
        if not self.square_selected:
            if not piece or piece.colour != self.turn.colour:
                if piece:
                    print(f"Not your turn! It's {self.turn.colour}'s turn.")
                return
            
            if(VERBOSE): print("Selecting square")
            self.square_selected = sq
            return

        # 2. Square already selected: handle move or deselection
        if(VERBOSE): print("Square already selected.")
        
        if self.square_selected == sq:
            # User selected already selected square -> Deselect
            if(VERBOSE): print("Deselecting square")
            self.square_selected = False
            return
        
        # Move piece
        src_sq = self.square_selected
        piece = self.board.pieces.get(src_sq)
        if piece:
            legal_moves = [m[1] for m in piece.get_possible_moves_for_piece(self.board)]
            if sq in legal_moves:
                # Trigger animation
                start_pix = self.window.get_pixels_from_square(src_sq[0], int(src_sq[1]))
                end_pix = self.window.get_pixels_from_square(sq[0], int(sq[1]))
                self.anim_piece = piece
                self.anim_start_pix = start_pix
                self.anim_end_pix = end_pix
                self.anim_progress = 0

                # Save state before moving
                self.save_state()

                # Move the piece in the board
                moved = self.board.move_piece(src_sq, sq)
                if moved:
                    self.turn = self.player if self.turn == self.computer else self.computer
                    self.last_move = (src_sq, sq)
                    
                    if self.board.is_in_check(self.turn.colour):
                        print(f"{self.turn.colour} is in Check!")
                
                self.square_selected = False
                return
            else:
                # Illegal move/target: if targeting own piece, switch selection, otherwise deselect
                if piece.colour == (self.board.pieces.get(sq).colour if self.board.pieces.get(sq) else None):
                    self.square_selected = sq
                    if(VERBOSE): print("Switching selection")
                else:
                    print("Illegal move (Check?)")
                    self.square_selected = False


if __name__ == "__main__":
    ai_mode = "--ai" in sys.argv
    window = Window()
    factory = PieceFactory()
    board = Board(factory.get_pieces())
    game = Game(window, board, ai_mode=ai_mode)
    game.main()