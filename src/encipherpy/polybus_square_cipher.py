def polybusSquare(plainText, encrypt = True):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    square = [
        ["a", "b", "c", "d", "e"],
        ["f", "g", "h", "i", "k"],
        ["l", "m", "n", "o", "p"],
        ["q", "r", "s", "t", "u"],
        ["v", "w", "x", "y", "z"]
    ]
    cipherText = []

    if encrypt == True:
        for letter in plainText:
            if letter not in alphabet:
                cipherText.append(letter)
            else:
                index = findInSquare(square, letter)
                cipherText.append(index)
    else:
        for i in range(0, len(plainText), 2):
            if plainText[i] not in alphabet:
                cipherText.append(plainText[i])
            else:
                row = int(plainText[i]) - 1
                column = int(plainText[i + 1]) - 1
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