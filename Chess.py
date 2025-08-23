#these are only used for the displays
bPiecesUnicode = ["\u265A","\u265B","\u265C","\u265D","\u265E","\u265F"]
#display unicode white chess pieces with expandtabs
bPieces = {
    "King":   f"{bPiecesUnicode[0]}\t".expandtabs(2),
    "Queen":  f"{bPiecesUnicode[1]}\t".expandtabs(2),
    "Rook":   f"{bPiecesUnicode[2]}\t".expandtabs(2),
    "Bishop": f"{bPiecesUnicode[3]}\t".expandtabs(2),
    "Knight": f"{bPiecesUnicode[4]}\t".expandtabs(2),
    "Pawn":   f"{bPiecesUnicode[5]}\t".expandtabs(2)
}
wPiecesUnicode = ["\u2654","\u2655","\u2656","\u2657","\u2658","\u2659" ]
#display unicode white chess pieces with expandtabs
wPieces = {
    "King":   f"{wPiecesUnicode[0]}\t".expandtabs(2),
    "Queen":  f"{wPiecesUnicode[1]}\t".expandtabs(2),
    "Rook":   f"{wPiecesUnicode[2]}\t".expandtabs(2),
    "Bishop": f"{wPiecesUnicode[3]}\t".expandtabs(2),
    "Knight": f"{wPiecesUnicode[4]}\t".expandtabs(2),
    "Pawn":   f"{wPiecesUnicode[5]}\t".expandtabs(2)
}
#chess board 8x8
boardSize = [8,8]

#chess pieces including initial notation names
wBoardPiecesDictionary = {"wKing":"K", "wQueen":"Q", "wRook":"R", "wBishop":"B", "wKnight":"N", "wPawn": "P"}
bBoardPiecesDictionary = {"bKing":"K", "bQueen":"Q", "bRook":"R", "bBishop":"B", "bKnight":"N", "bPawn": "P"}

#chess pieces
wBoardPieces = ["wKing", "wQueen", "wRook", "wBishop", "wKnight", "wPawn"]
bBoardPieces = ["bKing", "bQueen", "bRook", "bBishop", "bKnight", "bPawn"]


#all square position notations of chess board
squares = [
    ["a8","b8","c8","d8","e8","f8","g8","h8"],
    ["a7","b7","c7","d7","e7","f7","g7","h7"],
    ["a6","b6","c6","d6","e6","f6","g6","h6"],
    ["a5","b5","c5","d5","e5","f5","g5","h5"],
    ["a4","b4","c4","d4","e4","f4","g4","h4"],
    ["a3","b3","c3","d3","e3","f3","g3","h3"],
    ["a2","b2","c2","d2","e2","f2","g2","h2"],
    ["a1","b1","c1","d1","e1","f1","g1","h1"]
]

#used to link the current loopPosition of for loop to chess pieces
piecesPositionsDictionary = {"":""}
piecesPositionsDictionary.pop("")
#used to link the current loopPosition of for loop to all the squares in the board
squaresDictionary = {"":""}
squaresDictionary.pop("")
#used to link all squares with chess piece to their current squares and also specify the piece notation in current square
squaresWithPiecesAndnotations = {"":""}
squaresWithPiecesAndnotations.pop("")
#for loop's current position(used for linking in piecesPositionsDictionary)
loopPosition = complex
#chess pieces locations with notations(whole board)
chessPiecesLocationsWithNotations = {"":""}
chessPiecesLocationsWithNotations.pop("")

#This function displays the initial chess board
def initialDisplay():
    #this is the linked squares of each pieces in the board, continuously updating each move
    chessPiecesLocationsWithNotations = [{'a8': 'Ra8', 'b8': 'Nb8', 'c8': 'Bc8', 'd8': 'Qd8','e8': 'Ke8', 'f8': 'Bf8', 'g8': 'Ng8', 'h8': 'Rh8'},
         {'a7': 'Pa7', 'b7': 'Pb7', 'c7': 'Pc7', 'd7': 'Pd7', 'e7': 'Pe7', 'f7': 'Pf7', 'g7': 'Pg7', 'h7': 'Ph7'},
         {'a6': '', 'b6': '', 'c6': '', 'd6': '', 'e6': '', 'f6': '', 'g6': '', 'h6': ''},
         {'a5': '', 'b5': '', 'c5': '', 'd5': '', 'e5': '', 'f5': '', 'g5': '', 'h5': ''},
         {'a4': '', 'b4': '', 'c4': '', 'd4': '', 'e4': '', 'f4': '', 'g4': '', 'h4': ''},
         {'a3': '', 'b3': '', 'c3': '', 'd3': '', 'e3': '', 'f3': '', 'g3': '', 'h3': ''},
         {'a2': 'Pa2', 'b2': 'Pb2', 'c2': 'Pc2', 'd2': 'Pd2', 'e2': 'Pe2', 'f2': 'Pf2', 'g2': 'Pg2', 'h2': 'Ph2'},
         {'a1': 'Ra1', 'b1': 'Nb1', 'c1': 'Bc1', 'd1': 'Qd1', 'e1': 'Ke1', 'f1': 'Bf1', 'g1': 'Ng1', 'h1': 'Rh1'}]
    
    for i in range(boardSize[0]):
        for key, value in chessPiecesLocationsWithNotations[i].items():
            if value.isalnum():
                print(value, end = "")
            else:
                print("",end = "")
        print()
    

initialDisplay()


