from datetime import date
ano = int(input('Insira um ano do calendario: '))
if ano == 0:
    ano = date.today().year
if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
    print('\nO ano de \033[35m{}\033[0m é bissexto!'.format(ano))
else:
    print('\nO ano de \033[35m{}\033[0m não é um ano bissexto!'.format(ano))

