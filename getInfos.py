def convertBinaryToDec(value):
    p = len(value)
    valueDecimal = 0
    index = 0
    for k in range(p, 0, -1):
        if value[index] == "1":
            valueDecimal += 2**k
        index += 1
    decimal = int(valueDecimal/2)
    return decimal

def getPrenom(binsPrenom):
	textePrenom = ""
	for i in range(len(binsPrenom)):
		octet = binsPrenom[i]
		textePrenom += chr(convertBinaryToDec(octet))

	return textePrenom

def getInitNom(binNom):
	return chr(convertBinaryToDec(binNom))

def getTaille(binTaille):
	return str(100 + convertBinaryToDec(binTaille[1:]))

def getDateNaissance(binsDateNaissance):
	binJourNaissance = binsDateNaissance[0]
	jourNaissance = str(convertBinaryToDec(binJourNaissance))

	moisNaissance = str(convertBinaryToDec(binsDateNaissance[1]))

	binAnneeNaissance = binsDateNaissance[2]

	if(binAnneeNaissance[0]):
		anneeNaissance = "19"
	else:
		anneeNaissance = "20"
	
	anneeNaissance += str(convertBinaryToDec(binAnneeNaissance))

	return jourNaissance + "/" + moisNaissance + "/" + anneeNaissance

#infos stockées dans la liste octets
octets = ["01000010", "01100001", "01110011", "01110100", "01101001", "01100101", "01101110", "00000000", "01000100", "01010010", "00000100", "00001010", "01010101"]

infosTraitees = [getPrenom(octets[0:7]), getInitNom(octets[8]), octets[9][0], getTaille(octets[9]) , getDateNaissance(octets[10:13])]
for i in range(len(infosTraitees)):
	print(infosTraitees[i])