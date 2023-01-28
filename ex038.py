# cores:|  reset  | amarelo   |    azul   |   verde   |   roxo     | vermelho |
cores = ['\033[0m', '\033[33m', '\033[34m', '\033[32m', '\033[35m', '\033[31m']
# codigo:  | 0 |       | 1 |        | 2 |     | 3 |       | 4 |         | 5 |


n1 = int(input('Escreva o {}primeiro{} número: '.format(cores[4], cores[0])))
n2 = int(input('Escreva o {}segundo{} número: '.format(cores[1], cores[0])))

# determina qual é o maior número
maior = n1 if n1 > n2 else n2 if n2 > n1 else False

# determina se os dois numeros sao iguais
igual = True if n1 == n2 else False

# verificando se os números sao diferentes e exibindo diferença
if not igual:
    print('\nO {} valor é o maior ({}{}{})\n'
          .format('\033[1:35mprimeiro\033[0m' if maior == n1 else '\033[1:33msegundo\033[0m', cores[2], maior,
                  cores[0]))
# verificando se os números sao iguais
else:
    print('\nOs dois valores são iguais!')
