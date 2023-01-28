'''Faça um programa que leia um ângulo qualquer e mostre na tela o
valor do seno, cosseno e tangente desse ângulo.'''

from math import sin, cos, tan, radians

ang = float(input('Digite o ângulo que você deseja: '))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, sin(radians(ang))))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang, cos(radians(ang))))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang, tan(radians(ang))))