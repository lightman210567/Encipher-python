def polybusSquare(plainText, encrypt = True):
    square = [
        ["a", "b", "c", "d", "e"],
        ["f", "g", "h", "i", "k"],
        ["l", "m", "n", "o", "p"],
        ["q", "r", "s", "t", "u"],
        ["v", "w", "x", "y", "z"]
    ]
    cipherText = []
    plainTextList = []

    # remove all spaces from the plain text
    for character in plainText:
        if character != " ":
            plainTextList.append(character)

    if encrypt == True:
        for letter in plainTextList:
            index = findInSquare(square, letter)
            cipherText.append(index)
    else:
        for i in range(0, len(plainTextList), 2):
            row = int(plainTextList[i]) - 1
            column = int(plainTextList[i + 1]) - 1
            letter = square[row][column]
            cipherText.append(letter)

    cipherText = "".join(cipherText)
    return cipherText
        
def findInSquare(square, targetLetter):
    for rowIndex, row in enumerate(square):
        for columnIndex, letter in enumerate(row):
            if letter == targetLetter:
                index = str(rowIndex + 1) + str(columnIndex + 1) # add 1 to each index to make them start at 1 instead of 0
                return index