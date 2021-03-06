# -*- coding: utf-8 -*-
"""Actividad 6 - Fabris Germán.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1i128eYA57Orf17dtdJrY1xQbySS4i1-d
"""

''' Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales).
El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase: 
Un constructor.
mostrar(): Muestra los datos de la cuenta. 
 ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada. 
retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos '''
class Cuenta:
  def __init__(self,titular):
    self.titular = titular
    
  def cantidad(self,cantidad):  
    self.cantidad = cantidad

  def __str__(self):
    return f"Soy titular de ceunta llamado {self.titular} cantidad {self.cantidad}"

  def mostrar(self):
    return f'Datos de cuenta: Titular: {self.titular} Saldo: {self.cantidad}'
  
  def ingresar(self,ingresar):
    if ingresar < 0:
      return "No has ingresado nada, intenta nuevamente"
    else:
      self.ingresar = ingresar
      self.cantidad = self.cantidad + ingresar
      return f"Has ingresado: \033[1;32m{self.ingresar}\033[2J\033[ a tu cuenta, tu saldo es: {self.cantidad}"
  def retirar(self,retirar):
    self.retirar = retirar
    self.cantidad = self.cantidad - retirar
    return f"Has retirado: \033[1;31m{self.retirar}\033[2J\033[ de tu cuenta, tu saldo es: {self.cantidad}"
  
cuenta1 = Cuenta("German")
cuenta1.cantidad(1500)

print(cuenta1.mostrar())
print(cuenta1.ingresar(100))
print(cuenta1.retirar(200))
#print(cuenta1.ingresar(-2))