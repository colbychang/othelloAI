from button_chang import *
from graphics import *

def createGrid(win):
    """draws grid of 8x8 squares and the quit button and message board"""
    msg_board = Rectangle(Point(810, 10), Point(1190, 610))
    msg_board.draw(win)
    tiles = []
    
    # create 8 lists within tiles to be the columns of squares
    for i in range(8):
        tiles.append([])
        
        # create 8 squares per column going down vertically
        for j in range(8):

            new_square = Button(win, Point(i * 100 + 50, j * 100 + 50),
                                100, 100, "")
            new_square.setColor("forestgreen")
            tiles[i].append(new_square)

##            # checks if i + j is odd, fills in white or gray
##            if (i + j) % 2 == 0:
##                tiles[i][j].setColor("tan")
##            else:
##                tiles[i][j].setColor("brown")
    close_button = Button(win, Point(1100, 750), 75, 50, "Quit")
    close_button.activate("")
#    tiles.append(close_button) # MAYBE NOT DO THIS????
    return tiles

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
    win = GraphWin("Chess", 1200, 800)
    tiles = createGrid(win)
