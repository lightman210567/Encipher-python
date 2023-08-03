def vigenereCipher(plainText, key):
  plainTextLength = len(plainText)
  keyLength = len(key)

  # Check if the key is long enough for the plain text
  # If the key is not long enough, repeat the key until the text and key are equal lengths
  if plainTextLength > keyLength:
    difference = plainTextLength - keyLength

    keyList = list(key)
    keyBoundary = keyLength - 1

    keyPosition = 0
    # while the difference in length is not 0, append a part of the key to the end of the list
    # This repeats the key until the text and key have the same length
    while difference != 0:
      keyToAdd = keyList[keyPosition]
      keyList.append(keyToAdd)
      difference -= 1

      # Check if the last key part has been used.
      # If the key has been used, reset the position to start from the beginning.
      if keyPosition == keyBoundary:
        keyPosition = 0
      else:
        keyPosition += 1