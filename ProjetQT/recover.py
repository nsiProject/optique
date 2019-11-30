try:
	from PIL import Image as img
except ImportError:
	print("Erreur d'imporation des modules nécessaires...")
except Exception as error:
	print("[ERROR] : ", error)
else:

	# Récupération du prénom de la carte d'itentité sous la forme de 8 octets entregistrés dans une liste
	def recoverFirstName(carte):
		listeTemporaire = ""
		firstName = []
		comparaisonOne = 0
		comparaisonTwo = 0
		for ligne in range(0, round(carte.size[1]/13*8), round(carte.size[1]/13)):
			for colonne in range(0, round(carte.size[0]), round(carte.size[0]/8)):
				for carreauHeight in range(ligne, ligne+round(carte.size[1]/13), 1):
					for carreauWidth in range(colonne, colonne+round(carte.size[0]/8), 1):
						color = carte.getpixel((carreauWidth, carreauHeight))
						if color[0] > 127  and color[1] > 127 and color[2] > 127:
							comparaisonOne += 1
						else:
							comparaisonTwo += 1
				if comparaisonOne > comparaisonTwo:
					listeTemporaire += "0"
				else:
					listeTemporaire += "1"
				comparaisonOne = 0
				comparaisonTwo = 0
			firstName.append(listeTemporaire)
			listeTemporaire = ""
		del listeTemporaire
		del comparaisonOne
		del comparaisonTwo
		return firstName

	# Récupération de l'initiale du nom de famille de la carte d'intentité
	def recoverLastName(carte):
		lastName = ""
		comparaisonOne = 0
		comparaisonTwo = 0
		for colonne in range(0, round(carte.size[0]), round(carte.size[0]/8)):
			for carreauHeight in range(round(carte.size[1]/13*8), round(carte.size[1]/13*9), 1):
				for carreauWidth in range(colonne, colonne+round(carte.size[0]/8), 1):
					color = carte.getpixel((carreauWidth, carreauHeight))
					if color[0] > 127  and color[1] > 127 and color[2] > 127:
						comparaisonOne += 1
					else:
						comparaisonTwo += 1
			if comparaisonOne > comparaisonTwo:
				lastName += "0"
			else:
				lastName += "1"
			comparaisonOne = 0
			comparaisonTwo = 0
		del comparaisonOne
		del comparaisonTwo
		return lastName

	# Récupération du jour de naissance de la carte d'identité
	def recoverDay(carte):
		day = ""
		comparaisonOne = 0
		comparaisonTwo = 0
		for colonne in range(0, round(carte.size[0]), round(carte.size[0]/8)):
			for carreauHeight in range(round(carte.size[1]/13*10), round(carte.size[1]/13*11), 1):
				for carreauWidth in range(colonne, colonne+round(carte.size[0]/8), 1):
					color = carte.getpixel((carreauWidth, carreauHeight))
					if color[0] > 127  and color[1] > 127 and color[2] > 127:
						comparaisonOne += 1
					else:
						comparaisonTwo += 1
			if comparaisonOne > comparaisonTwo:
				day += "0"
			else:
				day += "1"
			comparaisonOne = 0
			comparaisonTwo = 0
		del comparaisonOne
		del comparaisonTwo
		return day

	# Récupération du mois de naissance de la carte d'identité
	def recoverMonth(carte):
		month = ""
		comparaisonOne = 0
		comparaisonTwo = 0
		for colonne in range(0, round(carte.size[0]), round(carte.size[0]/8)):
			for carreauHeight in range(round(carte.size[1]/13*11), round(carte.size[1]/13*12), 1):
				for carreauWidth in range(colonne, colonne+round(carte.size[0]/8), 1):
					color = carte.getpixel((carreauWidth, carreauHeight))
					if color[0] > 127  and color[1] > 127 and color[2] > 127:
						comparaisonOne += 1
					else:
						comparaisonTwo += 1
			if comparaisonOne > comparaisonTwo:
				month += "0"
			else:
				month += "1"
			comparaisonOne = 0
			comparaisonTwo = 0
		del comparaisonOne
		del comparaisonTwo
		return month

	# Récupération du genre de la personne de la carte d'identité (HOMME OU FEMME)
	def recoverKind(carte):
		kind = ""
		comparaisonOne = 0
		comparaisonTwo = 0
		for ligne in range(round(carte.size[1]/13*9), round(carte.size[1]/13*10), 1):
			for colonne in range(0, round(carte.size[0]/8), 1):
				color = carte.getpixel((colonne, ligne))
				if color[0] > 127  and color[1] > 127 and color[2] > 127:
					comparaisonOne += 1
				else:
					comparaisonTwo += 1
		if comparaisonOne > comparaisonTwo:
			kind = "Homme"
			return kind
		else:
			kind = "Femme"
			return kind

	# Récupération du siècle de la carte d'identité (1900 ou 2000)
	def recoverCentury(carte):
		century = 0
		comparaisonOne = 0
		comparaisonTwo = 0
		for ligne in range(round(carte.size[1]/13*12), carte.size[1], 1):
			for colonne in range(0, round(carte.size[0]/8), 1):
				color = carte.getpixel((colonne, ligne))
				if color[0] > 127  and color[1] > 127 and color[2] > 127:
					comparaisonOne += 1
				else:
					comparaisonTwo += 1
		if comparaisonOne > comparaisonTwo:
			century = 1900
			return century
		else:
			century = 2000
			return century

	# Récupération de la taille de la personne de la carte d'identité
	def recoverSize(carte):
		size = ""
		comparaisonOne = 0
		comparaisonTwo = 0
		for colonne in range(round(carte.size[0]/8), carte.size[0], round(carte.size[0]/8)):
			for carreauHeight in range(round(carte.size[1]/13*9), round(carte.size[1]/13*10), 1):
				for carreauWidth in range(colonne, colonne+round(carte.size[0]/8), 1):
					color = carte.getpixel((carreauWidth, carreauHeight))
					if color[0] > 127  and color[1] > 127 and color[2] > 127:
						comparaisonOne += 1
					else:
						comparaisonTwo += 1
			if comparaisonOne > comparaisonTwo:
				size += "0"
			else:
				size += "1"
			comparaisonOne = 0
			comparaisonTwo = 0
		del comparaisonOne
		del comparaisonTwo
		return size

	# Récupération de l'année de la personne de la carte d'identité
	def recoverYear(carte):
		year = ""
		comparaisonOne = 0
		comparaisonTwo = 0
		for colonne in range(round(carte.size[0]/8), carte.size[0], round(carte.size[0]/8)):
			for carreauHeight in range(round(carte.size[1]/13*12), carte.size[1], 1):
				for carreauWidth in range(colonne, colonne+round(carte.size[0]/8), 1):
					color = carte.getpixel((carreauWidth, carreauHeight))
					if color[0] > 127  and color[1] > 127 and color[2] > 127:
						comparaisonOne += 1
					else:
						comparaisonTwo += 1
			if comparaisonOne > comparaisonTwo:
				year += "0"
			else:
				year += "1"
			comparaisonOne = 0
			comparaisonTwo = 0
		del comparaisonOne
		del comparaisonTwo
		return year
