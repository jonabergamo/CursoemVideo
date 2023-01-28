n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

maior = n1 if n1 > n2 and n1 > n3 else n2 if n2 > n3 else n3
menor = n1 if n1 < n2 and n1 < n3 else n2 if n2 < n3 else n3

print('\nO maior número é \033[34m{}\033[0m!'.format(maior))
print('O menor número é \033[34m{}\033[0m!'.format(menor))
