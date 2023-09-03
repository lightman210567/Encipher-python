try: # attempt a relative import of the required modules
    from ._string_number_convert import _stringToNumbers as stringToNumbers
    from ._string_number_convert import _numbersToString as numbersToString
except: # if relative import fails, use a direct import instead
    from _string_number_convert import _stringToNumbers as stringToNumbers
    from _string_number_convert import _numbersToString as numbersToString

def substitutionCipher(plainText, cipherAlphabet):
    numberText = stringToNumbers(plainText)
    cipherLetters = []

    for number in numberText:
        if number == 1000:
            cipherLetters.append(" ")
        else:
            cipherLetter = cipherAlphabet[number]
            cipherLetters.append(cipherLetter)

    cipherText = "".join(cipherLetters)
    return cipherText