from graphics import *

class Button:
    def __init__(self, win, center, width, height, label):
        """draws the button itself"""
        self.xMin = center.getX() - width/2
        self.xMax = center.getX() + width/2
        self.yMin = center.getY() - height/2
        self.yMax = center.getY() + height/2
        pt1 = Point(self.xMin, self.yMin)
        pt2 = Point(self.xMax, self.yMax)
        self.outline = Rectangle(pt1, pt2)
        self.outline.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.occupied = False
        self.color = "white"
        self.piece_color = ""

    def setColor(self, new_color):
        """changes the color"""
        self.color = new_color
        self.outline.setFill(self.color)

    def activate(self, turn_color):
        """activates the button if it's clickable or not"""
        changing_color = False
        
        # for possible movement spots that aren't occupied 
        if not self.occupied:
            temp_color = "darksalmon"
            changing_color = True
            
        # for possible movement spots that are occupied
        elif self.piece_color != turn_color:
            temp_color = "red"
            changing_color = True
        if changing_color:
            self.outline.setFill(temp_color)
        self.active = True

    def deactivate(self):
        """deactivates button"""
        self.label.setFill("black")
        self.outline.setWidth(1)
        self.outline.setFill(self.color)
        self.active = False

    def clicked(self, pt):
        """checks if button was clicked"""
        wasClicked = False
        if self.xMin <= pt.getX() and self.xMax >= pt.getX():
            if self.yMin <= pt.getY() and self.yMax >= pt.getY():
                if self.active == True:
                    wasClicked = True
        return wasClicked

    def occupy(self, piece):
        """occupies square with a piece"""
        self.occupied = True
        self.piece_color = piece.color
        self.piece = piece

##    def tempOccupy(self, turn_color):
##        """temporary occupy for check situations"""
##        self.occupied = True
##        self.piece_color = turn_color

    def abandoned(self):
        """when a piece leaves a square"""
        self.occupied = False
        self.piece_color = ""
        
    def checkOccupied(self):
        """returns if the square is occupied and the piece color"""
        return self.occupied, self.piece_color

    def getCurrentPiece(self):
        """returns the occupying piece"""
        return self.piece

    def IDNumber(self, coord_pair):
        """sets square ID to a coordinate pair"""
        self.ID = coord_pair

    def getID(self):
        """returns ID"""
        return self.ID

    def flipPiece(self, turn_color):
        self.piece_color = turn_color
        self.piece.changeColor(turn_color)
