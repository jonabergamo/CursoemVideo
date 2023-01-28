from datetime import date

ano = int(input('Qual o seu ano de nascimento?: '))

# Calculando idade atual
idade = date.today().year - ano

# Calculando a diferença de idade com 18
passou = idade - 18

# verificando se o usuario tem menos de 18 anos
if idade < 18:
    print('Falta \033[34m{}\033[0m {} para você se alistar ao serviço militar!'.format(abs(passou), 'ano' if abs(
        passou) == 1 else 'anos'))
# verificando se o usuario tem 18 anos
elif idade == 18:
    print('Você está na idade de ser alistar ao serviço militar!')
# verificando se o usuario tem mais de 18 anos
else:
    print(
        'Você passou \033[34m{}\033[0m {} da data do seu alistamento!'.format(passou, 'ano' if passou == 1 else 'anos'))
