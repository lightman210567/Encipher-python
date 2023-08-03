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

def vigenereCipher(plainText, key):
  plainTextLength = len(plainText)
  keyLength = len(key)

  if plainTextLength > keyLength:
    extendKey(plainTextLength, key)