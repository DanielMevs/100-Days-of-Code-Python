

def caesarCipherEncryptor(string, key):
	newKey = key % 26
	newLetters = []
	for letter in string:
		newLetters.append(findNewLetter(letter, newKey))
	return "".join(newLetters)

def findNewLetter(letter, key):
	newLetter = ord(letter) + key
	return chr(newLetter) if newLetter <= 122 else chr(96 + newLetter % 122)