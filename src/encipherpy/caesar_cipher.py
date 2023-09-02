try: # attempt a relative import of the required modules
  from ._string_number_convert import _stringToNumbers as stringToNumbers
  from ._string_number_convert import _numbersToString as numbersToString
except: # if relative import fails, use a direct import instead
  from _string_number_convert import _stringToNumbers as stringToNumbers
  from _string_number_convert import _numbersToString as numbersToString

def caesarCipher(plainText, key, encrypt = True):
  numberText = stringToNumbers(plainText)
  cipherNumbers = []

  for number in numberText:
    if number == 1000:
      cipherNumbers.append(1000)
    else:
      if encrypt:
        shiftedNumber = (number + key) % 26
      else:
        shiftedNumber = (number - key) % 26
      cipherNumbers.append(shiftedNumber)

  cipherText = numbersToString(cipherNumbers)
  return cipherText
