try: # attempt a relative import of the required modules
  from ._string_number_convert import _stringToAscii as stringToAscii
  from ._string_number_convert import _asciiToString as asciiToString
except: # if relative import fails, use a direct import instead
  from _string_number_convert import _stringToAscii as stringToAscii
  from _string_number_convert import _asciiToString as asciiToString

# TODO rework rot47 code to use an alphabet string rather than mathematic operations
def rot47(plainText):
  asciiNumbers = stringToAscii(plainText)
  cipherNumbers = []

  for number in asciiNumbers:
    if number == 32:
      cipherNumbers.append(32)
    else:
      shiftedNumber = number + 47
      if shiftedNumber != 126:
        shiftedNumber = shiftedNumber % 126
      if shiftedNumber < 94:
        shiftedNumber = shiftedNumber + 32
      cipherNumbers.append(shiftedNumber)

  cipherText = asciiToString(cipherNumbers)
  return cipherText
