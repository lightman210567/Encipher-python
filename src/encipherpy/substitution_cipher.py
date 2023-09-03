try: # attempt a relative import of the required modules
    from ._string_number_convert import _stringToNumbers as stringToNumbers
    from ._string_number_convert import _numbersToString as numbersToString
    from ._punctuation import _detectPunctuation as detectPunctuation
    from ._punctuation import _removePunctuation as removePunctuation
    from ._punctuation import _restorePunctuation as restorePunctuation
except: # if relative import fails, use a direct import instead
    from _string_number_convert import _stringToNumbers as stringToNumbers
    from _string_number_convert import _numbersToString as numbersToString
    from _punctuation import _detectPunctuation as detectPunctuation
    from _punctuation import _removePunctuation as removePunctuation
    from _punctuation import _restorePunctuation as restorePunctuation

def substitutionCipher(plainText, cipherAlphabet):
    punctuation = detectPunctuation(plainText)
    plainText = removePunctuation(plainText, punctuation)

    numberText = stringToNumbers(plainText)
    cipherLetters = []

    for number in numberText:
        if number == 1000:
            cipherLetters.append(" ")
        elif number == 1001: # check for punctuation placeholders
            cipherLetters.append("#")
        else:
            cipherLetter = cipherAlphabet[number]
            cipherLetters.append(cipherLetter)

    cipherText = "".join(cipherLetters)
    cipherText = restorePunctuation(cipherText, punctuation)
    return cipherText