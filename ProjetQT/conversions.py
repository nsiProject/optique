# Conversion d'un entier naturel en binaire HUGO
def convertBinaryToDecimal(value):
	p = len(value)
	valueDecimal = 0
	index = 0
	for k in range(p, 0, -1):
		if value[index] == "1":
			valueDecimal += 2**k
		index += 1
	decimal = int(valueDecimal/2)
	return decimal

# Récupération du code ascii du code binaire du prénom en code ASCII HUGO
def getFirstName(binaryName):
	textName = ""
	for i in range(len(binaryName)):
		octet = binaryName[i]
		textName += str(chr(convertBinaryToDecimal(octet)))
	return str(textName)

# Récupération du code ascii du code binaire du nom en code ASCII HUGO
def getLastName(binaryName):
	return chr(convertBinaryToDecimal(binaryName))

# Récupération du code ascii du code binaire de la taille en code ASCII HUGO
def getSize(binarySize):
	return str("1m" + str(convertBinaryToDecimal(binarySize)))
# Récupération du code ascii du code binaire de la date de naissance en code ASCII HUGO
def getDateOfBirth(binaryDayOfBirth, binaryMonthOfBirth, binaryYearOfBirth, binaryCenturyOfBirth):
	stringDay = str(convertBinaryToDecimal(binaryDayOfBirth))
	stringMonth = str(convertBinaryToDecimal(binaryMonthOfBirth))
	stringYear = str(convertBinaryToDecimal(binaryYearOfBirth)+binaryCenturyOfBirth)
	return stringDay + "/" + stringMonth + "/" + stringYear