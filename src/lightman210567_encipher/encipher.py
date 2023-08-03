def extendKey(targetLength, key):
  difference = targetLength - len(key)
  keyList = list(key)
  keyBoundary = (len(key) - 1)

  keyPosition = 0
  while difference > 0:
    keyToAdd = key[keyPosition]
    keyList.append(keyToAdd)
    difference -= 1

    if keyPosition == keyBoundary:
      keyPosition = 0
    else:
      keyPosition += 1
  return "".join(keyList)

def stringToNumbers(string):
  alphabet = " abcdefghijklmnopqrstuvwxyz"
  numberList = []
  for letter in string:
    number = alphabet.find(letter)
    numberList.append(number)
  return numberList

def numbersToString(numbers):
  alphabet = " abcdefghijklmnopqrstuvwxyz"
  letterList = []
  for number in numbers:
    letter = alphabet[int(number)]
    letterList.append(letter)
  return "".join(letterList)

def vigenereCipher(plainText, key):
  plainTextLength = len(plainText)
  keyLength = len(key)

  if plainTextLength > keyLength:
    extendKey(plainTextLength, key)