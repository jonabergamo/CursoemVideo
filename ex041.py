from datetime import date

# cores:|  reset  | amarelo   |    azul   |   verde   |   roxo     | vermelho |
cores = ['\033[0m', '\033[33m', '\033[34m', '\033[32m', '\033[35m', '\033[31m']
# codigo:  | 0 |       | 1 |        | 2 |     | 3 |       | 4 |         | 5 |

nasc = int(input('\nDigite seu {}ano{} de nascimento: '.format(cores[4], cores[0])))
idade = date.today().year - nasc

if idade > 20:
    tipo = 'MASTER'
elif idade == 20:
    tipo = 'SENIOR'
elif 14 < idade <= 19:
    tipo = 'JUNIOR'
elif 9 < idade <= 14:
    tipo = 'INFANTIL'
else:
    tipo = 'MIRIM'


print('\nVocê é um atleta do tipo {}{}{}'.format(cores[2], tipo, cores[0]))
