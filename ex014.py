'''Escreva um programa que converta uma temperatura
digitando em graus Celsius e converta para graus Fahrenheit'''

celsius = float(input('Informe a temperatura em °C: '))
fah = celsius * 9/5 + 32
print('A temperatura de {}°C corresponde a {}°F!'.format(celsius, fah))
