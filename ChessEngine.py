#
# this class will:
# 1-store all information of the current state of the game
# 2-determine the valid moves at current state
# 3-keep moves log
#

class GameState():
    def __init__(self):
        # chess board is 8x8 2d list, each element has 2 characters
        # the firts one is the color "w" or "b"
        # the secong one is the piece type
        # "--" represents blank space with no pieces
        self.board = [
            ["bR", "bN", "bB", "bQ", "bk", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wk", "wB", "wN", "wR"],
        ]

