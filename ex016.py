'''Crie um programa que leia um número Real qualquer pelo
teclado e mostre na tela a sua porção Inteira.'''

from math import trunc
value = float(input('Digite um valor: '))
print('O valor digital foi {} e a sua porção inteira é {}'.format(value, trunc(value)))