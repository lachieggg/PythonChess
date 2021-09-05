import os

### Positions
CHARS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
NUMS =  [1, 2, 3, 4, 5, 6, 7, 8]

### Widths
SQUARE_WIDTH = 75
BORDER_WIDTH = 50
PIECE_WIDTH = 20

### Images
BOARD_IMG_PATH = os.getcwd() + '/' + 'assets/' + 'board/' + 'board.png'
ASSETS_IMG_PATH = os.getcwd() + '/' + 'assets' + '/'

### Screen
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
SCREEN_DIMENSIONS = (SCREEN_WIDTH, SCREEN_HEIGHT)

### Colours
RED_RGB   = (255, 0, 0)
CREAM_RGB = (248, 248, 151)
BROWN_RGB = (107, 73, 4)

### Pieces
KING =   'K'
QUEEN =  'Q'
ROOK =   'R'
HORSE =  'H'
BISHOP = 'B'
PAWN =   'P'

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
