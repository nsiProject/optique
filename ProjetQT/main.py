try:
	from recover import *
	from conversions import *
	from time import *
	from PIL import *
	import platform

	import sys
	import random
	from PySide2 import QtCore, QtWidgets, QtGui
except Exception as error:
	print("[ERROR] : ", error)
	exit()

def selectionImage(filename):
	try:		
		# Modification des propriétés de l'image avec la bibliothèque pillow (python -m pip install pip wheel setuptools --upgrade et python -m pip install --upgrade pillow)
		carte = img.open(filename)
		if carte.size[0] == 400 and carte.size[1] == 300:
			carte = carte.rotate(90)
			carte = carte.rotate(180)
			left = 111
			top = 40
			right = 275
			bottom = 300
			carte = carte.crop((left, top, right, bottom))
			carte = carte.resize((800, 1300))
		else:
			print("L'image ne peut pas être traduite...")
	except IOError:
		print("Ce fichier n'est pas recevable...")
	except Exception as error:
		print("[ERROR] : {}".format(error))
	else:
		print("Fin de l'importation de l'image")
		return carte

class Window(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()



		self.labelFile = QtWidgets.QLabel()
		self.labelFile.setGeometry(10, 10, 200, 30)

		self.btnFile = QtWidgets.QPushButton()
		self.btnFile.setGeometry(220, 10, 170, 30)
		self.btnFile.setText("Sélectionner un fichier")

		self.btnConvert = QtWidgets.QPushButton()
		self.btnConvert.setGeometry(400, 10, 100, 30)
		self.btnConvert.setText("Convertir")

		self.layoutTest = QtWidgets.QHBoxLayout()
		self.layoutTest.addWidget(self.labelFile)
		self.layoutTest.addWidget(self.btnFile)
		self.layoutTest.addWidget(self.btnConvert)

		self.btnFile.clicked.connect(self.chooseFile)
		self.btnConvert.clicked.connect(self.convertions)

		#Résultats (non visibles au lancement)

		self.labelPrenom = QtWidgets.QLabel()
		self.labelNom = QtWidgets.QLabel()
		self.labelSexe = QtWidgets.QLabel()
		self.labelTaille = QtWidgets.QLabel()
		self.labelNaissance = QtWidgets.QLabel()

		self.layoutResultats = QtWidgets.QFormLayout()        
		self.layoutResultats.addRow("Prénom : ", self.labelPrenom)
		self.layoutResultats.addRow("Nom : ", self.labelNom)
		self.layoutResultats.addRow("Sexe : ", self.labelSexe)
		self.layoutResultats.addRow("Taille : ", self.labelTaille)
		self.layoutResultats.addRow("Naissance : ", self.labelNaissance)

		#########

		self.layoutPrincipal = QtWidgets.QGridLayout(self)
		#self.layoutPrincipal.setVerticalSpacing(100)
		self.layoutPrincipal.addLayout(self.layoutTest, 0, 0)
		self.layoutPrincipal.addLayout(self.layoutResultats, 1, 0, 1, 3)
		#self.layoutPrincipal.addLayout(self.layoutTest)
		#self.layoutPrincipal.addLayout(self.layoutResultats)


	def chooseFile(self):
		fileName = QtWidgets.QFileDialog.getOpenFileName(self, "Open Image", "/", "Image Files (*.png *.jpg *.bmp)")
		#self.fileName = "\"" + fileName[0] + "\""
		self.fileName = fileName[0]
		self.labelFile.setText(self.fileName)

	def convertions(self):
		carte = selectionImage(self.fileName)

		infos = []
		infos.append(getFirstName(recoverFirstName(carte)))
		infos.append(getLastName(recoverLastName(carte)))
		infos.append(recoverKind(carte))
		infos.append(getSize(recoverSize(carte)))

		infos.append(getDateOfBirth(\
			recoverDay(carte), \
			recoverMonth(carte), \
			recoverYear(carte), \
			recoverCentury(carte))\
		)

		self.displayInfos(infos)

	def displayInfos(self, infos):
		try:
			self.labelPrenom.setText(infos[0])
		except:
			self.labelPrenom.setText("Erreur de lecture")
		try:
			self.labelNom.setText(infos[1])
		except:
			self.labelNom.setText("Erreur de lecture")
		try:
			self.labelSexe.setText(infos[2])
		except:
			self.labelSexe.setText("Erreur de lecture")
		try:
			self.labelTaille.setText(infos[3])
		except:
			self.labelTaille.setText("Erreur de lecture")
		try:
			self.labelNaissance.setText(infos[4])
		except:
			self.labelNaissance.setText("Erreur de lecture")
    	


        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Window()
    #window.resize(530, 450)
    window.show()

    sys.exit(app.exec_())
