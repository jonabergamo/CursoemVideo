# cores:|  reset  | amarelo   |    azul   |   verde   |   roxo     | vermelho |
cores = ['\033[0m', '\033[33m', '\033[1:34m', '\033[32m', '\033[1:35m', '\033[1:31m']
# codigo:  | 0 |       | 1 |        | 2 |     | 3 |       | 4 |         | 5 |

lado1: int = int(input('Digite o comprimento do {}primeiro{} lado: '.format(cores[5], cores[0])))
lado2 = int(input('Digite o comprimento do {}segundo{} lado: '.format(cores[4], cores[0])))
lado3 = int(input('Digite o comprimento do {}terceiro{} lado: '.format(cores[2], cores[0])))

equilatero = lado1 == lado2 == lado3
isosceles = lado1 == lado2 != lado3 or lado2 == lado3 != lado1 or \
            lado1 == lado3 != lado2
escaleno = not any([equilatero, isosceles])

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado3 + lado2 > lado1:
    if equilatero:
        print('\nO triângulo é {}equilátero{}!'.format(cores[5], cores[0]))
    elif isosceles:
        print('\nO triângulo é {}isosceles{}!'.format(cores[4], cores[0]))
    else:
        print('\nO triângulo é {}escaleno{}!'.format(cores[2], cores[0]))
else:
    print('\n{}As retas não formam um triângulo!'.format(cores[5]))
