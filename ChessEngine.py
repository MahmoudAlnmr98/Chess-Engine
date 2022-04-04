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

        self.whiteToMove = True
        self.movingLog = []

    def makeMove (self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.movingLog.append(move)                         # log the move
        self.whiteToMove = not self.whiteToMove             # swap players




class Move():


# class to keep track of moves also more features will be added later
# at first we wnt to keep track of the moves 
# 1- the location of the move selected
# 2- the destination of the location (the piece captured or no piece captured)

    # adding chess notation
    # maps keys to values, key : value
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4,
                   "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()} #reverse the dictionary
    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3,
                   "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}


    def __init__(self, startSq, endSq, board):
        # next lines stored the locations of the move
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]

    
    
    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)



    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r]

