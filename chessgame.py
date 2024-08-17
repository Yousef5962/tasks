import pygame as p
import chessengine
width = hight =512
dimension = 8
square = width // dimension
max_fps = 15
images = {}

def loadimages():
    pieces = ["wP","wR","wN","wB","wK","wQ","bP","bR","bN","bB","bK","bQ"]
    for piece in pieces:    
        images[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"),(square,square))
def main():
    p.init()
    screen = p.display.set_mode((width, hight))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = chessengine.Gamestate()
    validmoves = gs.getvalidmoves()
    movemade = False 

    loadimages()
    running = True
    sqselected = ()
    playerclicks = []
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0] // square
                row = location[1] // square
                if sqselected == (row, col):
                    sqselected = (row, col)
                    playerclicks = []
                else:
                    sqselected = (row, col)
                    playerclicks.append(sqselected)
                if len(playerclicks) == 2:
                    move = chessengine.move(playerclicks[0], playerclicks[1], gs.board)
                    print(move.getchessnotation())
                    if move in validmoves:
                        gs.makemove(move)
                        movemade = True
                    sqselected = ()
                    playerclicks = []

            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:
                    gs.undomove()  
                    movemade = True

        if movemade:
            validmoves = gs.getvalidmoves()
            print(f"Is Checkmate: {gs.is_checkmate()}")
            print(f"Is Stalemate: {gs.is_stalemate()}")
            
            while gs.is_check():
                if gs.is_checkmate():
                    print("Checkmate!")
                    running = False
                elif gs.is_stalemate():
                    print("Stalemate!")
                    running = False
                else:
                    print("check!")
                    running = False
                break
            movemade = False
        
        drawgamestate(screen, gs)
        clock.tick(max_fps)
        p.display.flip()
    
    p.quit()

def drawgamestate(screen, gs):
    drawboard(screen)
    drawpieces(screen, gs.board)

def drawboard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(dimension):
        for c in range(dimension):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen,color,p.Rect(c*square,r*square,square,square))
def drawpieces(screen, board):
    for r in range(dimension):
        for c in range(dimension):
            piece = board[r][c]
            if piece != "--":
                screen.blit(images[piece],p.Rect(c*square,r*square,square,square))
if __name__ == "__main__" :
    main()