from time import sleep
valcasa = float(input('Qual o valor da casa?: '))
salario = float(input('Qual o seu sálario?: '))
anos = int(input('Em quantos anos você vai pagar?'))

prestacao = valcasa / (anos*12)

if prestacao < (salario * 30) / 100:
    print('\n\033[32mSeu empréstimo foi aprovado! Você irá pagar a casa em \033[34m{}\033[32m {}'
          ' e irá pagar \033[33mR${:.2f}\033[32m por mês!\033[0m\n'
          .format(anos, 'ano' if anos == 1 else 'anos', prestacao))
    sleep(3)
    print('\033[35mAguardamos seu retorno!\033[0m')
else:
    print('\n\033[31mInfelizmente seu empréstimo foi negado! Uma prestação de \033[33mR${:.2f}\033[31m ao mês'
          ' durante \033[34m{}\033[31m {}\nestá fora do '
          'nosso orçamento!\033[0m\n'.format(prestacao, anos, 'ano' if anos == 1 else 'anos'))
    sleep(3)
    print('\033[35mTente novamente mais tarde!\033[0m')
