def polybusSquare(plainText):
    square = [
        ["a", "b", "c", "d", "e"],
        ["f", "g", "h", "i", "k"],
        ["l", "m", "n", "o", "p"],
        ["q", "r", "s", "t", "u"],
        ["v", "w", "x", "y", "z"]
    ]
    cipherText = []

    for letter in plainText:
        if letter != " ":
            index = findInSquare(square, letter)
            cipherText.append(index)
        else:
            cipherText.append(" ")
    cipherText = "".join(cipherText)
    return cipherText
        
def findInSquare(square, targetLetter):
    for rowIndex, row in enumerate(square):
        for columnIndex, letter in enumerate(row):
            if letter == targetLetter:
                index = str(rowIndex + 1) + str(columnIndex + 1) # add 1 to each index to make them start at 1 instead of 0
                return index