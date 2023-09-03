try: # attempt a relative import of the required modules
    from ._string_number_convert import _stringToNumbers as stringToNumbers
except: # if relative import fails, use a direct import instead
    from _string_number_convert import _stringToNumbers as stringToNumbers

def substitutionCipher(plainText, alphabet):
    print("placeholder")