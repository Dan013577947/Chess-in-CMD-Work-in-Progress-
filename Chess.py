#these are only used for the displays
bPiecesUnicode = ["\u265A","\u265B","\u265C","\u265D","\u265E","\u265F"]
#display unicode white chess pieces with expandtabs
bPieces = {
    "King":   f"{bPiecesUnicode[0]}".center(2),
    "Queen":  f"{bPiecesUnicode[1]}".center(2),
    "Rook":   f"{bPiecesUnicode[2]}".center(2),
    "Bishop": f"{bPiecesUnicode[3]}".center(2),
    "Knight": f"{bPiecesUnicode[4]}".center(2),
    "Pawn":   f"{bPiecesUnicode[5]}".center(2)
}
wPiecesUnicode = ["\u2654","\u2655","\u2656","\u2657","\u2658","\u2659" ]
#display unicode white chess pieces with expandtabs
wPieces = {
    "King":   f"{wPiecesUnicode[0]}".center(2),
    "Queen":  f"{wPiecesUnicode[1]}".center(2),
    "Rook":   f"{wPiecesUnicode[2]}".center(2),
    "Bishop": f"{wPiecesUnicode[3]}".center(2),
    "Knight": f"{wPiecesUnicode[4]}".center(2),
    "Pawn":   f"{wPiecesUnicode[5]}".center(2)
}
#this is the linked squares of each pieces in the board, continuously updating each move
chessPiecesLocationsWithNotations = {'a8': 'WRa8', 'b8': 'WNb8', 'c8': 'WBc8', 'd8': 'WQd8','e8': 'WKe8', 'f8': 'WBf8', 'g8': 'WNg8', 'h8': 'WRh8',
     'a7': '', 'b7': '', 'c7': 'WPc7', 'd7': 'WPd7', 'e7': 'WPe7', 'f7': 'WPf7', 'g7': 'WPg7', 'h7': 'WPh7',
     'a6': '', 'b6': '', 'c6': '', 'd6': '', 'e6': '', 'f6': '', 'g6': '', 'h6': '',
     'a5': '', 'b5': '', 'c5': '', 'd5': '', 'e5': '', 'f5': '', 'g5': '', 'h5': '',
     'a4': '', 'b4': '', 'c4': 'WPb7', 'd4': '', 'e4': '', 'f4': '', 'g4': '', 'h4': '',
     'a3': 'WPa7', 'b3': '', 'c3': '', 'd3': '', 'e3': '', 'f3': '', 'g3': '', 'h3': '',
     'a2': 'BPa2', 'b2': 'BPb2', 'c2': 'BPc2', 'd2': 'BPd2', 'e2': 'BPe2', 'f2': 'BPf2', 'g2': 'BPg2', 'h2': 'BPh2',
     'a1': 'BRa1', 'b1': 'BNb1', 'c1': 'BBc1', 'd1': 'BQd1', 'e1': 'BKe1', 'f1': 'BBf1', 'g1': 'BNg1', 'h1': 'BRh2'}
#this is used to save the old chessPiecesLocationsWithNotations(before the move was applied)
oldChessPiecesLocationsWithNotations ={}
#chess board 8x8
boardSize = [8,8]
#chess pieces linked with respective icons/image based on Capital letters (black and white)
chessBlackPiecesIcons = {"BK":bPieces["King"], "BQ":bPieces["Queen"], "BR":bPieces["Rook"], "BB":bPieces["Bishop"], "BN":bPieces["Knight"], "BP": bPieces["Pawn"]}
chessWhitePiecesIcons = {"WK":wPieces["King"], "WQ":wPieces["Queen"], "WR":wPieces["Rook"], "WB":wPieces["Bishop"], "WN":wPieces["Knight"], "WP": wPieces["Pawn"]}
#This function displays the initial chess board


def chessPiecesLocationsWithNotationsFunction():
    
    #used to display the board with pieces, this updates continuously
    for chessPiecesLocationsWithNotationsKey, chessPiecesLocationsWithNotationsValue in chessPiecesLocationsWithNotations.items():
        """detects whether there is a piece in the square, if there's capital
        letter then there's a piece. And also detects whether the piece is black or white"""
        if  chessPiecesLocationsWithNotationsValue != "":
            if chessPiecesLocationsWithNotationsValue[0] == "W" and chessPiecesLocationsWithNotationsValue[1].isupper():
                #white pieces displays/images
                for chessWhitePiecesIconsKey, chessWhitePiecesIconsValue in chessWhitePiecesIcons.items():
                    if chessPiecesLocationsWithNotationsValue[:2] == chessWhitePiecesIconsKey:
                        print(chessWhitePiecesIconsValue, end = "")
            elif chessPiecesLocationsWithNotationsValue[0] == "B" and chessPiecesLocationsWithNotationsValue[1].isupper():
                #black pieces displays/images
                for chessBlackPiecesIconsKey, chessBlackPiecesIconsValue in chessBlackPiecesIcons.items():
                    if chessPiecesLocationsWithNotationsValue[:2] == chessBlackPiecesIconsKey:
                        print(chessBlackPiecesIconsValue, end = "")
        #this is the display for squares without pieces
        else:
            print(" ".center(2),end = "")
        #this is used to make the board 8x8, not just horizontal
        if "h" in chessPiecesLocationsWithNotationsKey:
            print()
        else:
            print(end = "")
    move = str(input())
    
    return move

#the storage of all the possible moves of each white pieces(B was used here because CMD has black background and
#it makes the colors of the pieces opposite)
allPossibleMovesOfEachWhitePieces = {"BK": {}, "BQ": {}, "BR": {}, "BB": {}, "BN": {}, "BP": {}}
#the storage of all the possible moves of each black pieces(W was used here because CMD has black background and
#it makes the colors of the pieces opposite)
allPossibleMovesOfEachBlackPieces = {"WK": {}, "WQ": {}, "WR": {}, "WB": {}, "WN": {}, "WP": {}}
#lists of all letters and numbers of squares inside the board
letters = ["a","b","c","d","e","f","g","h"]
numbers = [1,2,3,4,5,6,7,8]
#used to declare the allPossibleMovesOfEachWhitePieces["BR"][oldPost] as a list, so it can be appended
allPossibleMovesOfEachWhitePiecesRookCounter=0
def boardMovements(move):
    
    count = 0
    #this detects if the move of the plalyer is included in all the possible legal moves in the current board
    for allPossibleMovesOfEachWhitePiecesKey, allPossibleMovesOfEachWhitePiecesValue in allPossibleMovesOfEachWhitePieces.items():
        origRookPosition = []
        #this detects all possible moves from every pieces in the current position in the chess board
        for chessPiecesLocationsWithNotationsKey, chessPiecesLocationsWithNotationsValue in chessPiecesLocationsWithNotations.items():
            """
            this saves the pieces positions before the move of the player was implemented 
            simple equation oldChessPiecesLocationsWithNotations = chessPiecesLocationsWithNotations don't work so needed to use for loop
            """
            oldChessPiecesLocationsWithNotations.update({chessPiecesLocationsWithNotationsKey:chessPiecesLocationsWithNotationsValue})
            #all possible moves for WHITE PAWNS
            if "B" in chessPiecesLocationsWithNotationsValue and "P" in chessPiecesLocationsWithNotationsValue:
                #used to store the current positions of each pieces which will be manipulated
                squareDigit, squareLetter, targetPosition = "","",""
                for x in chessPiecesLocationsWithNotationsKey:
                    if x.islower():
                        squareLetter = x
                    if x.isdigit():
                        squareDigit = str(x)   
                #handles the logic to detect each possible moves in current position, 
                if squareLetter and squareDigit:
                    
                    #1 step above
                    targetSquareDigit = int(squareDigit) + 1
                    #this if else make sure the pawns don't exceed the numbers od squares (1-8)included in the board
                    if targetSquareDigit in numbers:
                        oldPosition = squareLetter + str(squareDigit)
                        targetPosition = squareLetter + str(targetSquareDigit)
                        if chessPiecesLocationsWithNotations[targetPosition] == "":
                            """stores all the possible moves of all white pawns inside a list. The key in the
                            allPossibleMovesOfEachWhitePieces
                            dictionary will be the original position before the piece was moved"""
                            #needed to declare as empty list first before appending all the 2 squares +1 and + 2 square possible moves for each pawns
                            allPossibleMovesOfEachWhitePieces["BP"].update({oldPosition:[]})
                            #this appends all 2 squares (e2: [e3,e4], a2:[a3,a4]) to a list
                            allPossibleMovesOfEachWhitePieces["BP"][oldPosition].append(targetPosition)
                        #eating opponent chess piece
                        #LAST PART OF THE PROJECT, I DECIDED NOT TO CONTINUE TO FOCUS ON LEARNING PYTHON WEB LIBRARIES
                        """asciiCodeLeft,asciiCodeRight = ord(squareLetter) - 1,ord(squareLetter) + 1
                        convertCharLeft,convertCharRight = chr(asciiCodeLeft),chr(asciiCodeRight)
                        targetSquareLeft =  convertCharLeft+ str(targetSquareDigit)
                        targetSquareRight =  convertCharRight+ str(targetSquareDigit)
                        #print(chr(targetSquareLetterLeft) + str(targetSquareDigit), " -- ", chr(targetSquareLetterRight) + str(targetSquareDigit))
                        
                        if convertCharLeft in letters and convertCharRight in letters:
                            try:
                                if "W" in chessPiecesLocationsWithNotations[targetSquareLeft]:
                                
                                    allPossibleMovesOfEachWhitePieces["BP"][oldPosition].append(targetSquareLeft)
                               
                                    print(f"targetSquareLeft:{targetSquareLeft} -- oldPosition:{oldPosition}")
                                if "W" in chessPiecesLocationsWithNotations[targetSquareRight]:
                                    allPossibleMovesOfEachWhitePieces["BP"][oldPosition].append(targetSquareRight)
                                    
                                    print(f"targetSquareRight:{targetSquareRight} -- oldPosition:{oldPosition}")
                            except:
                                print(allPossibleMovesOfEachWhitePieces["BP"][oldPosition])"""
                    #2 step above (onlhy applicable if the pawn is at the starting position)
                    if squareDigit == "2":
                        #this detects which square in the current board has a chess piece in the way of the pawn
                        listOfKey, listOfValue, occupiedSquare= [],[],""
                        for key,value in allPossibleMovesOfEachWhitePieces.items():
                            for keyy,valuee in allPossibleMovesOfEachWhitePieces[key].items():
                                listOfKey.append(keyy)
                                for v in valuee:
                                    listOfValue.append(v)
                                    
                        listOfKey,listOfValue = list(set(listOfKey)), list(set(listOfValue))
                        #if there is a piece that blocks the path of the pawn, its square will be stored in occupiedSquare
                        for x in listOfKey:
                            if x in listOfValue:
                                occupiedSquare = x
                        #the targeted square will only be added in the list allPossibleMovesOfEachWhitePieces if it's currently empty (no one occupies)
                        if chessPiecesLocationsWithNotations[targetPosition] == "":
                            for x in targetPosition:
                                if x.isdigit():
                                    squareDigit = int(x)+1
                                if x.islower():
                                    squareLetter = x
                                if squareLetter and squareDigit and squareDigit != "2":
                                    targetPosition = squareLetter + str(squareDigit)
                                if targetPosition not in allPossibleMovesOfEachWhitePieces["BP"][oldPosition]:
                                    allPossibleMovesOfEachWhitePieces["BP"][oldPosition].append(targetPosition)
                        #fixed the problem such as rook on Rh3 but still can do h4 for pawn
                        for key, value in allPossibleMovesOfEachWhitePieces["BP"].items():
                            if occupiedSquare in value:
                                allPossibleMovesOfEachWhitePieces["BP"].update({key:[]})
            #all possible moves for White Rooks
            if "B" in chessPiecesLocationsWithNotationsValue and "R" in chessPiecesLocationsWithNotationsValue:
               
                #made the 2 squares of rook be inside a list (a1,h1)
                origRookPosition.append(chessPiecesLocationsWithNotationsKey)
                if len(origRookPosition) == 2:
                    #a1, h1
                    for eachOrigRookPosition in origRookPosition:
                        targetLetter,targetDigit = [],[]
                        #loops each a,1 and h,1
                        for x in eachOrigRookPosition:
                            if x.islower():
                                for xLetters in letters:
                                    if str(x)!=str(xLetters):
                                        #here stores all the letters except the origLetter (b,c,d,e,f,g,h)..and such
                                        targetLetter.append(xLetters)
                                    else:
                                        #here stores the origLetter -> a,h and such
                                        origLetter = xLetters
                            if x.isdigit():
                                for xNumbers in numbers:
                                    if str(x)!=str(xNumbers):
                                        #here stores all the letters except the origLetter (2,3,4,5,6,7,8)..and such
                                        targetDigit.append(xNumbers)
                                    else:
                                        #here stores the origDigit -> 1 and such
                                        origDigit = xNumbers
                            
                            if targetLetter and targetDigit:
                                targetPositionLetters, targetPositionDigits  = [],[]
                                for x in targetDigit:
                                    targetPositionDigits.append(str(origLetter) + str(x))
                                for x in targetLetter:
                                    targetPositionLetters.append(str(x) + str(origDigit))
                                #try and except helps handle errors usually in appending the list in dictionary chessPiecesLocationsWithNotations
                                allPossibleMovesOfEachWhitePieces["BR"].update({eachOrigRookPosition:[]})
                                #used to fix the problem regarding Rooks jumping white piece
                                withBDigit, withBLetter,squaresWithBDigit,squaresWithBDigitLowest,squaresWithBLetter,squaresWithBLetterLowest = "","",[],"",[],""
                                #this fixed the problem regarding rooks can jump on pawns below them (Ra4 can go Ra1 even pawn on a2 is present), and such
                                for x in targetPositionDigits:
                                    #for y in chessPiecesLocationsWithNotations[x]:
                                        #print(f"x:{x} -- y:{y}")
                                       # print(f"chessPiecesLocationsWithNotations[x]:{chessPiecesLocationsWithNotations[x]}")
                                    if "B" in chessPiecesLocationsWithNotations[x] and "BR" not in chessPiecesLocationsWithNotations[x]:
                                        squaresWithBDigit.append(x)
                                for x in squaresWithBDigit:
                                    if squaresWithBDigitLowest < x and squaresWithBDigitLowest == "":
                                        squaresWithBDigitLowest = x
                                    
                                #print(f"squaresWithBDigitLowest:{squaresWithBDigitLowest} -- eachOrigRookPosition:{eachOrigRookPosition}")
                                #targetPositionDigits (a1,a2,a3,a4,a5,a6,a7,a8) and such
                                for x in targetPositionDigits:
                                    targetPositionRook = "R"+x
                                    #include the target square in the list if it's an empty square or there's enemy piece which can be eaten
                                    if chessPiecesLocationsWithNotations[x] == "" or "W" in chessPiecesLocationsWithNotations[x]:
                                        #print(f"1 - eachOrigRookPosition:{eachOrigRookPosition}--withBDigit:{withBDigit} -- x:{x}")
                                        if targetPositionRook not in allPossibleMovesOfEachWhitePieces["BR"][eachOrigRookPosition] and withBDigit == "":
                                            #print(f"2 - eachOrigRookPosition:{eachOrigRookPosition}--withBDigit:{withBDigit} -- x:{x}")
                                           
                                            if eachOrigRookPosition > squaresWithBDigitLowest :
                                                if x > squaresWithBDigitLowest:
                                                    #if "Rh2" in allPossibleMovesOfEachWhitePieces["BR"][eachOrigRookPosition]:
                                                        
                                                        #print(f"1 -- targetPositionRook:{targetPositionRook} -- squaresWithBDigitLowest:{squaresWithBDigitLowest} -- squaresWithBLetterLowest:{squaresWithBLetterLowest} -- eachOrigRookPosition:{eachOrigRookPosition} -- withBDigit:{withBDigit} -- withBLetter:{withBLetter}")

                                                    allPossibleMovesOfEachWhitePieces["BR"][eachOrigRookPosition].append(targetPositionRook)
                                            else:
                                                #if "Rh2" in allPossibleMovesOfEachWhitePieces["BR"][eachOrigRookPosition]:
                                                    
                                                    #print(f"2 -- targetPositionRook:{targetPositionRook} -- squaresWithBDigitLowest:{squaresWithBDigitLowest} -- squaresWithBLetterLowest:{squaresWithBLetterLowest} -- eachOrigRookPosition:{eachOrigRookPosition} -- withBDigit:{withBDigit} -- withBLetter:{withBLetter}")

                                                allPossibleMovesOfEachWhitePieces["BR"][eachOrigRookPosition].append(targetPositionRook)
                                           
                                        else:
                                            #print(f"3 - eachOrigRookPosition:{eachOrigRookPosition}--withBDigit:{withBDigit} -- x:{x}")
                                            if eachOrigRookPosition < withBDigit:
                                                if x < withBDigit:
                                                    #if "Rh2" in allPossibleMovesOfEachWhitePieces["BR"][eachOrigRookPosition]:
                                                        #print(f"3 -- targetPositionRook:{targetPositionRook} -- squaresWithBDigitLowest:{squaresWithBDigitLowest} -- squaresWithBLetterLowest:{squaresWithBLetterLowest} -- eachOrigRookPosition:{eachOrigRookPosition} -- withBDigit:{withBDigit} -- withBLetter:{withBLetter}")

                                                   # print(f"4 - eachOrigRookPosition:{eachOrigRookPosition}--withBDigit:{withBDigit} -- x:{x}")
                                                    allPossibleMovesOfEachWhitePieces["BR"][eachOrigRookPosition].append(targetPositionRook)
                                                    if "W" in chessPiecesLocationsWithNotations[x]:
                                                        break
                                                
                                            else:
                                               
                                                if x > withBDigit:
                                                    #if "Rh2" in allPossibleMovesOfEachWhitePieces["BR"][eachOrigRookPosition]:
                                                        #print(f"4 -- targetPositionRook:{targetPositionRook} -- squaresWithBDigitLowest:{squaresWithBDigitLowest} -- squaresWithBLetterLowest:{squaresWithBLetterLowest} -- eachOrigRookPosition:{eachOrigRookPosition} -- withBDigit:{withBDigit} -- withBLetter:{withBLetter}")

                                                   # print(f"5 - eachOrigRookPosition:{eachOrigRookPosition}--withBDigit:{withBDigit} -- x:{x}")
                                                    allPossibleMovesOfEachWhitePieces["BR"][eachOrigRookPosition].append(targetPositionRook)
                                                    if "W" in chessPiecesLocationsWithNotations[x]:
                                                        break
                                                
                                    elif "B" in chessPiecesLocationsWithNotations[x]:
                                        """if "BR" not in chessPiecesLocationsWithNotations[x]: fixed the error regarding when 2
                                        rooks on the same number meet
                                        and there's a black piece between them, the above rook returns error when it jumps the black piece"""
                                        if "BR" not in chessPiecesLocationsWithNotations[x]:
                                            withBDigit = x
                                                                            
                                for x in targetPositionLetters:
                                    #for y in chessPiecesLocationsWithNotations[x]:
                                        #print(f"x:{x} -- y:{y}")
                                    if "B" in chessPiecesLocationsWithNotations[x] and "BR" not in chessPiecesLocationsWithNotations[x]:
                                        squaresWithBLetter.append(x)
                                    
                                for x in squaresWithBLetter:
                                    if squaresWithBLetterLowest < x and squaresWithBLetterLowest == "":
                                        squaresWithBLetterLowest = x
                                    
                                #print(f"squaresWithBLetterLowest:{squaresWithBLetterLowest} -- eachOrigRookPosition:{eachOrigRookPosition}")
                                
                                #targetPositionDigits (a1,b1,c1,d1,e1,f1,g1,h1) and such
                                for x in targetPositionLetters:
                                    #print(f"x:{x} -- withBLetter:{withBLetter}")
                                    targetPositionRook = "R"+x
                                    #include the target square in the list if it's an empty square or there's enemy piece which can be eaten
                                    if chessPiecesLocationsWithNotations[x] == "" or "W" in chessPiecesLocationsWithNotations[x]:
                                        #print(f"6 - eachOrigRookPosition:{eachOrigRookPosition}--withBLetter:{withBLetter} -- x:{x}")
                                        if targetPositionRook not in allPossibleMovesOfEachWhitePieces["BR"][eachOrigRookPosition] and withBLetter == "":
                                            #print(f"7 - eachOrigRookPosition:{eachOrigRookPosition}--withBLetter:{withBLetter} -- x:{x}")
                                            
                                            if eachOrigRookPosition > squaresWithBLetterLowest :
                                                if x > squaresWithBLetterLowest:
                                                    #if "Rh2" in allPossibleMovesOfEachWhitePieces["BR"][eachOrigRookPosition]:
                                                        #print(f"5 -- targetPositionRook:{targetPositionRook} -- squaresWithBDigitLowest:{squaresWithBDigitLowest} -- squaresWithBLetterLowest:{squaresWithBLetterLowest} -- eachOrigRookPosition:{eachOrigRookPosition} -- withBDigit:{withBDigit} -- withBLetter:{withBLetter}")

                                                    allPossibleMovesOfEachWhitePieces["BR"][eachOrigRookPosition].append(targetPositionRook)
                                            else:
                                                #if "Rh2" in allPossibleMovesOfEachWhitePieces["BR"][eachOrigRookPosition]:
                                                    #print(f"6 -- targetPositionRook:{targetPositionRook} -- squaresWithBDigitLowest:{squaresWithBDigitLowest} -- squaresWithBLetterLowest:{squaresWithBLetterLowest} -- eachOrigRookPosition:{eachOrigRookPosition} -- withBDigit:{withBDigit} -- withBLetter:{withBLetter}")

                                                allPossibleMovesOfEachWhitePieces["BR"][eachOrigRookPosition].append(targetPositionRook)
                                        else:
                                            #print(f"8 - eachOrigRookPosition:{eachOrigRookPosition}--withBLetter:{withBLetter} -- x:{x}")
                                            if eachOrigRookPosition < withBLetter:
                                                if x < withBLetter:
                                                    #p#rint(f"9 - eachOrigRookPosition:{eachOrigRookPosition}--withBLetter:{withBLetter} -- x:{x}")
                                                    #if "Rh2" in allPossibleMovesOfEachWhitePieces["BR"][eachOrigRookPosition]:
                                                        #print(f"7 -- targetPositionRook:{targetPositionRook} -- squaresWithBDigitLowest:{squaresWithBDigitLowest} -- squaresWithBLetterLowest:{squaresWithBLetterLowest} -- eachOrigRookPosition:{eachOrigRookPosition} -- withBDigit:{withBDigit} -- withBLetter:{withBLetter}")

                                                    allPossibleMovesOfEachWhitePieces["BR"][eachOrigRookPosition].append(targetPositionRook)
                                                    if "W" in chessPiecesLocationsWithNotations[x]:
                                                        break
                                            else:
                                                if x > withBLetter:
                                                    #print(f"10 - eachOrigRookPosition:{eachOrigRookPosition}--withBLetter:{withBLetter} -- x:{x}")
                                                    #if "Rh2" in allPossibleMovesOfEachWhitePieces["BR"][eachOrigRookPosition]:
                                                        #print(f"8 -- targetPositionRook:{targetPositionRook} -- squaresWithBDigitLowest:{squaresWithBDigitLowest} -- squaresWithBLetterLowest:{squaresWithBLetterLowest} -- eachOrigRookPosition:{eachOrigRookPosition} -- withBDigit:{withBDigit} -- withBLetter:{withBLetter}")

                                                    allPossibleMovesOfEachWhitePieces["BR"][eachOrigRookPosition].append(targetPositionRook)
                                                    if "W" in chessPiecesLocationsWithNotations[x]:
                                                        break
                                    elif "B" in chessPiecesLocationsWithNotations[x]:
                                        """if "BR" not in chessPiecesLocationsWithNotations[x]: fixed the error regarding when 2
                                        rooks on the same number meet
                                        and there's a black piece between them, the above rook returns error when it jumps the black piece"""
                                        if "BR" not in chessPiecesLocationsWithNotations[x]:
                                            withBLetter = x
                    #print(f"allPossibleMovesOfEachWhitePieces['BR'][origRookPosition[0]]:{allPossibleMovesOfEachWhitePieces['BR'][origRookPosition[0]]} -- allPossibleMovesOfEachWhitePieces['BR'][origRookPosition[1]]:{allPossibleMovesOfEachWhitePieces['BR'][origRookPosition[1]]}")
                    #this handles the error when both 2 rooks can go to a square which confuses the system 
                    doubleSquareRook = []
                    for x in allPossibleMovesOfEachWhitePieces['BR'][origRookPosition[0]]:
                        if x in allPossibleMovesOfEachWhitePieces['BR'][origRookPosition[1]]:
                            doubleSquareRook.append(x)
                            count = 0
        
        #this handles the error when both 2 rooks can go to a square which confuses the system 
        if move in doubleSquareRook and move != "":
            if count == 0:
                chosenRookPositionList,chosenRookPosition,chosenTargetSquareRookList,chosenTargetSquareRook = [],"",[],""
                chosenRook = input("Which Rook: ")
                for x in chosenRook:
                    if not x.isupper():
                        chosenRookPositionList.append(x)
                for x in move:
                    if not x.isupper():
                        chosenTargetSquareRookList.append(x)
                    
                if len(chosenRookPositionList) != 1:
                    chosenRookPosition = "".join(chosenRookPositionList)
                if len(chosenTargetSquareRookList) != 1:
                    chosenTargetSquareRook = "".join(chosenTargetSquareRookList)
                doubleSquareRookWithAnnotation = "B" + move
                #print(f"chosenRookPosition:{chosenRookPosition} -- doubleSquareRook:{doubleSquareRook}")
                if chosenRookPosition in origRookPosition:
                    #this updates the display in relevant with doubleSquareRook
                    chessPiecesLocationsWithNotations.update({chosenRookPosition:""})
                    chessPiecesLocationsWithNotations.update({chosenTargetSquareRook:doubleSquareRookWithAnnotation})
                count = 1
        else:            
                            
            #used to store the current positions of each pieces which will be manipulated
            pieceLetters, squarePosition = [],[]
            #this handles the updating of the piece images and the deletion of the piece images left out after the move was implemented
            for allPossibleMovesOfEachWhitePiecesValueKey,allPossibleMovesOfEachWhitePiecesValueValue in allPossibleMovesOfEachWhitePiecesValue.copy().items():
                if move in allPossibleMovesOfEachWhitePiecesValueValue:
                    
                    #print(f"move:{move}|allPossibleMovesOfEachWhitePiecesValueValue:{allPossibleMovesOfEachWhitePiecesValueValue}")
                    for x in allPossibleMovesOfEachWhitePiecesKey:
                        if x.isupper():
                            pieceLetters.append(x)
                    for x in move:
                        #print(f"squarePosition:{squarePosition}, x:{x}")
                        if not x.isupper():
                            squarePosition.append(x)
                    if pieceLetters and squarePosition:
                        targetMoveWithAnnotation = "".join(pieceLetters + squarePosition)
                        #this makes the list the pieceLettters and squarePosition be string
                        squarePosition = "".join(squarePosition)
                        pieceLetters = "".join(pieceLetters)
                        
                        
                        #this updates the display of the pieces when the move was implemented
                        chessPiecesLocationsWithNotations.update({squarePosition:targetMoveWithAnnotation})
                        #this makes the piece's left square "" after the move was implemented																#
                        #                                                                                                           NOTE!!: .copy fixed the error regarding the "runtime error,
                        #                                                                                                               sized changed of dictionary during iteration
                        for allPossibleMovesOfEachWhitePiecesKey, allPossibleMovesOfEachWhitePiecesValue in allPossibleMovesOfEachWhitePieces[pieceLetters].copy().items():
                            #added this for loop to get access to all values inside the key (a2:[a3,a4], b2:[b3,b4]..etc)
                            for allPossibleMovesOfEachWhitePiecesValueValue in allPossibleMovesOfEachWhitePiecesValue:
                                if move == allPossibleMovesOfEachWhitePiecesValueValue:
                                    #this makes the piece's left square "" after the move was implemented
                                    
                                    chessPiecesLocationsWithNotations.update({allPossibleMovesOfEachWhitePiecesKey: ""})
                                    """this deletes the stored possible move after the piece was moved to make sure
                                    the player can't use the same move again"""
                                    allPossibleMovesOfEachWhitePieces[pieceLetters].pop(allPossibleMovesOfEachWhitePiecesKey)
        
                   
                    
    
    print(allPossibleMovesOfEachWhitePieces)
while True:			
    boardMovements(chessPiecesLocationsWithNotationsFunction())
    
 
    
    
    
    
    
   













