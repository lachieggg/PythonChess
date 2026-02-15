import os
import pygame

import Board
from Constants import *

class Window:
    def __init__(self):
        """Initializer for the Window"""
        pygame.init()
        pygame.display.set_caption('PythonChess')
        # Use DOUBLEBUF for smooth rendering on MacOS. HWSURFACE removed as it causes jitter.
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF)
        self.screen.fill((255, 255, 255))
        # Load and crop the 8x8 grid from board.png (it has a 50px baked-in border)
        full_board_img = pygame.image.load(BOARD_IMG_PATH).convert()
        # Crop center 600x600 (700 total - 50 on each side)
        crop_rect = pygame.Rect(50, 50, 600, 600)
        self.bgimg = full_board_img.subsurface(crop_rect).copy()
        
        # Scale ONLY the grid to the desired play area size (640x640)
        play_area_size = 8 * SQUARE_WIDTH
        self.bgimg = pygame.transform.smoothscale(self.bgimg, (play_area_size, play_area_size))
        self.image_cache = {}
        self.draw_board()
        self.map()

    def render_piece(self, piece):
        """Render a piece in the window"""
        if not piece:
            return
        pos = piece.get_position() # Position eg. 'H5' or 'A3'
        [x, y] = self.get_pixels_from_square(*pos)
        self.render_piece_at(piece, x, y)

    def render_piece_at(self, piece, x, y):
        """Render a piece at specific pixel coordinates, centering it in the square"""
        if not piece:
            return
        # Cache image loading and convert to alpha format for transparency support
        if piece.filename not in self.image_cache:
            img = pygame.image.load(piece.filename).convert_alpha()
            # Scale pieces to fit nicely in 80px squares (using PIECE_HEIGHT from constants)
            w, h = img.get_size()
            scale = PIECE_HEIGHT / h
            new_size = (int(w * scale), PIECE_HEIGHT)
            self.image_cache[piece.filename] = pygame.transform.smoothscale(img, new_size)
            
        icon = self.image_cache[piece.filename]
        # Calculate dynamic centering within the SQUARE_WIDTH x SQUARE_WIDTH block
        icon_w, icon_h = icon.get_size()
        center_x = x + (SQUARE_WIDTH - icon_w) // 2
        center_y = y + (SQUARE_WIDTH - icon_h) // 2
        self.screen.blit(icon, (center_x, center_y))

    def draw_board(self):
        """Draw the background and a substantial outer decorative border"""
        # Fill background with a deep walnut/dark charcoal color
        self.screen.fill((30, 25, 20))
        
        # Blit the board image into the centered play area
        self.screen.blit(self.bgimg, (BORDER_WIDTH, BORDER_WIDTH))
        
        # Draw a substantial decorative frame outside the board
        # board_rect is the play area (640x640 starting at 80,80)
        board_rect = pygame.Rect(BORDER_WIDTH, BORDER_WIDTH, 8 * SQUARE_WIDTH, 8 * SQUARE_WIDTH)
        
        # 1. Outer dark edge
        pygame.draw.rect(self.screen, (50, 40, 30), board_rect.inflate(40, 40), 20)
        # 2. Main beveled frame (medium wood)
        pygame.draw.rect(self.screen, (100, 75, 50), board_rect.inflate(20, 20), 10)
        # 3. Inner highlight rim
        pygame.draw.rect(self.screen, (160, 130, 90), board_rect.inflate(4, 4), 2)
        # 4. Deep shadow around the play area
        pygame.draw.rect(self.screen, (10, 5, 0), board_rect, 2)

    def render_pieces(self, pieces_list, exclude_piece=None):
        """Render all the pieces on the board except optionally one"""
        for piece in pieces_list:
            if piece == exclude_piece:
                continue
            self.render_piece(piece)

    def get_square_rgb(self, char, num):
        """Get the square RGB from char and num coords"""
        if self.get_square_colour(char, num):
            return CREAM_RGB
        return BROWN_RGB

    def get_square_colour(self, char, num):
        """Returns the square colour as a bool given the coordinates"""
        char_as_num = ord(char) - ord('A') + 1
        if ((char_as_num + num) % 2) == 0:
            return False
        return True

    def highlight_sq(self, sq, color=RED_RGB):
        """Highlight a square on the Window"""
        if not sq:
            return
        char, num = sq[0], int(sq[1])
        coords = self.get_pixels_from_square(char, num)
        if not coords:
            return
        x, y = coords

        pygame.draw.rect(
            self.screen,
            color,
            (x, y, SQUARE_WIDTH, SQUARE_WIDTH),
            HIGHLIGHTING_WIDTH
        )

    def get_screen_dimensions(self):
        """Return the dimensions of the screen as  a tuple"""
        return SCREEN_DIMENSIONS

    def map(self):
        """Map board squares to screen pixels for rendering and selecting squares"""
        self.pmap = {} # PMAP i.e. Pixel Map

        x = BORDER_WIDTH - SQUARE_WIDTH
        for char in CHARS:
            y = BORDER_WIDTH - SQUARE_WIDTH
            x += SQUARE_WIDTH
            for num in NUMS[::-1]:
                y += SQUARE_WIDTH
                key = char + str(num)
                self.pmap[key] = (x, y)

    def get_square_from_pixels(self, x, y, screen_width, screen_height):
        """Returns the square id from mouse position"""

        num_index = int(float(y - BORDER_WIDTH)/SQUARE_WIDTH)
        char_index = int(float(x - BORDER_WIDTH)/SQUARE_WIDTH)

        if num_index >= len(NUMS) or char_index >= len(CHARS):
            return False

        num = NUMS[::-1][num_index]
        char = CHARS[char_index]

        return char + str(num)

    def get_pixels_from_square(self, char, num):
        """Returns the mouse position from square char and number"""

        if char not in CHARS or num not in NUMS:
            return False

        return self.pmap.get(char + str(num))


    def get_square_pixel_limits(self, char, num):
        """Returns the pixel limits that constitute the mouse being over a square"""
        x_min, y_min = self.pmap.get(char + str(num))
        return [(x_min, x_min+SQUARE_WIDTH), (y_min, y_min+SQUARE_WIDTH)]

    def draw_quit_button(self):
        """Draw a quit button in the top right corner"""
        # Button dimensions
        btn_w, btn_h = 60, 30
        self.quit_btn_rect = pygame.Rect(SCREEN_WIDTH - btn_w - 10, 10, btn_w, btn_h)
        
        # Draw button shadow
        pygame.draw.rect(self.screen, (50, 50, 50), self.quit_btn_rect.move(2, 2))
        # Draw button
        pygame.draw.rect(self.screen, (200, 0, 0), self.quit_btn_rect)
        # Draw border
        pygame.draw.rect(self.screen, (255, 255, 255), self.quit_btn_rect, 2)
        
        # Text
        font = pygame.font.SysFont('Arial', 18, bold=True)
        text = font.render('QUIT', True, (255, 255, 255))
        text_rect = text.get_rect(center=self.quit_btn_rect.center)
        self.screen.blit(text, text_rect)

    def draw_pause_button(self, paused):
        """Draw a pause button next to the quit button"""
        btn_w, btn_h = 80, 30
        # Position it to the left of the QUIT button (which is at SCREEN_WIDTH - 60 - 10)
        self.pause_btn_rect = pygame.Rect(SCREEN_WIDTH - btn_w - 80, 10, btn_w, btn_h)
        
        color = (180, 180, 0) if not paused else (0, 180, 0)
        label = 'PAUSE' if not paused else 'RESUME'
        
        # Shadow
        pygame.draw.rect(self.screen, (50, 50, 50), self.pause_btn_rect.move(2, 2))
        # Button
        pygame.draw.rect(self.screen, color, self.pause_btn_rect)
        # Border
        pygame.draw.rect(self.screen, (255, 255, 255), self.pause_btn_rect, 2)
        
        font = pygame.font.SysFont('Arial', 18, bold=True)
        text = font.render(label, True, (255, 255, 255))
        text_rect = text.get_rect(center=self.pause_btn_rect.center)
        self.screen.blit(text, text_rect)

    def is_quit_clicked(self, pos):
        """Check if the quit button was clicked"""
        if hasattr(self, 'quit_btn_rect'):
            return self.quit_btn_rect.collidepoint(pos)
        return False

    def is_pause_clicked(self, pos):
        """Check if the pause button was clicked"""
        if hasattr(self, 'pause_btn_rect'):
            return self.pause_btn_rect.collidepoint(pos)
        return False
