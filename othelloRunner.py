## Othello Runner

from graphics import *

def initPieces(win, locationList, message):
    whitePiece1 = Piece("white", location, 3, win)
    whitePiece2 = Piece("white", location, 4, win)
    blackPiece1 = Piece("black", location, 3, win)
    blackPiece2 = Piece("black", location, 4, win)

    blackPieceList = [blackPiece1, blackPiece2]
    whitePieceList = [whitePiece1, whitePiece2]
    pieceList = [whitePiece1, whitePiece2, blackPiece1, blackPiece2]

    
    


def currentPositions(pieceList):
	"""This method returns the current positions of all the pieces sent in through a list as a parameter."""

	# Appending all the locations of the objects in the list to an empty list.
	occupiedSpaces = []
	for piece in pieceList:
		occupiedSpaces.append(piece.getLocation())

	return occupiedSpaces
    
