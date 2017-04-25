# Othello AI


def maxDisks(tiles, turn_color, possibleMoves, blackPieceList, whitePieceList):

    if turn_color == "white":
        bestMove = ""
        lenlist = 0 
        for move in possibleMoves:
            if len(whitePieceList) > lenlist:
                lenlist = len(whitePieceList)
                bestMove = move

    if turn_color == "black":
        bestMove = ""
        lenlist = 0 
        for move in possibleMoves:
            if len(blackPieceList) > lenlist:
                lenlist = len(blackPieceList)
                bestMove = move


    return bestMove


def weightDisks(tiles, possibleMoves):

    weightList = [7,2,5,4,4,5,2,7,
                  2,1,3,3,3,3,1,2,
                  5,3,6,5,5,6,3,5,
                  4,3,5,6,6,5,3,4,
                  4,3,5,6,6,5,3,4,
                  5,3,6,5,5,6,3,5,
                  2,1,3,3,3,3,1,2,
                  7,2,5,4,4,5,2,7]

    for i in range (0,7):
        (tiles[0][i]).ID = weightList[i]
        (tiles[1][i]).ID = weightList[(i+8)]
        (tiles[2][i]).ID = weightList[(i+15)]
        (tiles[3][i]).ID = weightList[(i+22)]
        (tiles[4][i]).ID = weightList[(i+29)]
        (tiles[5][i]).ID = weightList[(i+36)]
        (tiles[6][i]).ID = weightList[(i+43)]
        (tiles[7][i]).ID = weightList[(i+50)]
        


    worst = 0
    bestmove = []
    for i in (0, len(possibleMoves)):
        coord = possibleMoves[i].ID
        if (tiles(coord[0], coord[1])).ID > worst:
            worst = (tiles(coord[0], coord[1])).ID
            x = coord[0]
            y = coord[1]

    bestmove.append(x)
    bestmove.append(y)

    return bestmove 

    

    



            
        
    

    # check the length of blackPieceList
    # white piece list
