from graphics import *

class Piece:

    def __init__(self, color, location, win):
        self.rowList = [0,1,2,3,4,5,6,7]
        self.columnList = [0, 1, 2, 3, 4, 5, 6, 7]
        self.win = win
        self.color = color
        self.loc = location
##        self.row = row 
        self.x = location[0] * 100 + 50
        self.y = location[1] * 100 + 50
        self.circ = Circle(Point(self.x, self.y), 40)
        self.circ.setFill(color)
        self.circ.draw(win)
##        self.location = [self.column, self.row]
                

##    def getLocation(self):
##        return [self.column, self.row]


##
##    def movePiece(self, tiles, newLoc, myPiece):
##        oldPoint = self.tiles[self.row][self.currentLetter]
##        oldX = oldPoint.getX()
##        oldY = oldPoint.getY()
##
##        self.newNumber = newLoc[0]
##        self.newLetter = newLoc[1]
##
##        newPoint = self.locationList[self.newNumber][self.newLetter]
##        # check the list used here 
##        newX = newPoint.getX()
##        newY = newPoint.getY()
##        dx = newX - oldX
##        dy = newY - oldY
##        myPiece.move(dx, dy)

    def changeColor(self, turn_color):
        if turn_color == "white":
            self.circ.setFill("white")
        elif turn_color == "black":
            self.circ.setFill("black")
            

    def colorFlip(self, tiles, turn_color, opponent_color, piecepos):

        
        
            
          #  xpiece, ypiece = position of piece
          ##### find the function used to find these coordinates #####
            
           # xdireclist = [-1,-1,-1,0,0,1,1,1]
           # ydireclist = [-1,0,1,-1,1,-1,0,1]

            for dx in [-1,0,1]:
                for dy in [-1,0,1]:
                    if dx == 0 and dy == 0:
                        jimbo = 1
                    else:
                        xmove = xpiece + dx
                        ymove = ypiece + dy

                    if turn_color == "white":
                        while (tiles[xmove][ymove]).ID == opponentColor:
                            whitepiece = Piece("white", ((tiles[xmove],[ymove]).ID),win)
                            whitePieceList.append(whitepiece)
                            xmove = xmove + dx
                            ymove = ymove + dy
                            if (tiles[xmove][ymove]).ID == turn_color or (tiles[xmove][ymove]).ID == "":
                                break


                    if turn_color == "black": 
                        while (tiles[xmove][ymove]).ID == opponentColor:
                            blackpiece = Piece("black", ((tiles[xmove][ymove]).ID),win)
                            blackPieceList.append(blackpiece)
                            xmove = xmove + dx
                            ymove = ymove + dy
                            if (tiles[xmove][ymove]).ID == turn_color or (tiles[xmove][ymove]).ID == "":
                                break
                            
                            
                    


        

        
        
