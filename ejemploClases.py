"""
Definir clases en python
"""
import sys
import PySide
from PySide.QtGui import QApplication
from PySide.QtGui import QMessageBox

app=QApplication(sys.argv)
# -*- coding: utf8 -*-
class animal:
	def __init__(self,type):
		self.type=type

#Clase con herencia
class Dog(animal):
	"""docstring for Dog"""
	def __init__(self, name):
		super(Dog,self).__init__(type="Perro")
		self.prop=None #Null
		self.name=name
		self.tricks=[]

	def addTrick(self,trick):
		self.tricks.append(trick)
		

a = Dog(name="Firulais")

a.addTrick(trick="Gira")
# truco=input("Nombre de truco: ")
# a.addTrick(trick="truco")
print("El "+a.type+" "+a.name+" hace los trucos: ")
print(a.tricks)
msgBox = QMessageBox()
msgBox.setText("The document has been modified.")
msgBox.exec_()
# raw_input()