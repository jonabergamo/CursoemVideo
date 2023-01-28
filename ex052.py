num = int(input('Digite um número inteiro: '))


if num <= 1:
    print('Números menores ou iguais a 1 não podem ser primos')
for i in range(2, int(num ** (1/2)) + 1):
    if num % i == 0:
        print('O número não é primo!')
    else:
        print('O número é primo!')
        exit()
