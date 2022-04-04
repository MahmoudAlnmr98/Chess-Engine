#
# this is the main driver which is responsible for handling 
# 1-user input 
# 2-current game state
#


import pygame as p
import ChessEngine

WIDTH = HEIGHT = 512 
DIMENSIONS = 8              # dimensions are 8x8
SQ_SIZQ = HEIGHT // DIMENSIONS
MAX_FPS = 15
IMAGES = {}
global screen
# initialize images dictionary, will be called once in main for speed

def LoadImages():
    pieces = ["bR", "bN", "bB", "bQ", "bk", "bN", "bR", "bP", "wR", "wN", "wB", "wQ", "wk", "wN", "wR", "wP"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png") , (SQ_SIZQ, SQ_SIZQ))
        #now we can access images by saying for example IMAGES["wP"]
        #p.transform.scale is used to scale the image to size desired

# main deiver
# 1-handling inputs 
# 2-updating graphics

def main():
    p.init()
    screen = p.display.set_mode((HEIGHT,WIDTH))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    #choose backgroung as image
    #myboard = p.transform.scale(p.image.load("images/board.png"),(512,512))
    #screen.blit(myboard, (0,0))
    gs = ChessEngine.GameState()            # gs = game state
    LoadImages()                            # loaded once before infinte loop
    running = True
    '''
    the player in to move a piece he selects two squares
    the first square is the the square at which the piece is located (presses in pawn for example)
    the second square is the target square to place the piece
    we are going to create a tuple to store the (x, y) of the current click
    and a list to store both click, a list of two tuples, so the list will contain
    1- the selected piece location
    2- the target square location
    '''
    sqSelected = ()     # tuple to keep track of last click ,deafult  no square selected
    playerClicks = []   # keep track of user clicks, two clicks
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()        #gives (x, y) locations of mouse
                # algorithm to find the row and column in which the mouse in giving
                # (x, y) coordinates
                # the steps are
                # find the row*column area in our case we have it already in SQ_SIZE
                # divide the x coordinate by the previous area to get the column
                # divide the y coordinate by the previous are to get the row
                col = location[0] // SQ_SIZQ
                row = location[1] // SQ_SIZQ

                '''
                now we will check if the sqSelected variable == (row, coloumn)
                if so then the user already pressed that square, so he wants to deselect it 
                the the solution to deselect is the following:
                1- if sqSelected == row, col
                then empty the sqSelected and empty the list playerClicks
                this means we return to the state of no square selected which means 
                we select no square or deselct the selected one
                if not then record the current click in the tuple and append that to the list 
                then check if the length of the list is equal 2, then we have the 2 locations
                '''
                if sqSelected == (row, col):
                    sqSelected = ()
                    playerClicks = []
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected)
                
                if len(playerClicks) == 2 :
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.getChessNotation())
                    gs.makeMove(move)
                    sqSelected = ()
                    playerClicks = []

        clock.tick(MAX_FPS)
        p.display.flip()
        drawGameState(screen, gs)
        
        

# this function responsible for all graphics in current game state
def drawGameState(screen, gs):
    drawBoard(screen)               #draw squares on the board
    drawPieces(screen, gs.board)           #draw pieces on their squares


# this function draws squares on the board
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("grey")]
    for r in range(DIMENSIONS):
        for c in range(DIMENSIONS):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZQ, r*SQ_SIZQ, SQ_SIZQ, SQ_SIZQ))
            

#this function draw pieces on the board using current game states
def drawPieces(screen, board):
    for r in range(DIMENSIONS):
        for c in range(DIMENSIONS):
            piece = board[r][c]
            if piece != "--":       # not empty square
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZQ, r*SQ_SIZQ, SQ_SIZQ, SQ_SIZQ))
                
    



main()
