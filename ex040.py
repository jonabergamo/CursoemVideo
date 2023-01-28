# cores:|  reset  | amarelo   |    azul   |   verde   |   roxo     | vermelho |
cores = ['\033[0m', '\033[33m', '\033[34m', '\033[32m', '\033[35m', '\033[31m']
# codigo:  | 0 |       | 1 |        | 2 |     | 3 |       | 4 |         | 5 |

# Nota da primeira prova
nota1 = float(input('\nDigite a nota da {}primeira{} prova: '.format(cores[2], cores[0])))

# Nota da segunda prova
nota2 = float(input('Digite a nota da {}segunda{} prova: '.format(cores[4], cores[0])))

if nota1 < 0 and nota2 < 0:

    nota1 = 0
    nota2 = 0

elif nota2 < 0:

    nota2 = 0

elif nota1 < 0:

    nota1 = 0

# Média das duas provas
media = (nota1 + nota2) / 2

# Exibindo resultados baseados na média
print('\nMÉDIA: {}{}\nREPROVADO{}'.format(cores[5], media, cores[0]) if 0 <= media < 5 else
      '\nMÉDIA: {}{}\nRECUPERAÇÃO{}'.format(cores[1], media, cores[0]) if 5 <= media <= 6.9 else
      '\nMÉDIA: {}{}\nAPROVADO{}'.format(cores[3], media, cores[0]))
