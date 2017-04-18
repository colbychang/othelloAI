# AI

from graphics import *

class Piece:

    def __init__(self, color, location, row, win):
        self.letterList = ["a", "b", "c", "d", "e", "f", "g", "h"]
        self.numberList = [1, 2, 3, 4, 5, 6, 7, 8]
        self.win = win
        self.color = color
        self.loc = location
        self.row = row 
        self.x = location[0] * 100 - 50
        self.y = location[0] * 100 - 50
        self.circ = Circle(Point(self.x, self.y), 40)

        if self.color == "white":
            if self.row == 3:
                self.currentNumber = 3
                

            if self.row == 4:
                self.currentNumber = 4

        if self.color == "black":
            if self.row == 3:
                self.currentNumber = 4

            if self.row == 4:
                self.currentNumber = 3

        self.location = [self.row, self.currentNumber]
                

    def getLocation(self):
        return [self.currentNumber, self.currentLetter]




    def movePiece(self, newLoc, myPiece):
        oldPoint = self.tiles[self.row][self.currentLetter]
        oldX = oldPoint.getX()
        oldY = oldPoint.getY()

        self.newNumber = newLoc[0]
        self.newLetter = newLoc[1]

        newPoint = self.locationList[self.newNumber][self.newLetter]
        # check the list used here 
        newX = newPoint.getX()
        newY = newPoint.getY()
        dx = newX - oldX
        dy = newY - oldY
        myPiece.move(dx, dy)


        
        
