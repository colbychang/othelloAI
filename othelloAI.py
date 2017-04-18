# AI

from graphics import *

class Piece:

    def __init__(self, color, location, win):
        self.rowList = [0,1,2,3,4,5,6,7]
        self.columnList = [0, 1, 2, 3, 4, 5, 6, 7]
        self.win = win
        self.color = color
        self.loc = location
        self.row = row 
        self.x = location[0] * 100 - 50
        self.y = location[0] * 100 - 50
        self.circ = Circle(Point(self.x, self.y), 40)

        self.location = [self.column, self.row]
                

    def getLocation(self):
        return [self.column, self.row]


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


    def colorFlip(self, tiles, newLoc, myPiece

        
        
