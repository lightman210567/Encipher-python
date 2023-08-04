def extendKey(plainText, key):
  targetLength = len(plainText)
  difference = targetLength - len(key)
  keyList = list(key)
  keyBoundary = (len(key) - 1)

  i = len(key)
  keyPosition = 0
  while difference > 0:
    if plainText[i] == " ":
      keyToAdd = " "
    else:
      keyToAdd = key[keyPosition]
      if keyPosition == keyBoundary:
        keyPosition = 0
      else:
        keyPosition += 1
    keyList.append(keyToAdd)
    difference -= 1
    i += 1

  return "".join(keyList)

def stringToNumbers(string):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  numberList = []
  for letter in string:
    if letter == " ":
      number = 1000
    else:
      number = alphabet.find(letter)
    numberList.append(number)
  return numberList

def numbersToString(numbers):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  letterList = []
  for number in numbers:
    if number == 1000:
      letter = " "
    else:
      letter = alphabet[int(number)]
    letterList.append(letter)
  return "".join(letterList)

def vigenereCipher(plainText, key):
  plainTextLength = len(plainText)
  keyLength = len(key)
  if plainTextLength > keyLength:
    key = extendKey(plainText, key)

  numberList = stringToNumbers(plainText)
  numericKey = stringToNumbers(key)
  cipherNumbers = []
  
  for i in range(0, plainTextLength):
    plainNumber = numberList[i]
    shift = numericKey[i]

    if plainNumber == 1000:
      cipherNumbers.append(1000)
    else:
      shiftedNumber = (plainNumber + shift) % 26
      cipherNumbers.append(shiftedNumber)

  cipherText = numbersToString(cipherNumbers)
  return cipherText

test = vigenereCipher("this is a test of the vigenere cipher", "secure")
print(test)