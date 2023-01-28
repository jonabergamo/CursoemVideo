n = int(input('Digite um número inteiro: '))
if n % 2 == 0:
    print('O numero \033[35m{}\033[0m é par!'.format(n))
else:
    print('O numero \033[35m{}\033[0m é impar!'.format(n))
