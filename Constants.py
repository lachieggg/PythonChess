import os

### Size
BOARD_WIDTH = BOARD_HEIGHT = 8

### Indexes
NUM_START = 1
CHAR_START = ord('A')

### Board
NUMS =  [n      for n in range(NUM_START,  NUM_START+BOARD_HEIGHT)]
CHARS = [chr(c) for c in range(CHAR_START, CHAR_START+BOARD_WIDTH)]

### Widths
PIECE_WIDTH = 20
SQUARE_WIDTH = 75
BORDER_WIDTH = 50

### Images
BOARD_IMG_PATH = os.getcwd() + '/' + 'assets/' + 'board/' + 'board.png'
ASSETS_IMG_PATH = os.getcwd() + '/' + 'assets' + '/'

### Screen
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
SCREEN_DIMENSIONS = (SCREEN_WIDTH, SCREEN_HEIGHT)

### Colours
CREAM_RGB = (248, 248, 151)
BROWN_RGB = (107, 73, 4)
RED_RGB   = (255, 0, 0)

### Highlighting
HIGHLIGHTING_WIDTH = 1

### Pieces
BISHOP = 'B'
QUEEN =  'Q'
HORSE =  'H'
KING =   'K'
ROOK =   'R'
PAWN =   'P'

PIECE_MAPPING = {
    BISHOP: 'Bishop',
    QUEEN:  'Queen',
    HORSE:  'Horse',
    KING:   'King',
    ROOK:   'Rook',
    PAWN:   'Pawn'
}

### Teams
WHITE = 'White'
BLACK = 'Black'
WHITE_ROW = 1
BLACK_ROW = 8

### Pieces
WHITE_MAIN_PIECES = [
    [ROOK,   WHITE, 'A', WHITE_ROW],
    [HORSE,  WHITE, 'B', WHITE_ROW],
    [BISHOP, WHITE, 'C', WHITE_ROW],
    [QUEEN,  WHITE, 'D', WHITE_ROW],
    [KING,   WHITE, 'E', WHITE_ROW],
    [BISHOP, WHITE, 'F', WHITE_ROW],
    [HORSE,  WHITE, 'G', WHITE_ROW],
    [ROOK,   WHITE, 'H', WHITE_ROW]
]
BLACK_MAIN_PIECES = [
    [ROOK,   BLACK, 'A', BLACK_ROW],
    [HORSE,  BLACK, 'B', BLACK_ROW],
    [BISHOP, BLACK, 'C', BLACK_ROW],
    [QUEEN,  BLACK, 'D', BLACK_ROW],
    [KING,   BLACK, 'E', BLACK_ROW],
    [BISHOP, BLACK, 'F', BLACK_ROW],
    [HORSE,  BLACK, 'G', BLACK_ROW],
    [ROOK,   BLACK, 'H', BLACK_ROW]
]
WHITE_PAWNS = [
    [PAWN, WHITE, 'A', WHITE_ROW+1],
    [PAWN, WHITE, 'B', WHITE_ROW+1],
    [PAWN, WHITE, 'C', WHITE_ROW+1],
    [PAWN, WHITE, 'D', WHITE_ROW+1],
    [PAWN, WHITE, 'E', WHITE_ROW+1],
    [PAWN, WHITE, 'F', WHITE_ROW+1],
    [PAWN, WHITE, 'G', WHITE_ROW+1],
    [PAWN, WHITE, 'H', WHITE_ROW+1]
]
BLACK_PAWNS = [
    [PAWN, BLACK, 'A', BLACK_ROW-1],
    [PAWN, BLACK, 'B', BLACK_ROW-1],
    [PAWN, BLACK, 'C', BLACK_ROW-1],
    [PAWN, BLACK, 'D', BLACK_ROW-1],
    [PAWN, BLACK, 'E', BLACK_ROW-1],
    [PAWN, BLACK, 'F', BLACK_ROW-1],
    [PAWN, BLACK, 'G', BLACK_ROW-1],
    [PAWN, BLACK, 'H', BLACK_ROW-1]
]
PIECES_DATA = WHITE_MAIN_PIECES + BLACK_MAIN_PIECES + WHITE_PAWNS + BLACK_PAWNS
