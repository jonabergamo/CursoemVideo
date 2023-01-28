# cores:|  reset  | amarelo   |    azul   |   verde   |   roxo     | vermelho |
cores = ['\033[0m', '\033[1:33m', '\033[1:34m', '\033[32m', '\033[1:35m', '\033[31m']
# codigo:  | 0 |       | 1 |        | 2 |     | 3 |       | 4 |         | 5 |

peso = float(input('Digite seu {}peso{}: '.format(cores[5], cores[0])))
altura: float = float(input('Digite sua {}altura{}: '.format(cores[2], cores[0])))

if altura > 10:
    altura = altura / 100

IMC = peso / (altura ** 2)
IMC_LIST = ['{}Abaixo do Peso{}'.format(cores[5], cores[0]),
            'no {}Peso ideal{}'.format(cores[3], cores[0]),
            'em {}Sobrepeso{}'.format(cores[4], cores[0]),
            'em estado de {}Obesidade{}'.format(cores[4], cores[0]),
            'em estado de {}Obesidade Mórbida{}'.format(cores[1], cores[0])]

if 0 < IMC <= 18.5:
    print('Você está {}', IMC_LIST[0])
elif 18.5 < IMC <= 25:
    print('Você está', IMC_LIST[1])
elif 25 < IMC <= 30:
    print('Você está', IMC_LIST[2])
elif 30 < IMC <= 40:
    print('Você está', IMC_LIST[3])
else:
    print('Você está', IMC_LIST[4])


print('Seu IMC é {}{:.1f}{}'
      .format(cores[5], IMC, cores[0]))
