import pygame
from Constants import *

class Window:
    def __init__(self):
        """Initialize the chess window"""
        pygame.init()
        pygame.display.set_caption('PythonChess')
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF)
        
        # Load and prepare board image
        full_board = pygame.image.load(BOARD_IMG_PATH).convert()
        w, h = full_board.get_size()
        grid_size = SOURCE_SQUARE_WIDTH * 8
        crop_rect = pygame.Rect((w - grid_size) // 2, (h - grid_size) // 2, grid_size, grid_size)
        self.bgimg = pygame.transform.smoothscale(
            full_board.subsurface(crop_rect).copy(), 
            (8 * SQUARE_WIDTH, 8 * SQUARE_WIDTH)
        )
        
        self.image_cache = {}
        self._build_pixel_map()
        self.draw_board()

    def _build_pixel_map(self):
        """Map board squares to screen coordinates"""
        self.pmap = {}
        for i, char in enumerate(CHARS):
            for j, num in enumerate(NUMS[::-1]):
                self.pmap[char + str(num)] = (
                    BORDER_WIDTH + i * SQUARE_WIDTH,
                    BORDER_WIDTH + j * SQUARE_WIDTH
                )

    def draw_board(self):
        """Draw the board with decorative border and labels"""
        self.screen.fill((30, 25, 20))
        self.screen.blit(self.bgimg, (BORDER_WIDTH, BORDER_WIDTH))
        
        # Draw decorative frame
        board_rect = pygame.Rect(BORDER_WIDTH, BORDER_WIDTH, 8 * SQUARE_WIDTH, 8 * SQUARE_WIDTH)
        pygame.draw.rect(self.screen, (50, 40, 30), board_rect.inflate(40, 40), 20)
        pygame.draw.rect(self.screen, (100, 75, 50), board_rect.inflate(20, 20), 10)
        pygame.draw.rect(self.screen, (160, 130, 90), board_rect.inflate(4, 4), 2)
        pygame.draw.rect(self.screen, (10, 5, 0), board_rect, 2)
        
        self._draw_labels()

    def _draw_labels(self):
        """Draw coordinate labels (A-H, 1-8)"""
        font = pygame.font.SysFont('Arial', 24, bold=True)
        color = (220, 200, 160)
        
        # Ranks (1-8)
        for i in range(8):
            text = font.render(str(8 - i), True, color)
            pos = (BORDER_WIDTH // 2, BORDER_WIDTH + i * SQUARE_WIDTH + SQUARE_WIDTH // 2)
            self.screen.blit(text, text.get_rect(center=pos))
        
        # Files (A-H)
        for i in range(8):
            text = font.render(chr(ord('A') + i), True, color)
            pos = (BORDER_WIDTH + i * SQUARE_WIDTH + SQUARE_WIDTH // 2, SCREEN_HEIGHT - BORDER_WIDTH // 2)
            self.screen.blit(text, text.get_rect(center=pos))

    def render_piece(self, piece):
        """Render a piece at its current position"""
        if not piece:
            return
        x, y = self.get_pixels_from_square(*piece.get_position())
        self.render_piece_at(piece, x, y)

    def render_piece_at(self, piece, x, y):
        """Render a piece at specific pixel coordinates"""
        if not piece:
            return
        
        # Load and cache piece image
        if piece.filename not in self.image_cache:
            img = pygame.image.load(piece.filename).convert_alpha()
            w, h = img.get_size()
            scale = PIECE_HEIGHT / h
            self.image_cache[piece.filename] = pygame.transform.smoothscale(
                img, (int(w * scale), PIECE_HEIGHT)
            )
        
        icon = self.image_cache[piece.filename]
        icon_w, icon_h = icon.get_size()
        center_pos = (x + (SQUARE_WIDTH - icon_w) // 2, y + (SQUARE_WIDTH - icon_h) // 2)
        self.screen.blit(icon, center_pos)

    def render_pieces(self, pieces_list, exclude_piece=None):
        """Render all pieces except optionally one"""
        for piece in pieces_list:
            if piece != exclude_piece:
                self.render_piece(piece)

    def highlight_sq(self, sq, color=RED_RGB):
        """Highlight a square"""
        if not sq:
            return
        x, y = self.get_pixels_from_square(sq[0], int(sq[1]))
        pygame.draw.rect(self.screen, color, (x, y, SQUARE_WIDTH, SQUARE_WIDTH), HIGHLIGHTING_WIDTH)

    def get_square_from_pixels(self, x, y, screen_width=None, screen_height=None):
        """Get square ID from pixel coordinates"""
        char_idx = int((x - BORDER_WIDTH) / SQUARE_WIDTH)
        num_idx = int((y - BORDER_WIDTH) / SQUARE_WIDTH)
        
        if char_idx < 0 or char_idx >= len(CHARS) or num_idx < 0 or num_idx >= len(NUMS):
            return False
        
        return CHARS[char_idx] + str(NUMS[::-1][num_idx])

    def get_pixels_from_square(self, char, num):
        """Get pixel coordinates from square"""
        if char not in CHARS or num not in NUMS:
            return False
        return self.pmap.get(char + str(num))

    def draw_quit_button(self):
        """Draw quit button in top right"""
        self.quit_btn_rect = pygame.Rect(SCREEN_WIDTH - 70, 10, 60, 30)
        pygame.draw.rect(self.screen, (50, 50, 50), self.quit_btn_rect.move(2, 2))
        pygame.draw.rect(self.screen, (200, 0, 0), self.quit_btn_rect)
        pygame.draw.rect(self.screen, (255, 255, 255), self.quit_btn_rect, 2)
        
        font = pygame.font.SysFont('Arial', 18, bold=True)
        text = font.render('QUIT', True, (255, 255, 255))
        self.screen.blit(text, text.get_rect(center=self.quit_btn_rect.center))

    def draw_pause_button(self, paused):
        """Draw pause/resume button"""
        self.pause_btn_rect = pygame.Rect(SCREEN_WIDTH - 180, 10, 100, 30)
        color = (0, 180, 0) if paused else (180, 180, 0)
        label = 'RESUME' if paused else 'PAUSE'
        
        pygame.draw.rect(self.screen, (50, 50, 50), self.pause_btn_rect.move(2, 2))
        pygame.draw.rect(self.screen, color, self.pause_btn_rect)
        pygame.draw.rect(self.screen, (255, 255, 255), self.pause_btn_rect, 2)
        
        font = pygame.font.SysFont('Arial', 18, bold=True)
        text = font.render(label, True, (255, 255, 255))
        self.screen.blit(text, text.get_rect(center=self.pause_btn_rect.center))

    def draw_scores(self, white_score, black_score):
        """Draw player scores in the top left margin"""
        font = pygame.font.SysFont('Arial', 18, bold=True)
        color = (220, 200, 160) # Parchment gold
        
        white_text = font.render(f"WHITE: {white_score}", True, color)
        black_text = font.render(f"BLACK: {black_score}", True, color)
        
        # Position in top-left margin
        self.screen.blit(white_text, (20, 10))
        self.screen.blit(black_text, (20, 35))

    def draw_undo_button(self):
        """Draw undo button"""
        self.undo_btn_rect = pygame.Rect(SCREEN_WIDTH - 290, 10, 100, 30)
        
        pygame.draw.rect(self.screen, (50, 50, 50), self.undo_btn_rect.move(2, 2))
        pygame.draw.rect(self.screen, (70, 130, 180), self.undo_btn_rect) # Steel Blue
        pygame.draw.rect(self.screen, (255, 255, 255), self.undo_btn_rect, 2)
        
        font = pygame.font.SysFont('Arial', 18, bold=True)
        text = font.render('UNDO', True, (255, 255, 255))
        self.screen.blit(text, text.get_rect(center=self.undo_btn_rect.center))

    def draw_reset_button(self):
        """Draw reset button"""
        self.reset_btn_rect = pygame.Rect(SCREEN_WIDTH - 400, 10, 100, 30)
        
        pygame.draw.rect(self.screen, (50, 50, 50), self.reset_btn_rect.move(2, 2))
        pygame.draw.rect(self.screen, (255, 140, 0), self.reset_btn_rect) # Dark Orange
        pygame.draw.rect(self.screen, (255, 255, 255), self.reset_btn_rect, 2)
        
        font = pygame.font.SysFont('Arial', 18, bold=True)
        text = font.render('RESET', True, (255, 255, 255))
        self.screen.blit(text, text.get_rect(center=self.reset_btn_rect.center))

    def is_quit_clicked(self, pos):
        """Check if quit button was clicked"""
        return hasattr(self, 'quit_btn_rect') and self.quit_btn_rect.collidepoint(pos)

    def is_pause_clicked(self, pos):
        """Check if pause button was clicked"""
        return hasattr(self, 'pause_btn_rect') and self.pause_btn_rect.collidepoint(pos)

    def is_undo_clicked(self, pos):
        """Check if undo button was clicked"""
        return hasattr(self, 'undo_btn_rect') and self.undo_btn_rect.collidepoint(pos)

    def is_reset_clicked(self, pos):
        """Check if reset button was clicked"""
        return hasattr(self, 'reset_btn_rect') and self.reset_btn_rect.collidepoint(pos)

    # Removed unused methods
    def get_screen_dimensions(self):
        return SCREEN_DIMENSIONS

    def get_square_colour(self, char, num):
        char_num = ord(char) - ord('A') + 1
        return ((char_num + num) % 2) == 1

    def get_square_rgb(self, char, num):
        return CREAM_RGB if self.get_square_colour(char, num) else BROWN_RGB

    def get_square_pixel_limits(self, char, num):
        x, y = self.pmap.get(char + str(num))
        return [(x, x + SQUARE_WIDTH), (y, y + SQUARE_WIDTH)]