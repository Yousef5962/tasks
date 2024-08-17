class Gamestate():
    def __init__(self):
        self.board = [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bP","bP","bP","bP","bP","bP","bP","bP"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wP","wP","wP","wP","wP","wP","wP","wP"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]]
        self.whitetomove = True
        self.movelog = []
    def makemove(self,move):
        self.board[move.startrow][move.startcol] = "--"
        self.board[move.endrow][move.endcol] = move.piecemoved
        self.movelog.append(move)
        self.whitetomove = not self.whitetomove
    def undomove(self):
        if len(self.movelog) != 0:
            move = self.movelog.pop()
            self.board[move.startrow][move.startcol] = move.piecemoved
            self.board[move.endrow][move.endcol] = move.piececaptured
            self.whitetomove = not self.whitetomove

    def getvalidmoves(self):
        return self.getallpossiblemoves()

    def getallpossiblemoves(self):
        moves = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0]
                if (turn == "w" and self.whitetomove) or (turn =="b" and not self.whitetomove):
                    piece = self.board[r][c][1]
                    if piece == "P":
                        self.getPawnmoves(r,c,moves)
                    elif piece == "R":
                        self.getRookmoves(r,c,moves)
                    elif piece == "B":
                        self.getBishopmoves(r,c,moves)
                    elif piece == "N":
                        self.getKnightmoves(r,c,moves)
                    elif piece == "K":
                        self.getKingmoves(r,c,moves)
                    elif piece == "Q":
                        self.getQueenmoves(r,c,moves)
        return moves

                    
    def getPawnmoves(self, r, c, moves):
        if self.whitetomove:
            if self.board[r-1][c] == "--":
                moves.append(move((r, c), (r-1, c), self.board))
                if r == 6 and self.board[r-2][c] == "--":
                    moves.append(move((r, c), (r-2, c), self.board))
            if c - 1 >= 0:
                if self.board[r-1][c-1][0] == "b":
                    moves.append(move((r, c), (r-1, c-1), self.board))
            if c + 1 <= 7:
                if self.board[r-1][c+1][0] == "b":
                    moves.append(move((r, c), (r-1, c+1), self.board))
        else:
            if self.board[r+1][c] == "--":
                moves.append(move((r, c), (r+1, c), self.board))
                if r == 1 and self.board[r+2][c] == "--":
                    moves.append(move((r, c), (r+2, c), self.board))
            if c - 1 >= 0:
                if self.board[r+1][c-1][0] == "w":
                    moves.append(move((r, c), (r+1, c-1), self.board))
            if c + 1 <= 7:
                if self.board[r+1][c+1][0] == "w":
                    moves.append(move((r, c), (r+1, c+1), self.board))


    def getRookmoves(self, r, c, moves):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        enemycolor = "b" if self.whitetomove else "w"
        for d in directions:
            for i in range(1, 8):
                endrow = r + d[0] * i
                endcol = c + d[1] * i
                if 0 <= endrow < 8 and 0 <= endcol < 8:
                    endpiece = self.board[endrow][endcol]
                    if endpiece == "--":
                        moves.append(move((r, c), (endrow, endcol), self.board))
                    elif endpiece[0] == enemycolor:
                        moves.append(move((r, c), (endrow, endcol), self.board))
                        break
                    else:
                        break
                else:
                    break

    def getBishopmoves(self, r, c, moves):
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        enemycolor = "b" if self.whitetomove else "w"
        for d in directions:
            for i in range(1, 8):
                endrow = r + d[0] * i
                endcol = c + d[1] * i
                if 0 <= endrow < 8 and 0 <= endcol < 8:
                    endpiece = self.board[endrow][endcol]
                    if endpiece == "--":
                        moves.append(move((r, c), (endrow, endcol), self.board))
                    elif endpiece[0] == enemycolor:
                        moves.append(move((r, c), (endrow, endcol), self.board))
                        break
                    else:
                        break
                else:
                    break

    def getKnightmoves(self, r, c, moves):
        knightmoves = [
            (-2, -1), (-1, -2), (1, -2), (2, -1),
            (2, 1), (1, 2), (-1, 2), (-2, 1)
        ]
        allycolor = "w" if self.whitetomove else "b"
        for m in knightmoves:
            endrow = r + m[0]
            endcol = c + m[1]
            if 0 <= endrow < 8 and 0 <= endcol < 8:
                endpiece = self.board[endrow][endcol]
                if endpiece == "--" or endpiece[0] != allycolor:
                    moves.append(move((r, c), (endrow, endcol), self.board))
    
    def getKingmoves(self, r, c, moves):
        kingmoves = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1),
            (0, 1), (1, -1), (1, 0), (1, 1)
        ]
        allycolor = "w" if self.whitetomove else "b"
        for i in range(8):
            endrow = r + kingmoves[i][0]
            endcol = c + kingmoves[i][1]
            if 0 <= endrow < 8 and 0 <= endcol < 8:
                endpiece = self.board[endrow][endcol]
                if endpiece == "--" or endpiece[0] != allycolor:
                    moves.append(move((r, c), (endrow, endcol), self.board))

    def getQueenmoves(self, r, c, moves):
        self.getRookmoves(r, c, moves)
        self.getBishopmoves(r, c, moves)

    def is_check(self):
        king_row, king_col = self.find_king(self.whitetomove)
        if king_row is None or king_col is None:
            return False
        opponent_moves = self.getallpossiblemoves_for_opponent()
        for move in opponent_moves:
            if move.endrow == king_row and move.endcol == king_col:
                return True
        return False

    def find_king(self, is_white):
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                piece = self.board[r][c]
                if piece[0] == ("w" if is_white else "b") and piece[1] == "K":
                    return r, c
        return None, None


    def getallpossiblemoves_for_opponent(self):
        self.whitetomove = not self.whitetomove
        moves = self.getallpossiblemoves()
        self.whitetomove = not self.whitetomove
        return moves

    def is_checkmate(self):
        if not self.is_check():
            return False
        for move in self.getvalidmoves():
            self.makemove(move)
            if not self.is_check():
                self.undomove()
                return False
            self.undomove()
        return True


    def is_stalemate(self):
        if self.is_check():
            return False
        if len(self.getvalidmoves()) == 0:
            return True
        return False



class move():
    rankstorows = {"1":7,"2":6,"3":5,"4":4,
                   "5":3,"6":2,"7":1,"8":0}
    rowstoranks = {v: k for k, v in rankstorows.items()}
    filestocol = {"a":0,"b":1,"c":2,"d":3,
                   "e":4,"f":5,"g":6,"h":7}
    colstofiles = {v: k for k,v in filestocol.items()}

    def __init__(self , startsq , endsq , board):
        self.startrow = startsq[0]
        self.startcol = startsq[1]
        self.endrow = endsq[0]
        self.endcol = endsq[1]
        self.piecemoved = board[self.startrow][self.startcol]
        self.piececaptured = board[self.endrow][self.endcol]
        self.moveID = self.startrow * 1000 + self.startcol * 100 + self.endrow * 10 + self.endcol
    def __eq__(self, other):
        if isinstance(other, move):
            return self.moveID == other.moveID
        return False
    def getchessnotation(self):
        return self.getrankfiles(self.startrow,self.startcol) +self.getrankfiles(self.endrow,self.endcol)
    
    def getrankfiles(self,r,c):
        return self.colstofiles[c] + self.rowstoranks[r]