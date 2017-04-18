## Othello Runner
from othelloAI import *
from graphics import *
from othelloGUI import *
from button_chang import *

def initPieces(win, tiles):
    loc1 = [3,3]
    loc2 = [4,4]
    loc3 = [3,4]
    loc4 = [4,3]
    whitePiece1 = Piece("white", loc1, win)
    whitePiece2 = Piece("white", loc2, win)
    blackPiece1 = Piece("black", loc3, win)
    blackPiece2 = Piece("black", loc4, win)

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


def findMoves(win, tiles, turn_color, opposite_color):
    turn_tiles = []

    # finding the tiles with pieces of corresponding turn
    for column in tiles:
        for square in column:
            if square.piece_color == turn_color:
                turn_tiles.append(square)

    # finding the possible moves from each piece
    possible_moves = []
    for square in turn_tiles:
        x = square.ID[0]
        y = square.ID[1]
        
        x_direction = [[x, 8, 1], [x, -1, -1]]
        y_direction = [[y, 8, 1], [y, -1, -1]]

        # checks going left and going right from the piece
        for direction in x_direction:
            step = direction[2]
            start_square = direction[0] + step
            max_square = direction[1]
            first_square = True
            for i in range(start_square, max_square, step):
                check_square = tiles[i][y]
                check_square.piece_color = color
                if color == turn_color:
                    break
                elif color == "":
                    if not first_square:
                        possible_moves.append(check_square)
                    break
                first_square = False

        for direction in y_direction:
            step = direction[2]
            start_square = direction[0] + step
            max_square = direction[1]
            first_square = True
            for i in range(start_square, max_square, step):
                check_square = tiles[x][i]
                check_square.piece_color = color
                if color == turn_color:
                    break
                elif color == "":
                    if not first_square:
                        possible_moves.append(check_square)
                    break
                first_square = False

        diagonals = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
        for direction in diagonals:
            x_step = direction[0]
            y_step = direction[1]
            x_test = x + x_step
            y_test = y + y_step
            if x_step > 0:
                x_max = 8
            else:
                x_max = -1
            if y_step > 0:
                y_max = 8
            else:
                y_max = -1

            first_square = True
            while x_test != x_max and y_test != y_max:
                check_square = tiles[x_test][y_test]
                check_square.piece_color = color
                if color == turn_color:
                    break
                elif color == "":
                    if not first_square:
                        possible_moves.append(check_square)
                    break
                first_square = False
                x_test += x_step
                y_test += y_step

def main():
    win = GraphWin("Othello", 1200, 800)
    tiles = createGrid(win)
    initPieces(win, tiles)
