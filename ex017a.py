'''Faça um programa que leia o comprimento do cateto oposto e do
cateto adjacente de um triângulo retângulo. Calcule e mostre o
comprimento da hipotenusa'''

from math import sqrt
co = float(input('Comprimento do cateto oposto: '))
ca =float(input('Comprimento do cateto adjascente: '))
h = (co**2) + (ca**2)
print('A hipotenusa vai medir {:.2f}'.format(sqrt(h)))