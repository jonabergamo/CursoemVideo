produto = float(input('\nQual o preço do produto?: '))
condicao = int(input('\nQual a condição de pagamento?\n\n[ 1 ] À vista \033[34mdinheiro/cheque\n'
                     '\033[0m[ 2 ] À vista \033[34mcartão\033[0m: \033[33m5%\033[0m de desconto\n'
                     '[ 3 ] Em até \033[34m2x no cartão\033[0m: preço normal'
                     '\n[ 4 ] \033[34m3x ou mais\033[0m no cartão:\033[33m 20%\033[0m de juros\n'))
condicao_TXT = ''
juros = 0
produto_final = 0
parcelas = 0

if condicao == 1:
    condicao_TXT = 'À vista \033[34mdinheiro/cheque\033[0m'
    juros = 10
    produto = produto - (produto * 10) / 100
elif condicao == 2:
    condicao_TXT = 'À vista \033[34mcartão\033[0m'
    juros = 5
    produto = produto - (produto * 5) / 100
elif condicao == 3:
    parcelas = 2
    condicao_TXT = 'Em até \033[34m2x no cartão\033[0m'
    juros = 0
    produto = produto
    produto_final = produto / parcelas
elif condicao == 4:
    parcelas = int(input('Em quantas parcelas?: '))
    if 3 <= parcelas:
        condicao_TXT = '\033[34m3x ou mais\033[0m no cartão'
        juros = -20
        produto = produto + (produto * 20) / 100
        produto_final = produto / parcelas
    else:
        print('\n\n\033[31mEscolha um valor maior que 3x!\n\n')
        exit()
else:
    print('Escolha uma opção válida!')

if juros == 0:
    juros_TXT = 'Nenhum'
elif juros > 0:
    juros_TXT = '\033[32mDesconto'
else:
    juros_TXT = "\033[33mJuros"


print('Você escolheu a opção {} e irá pagar \033[32mR${}\033[0m pelo produto\n{}:{}%'
      .format(condicao_TXT, produto, juros_TXT, abs(juros)))
print('\033[0mSerão {} parcelas de R${:.2f}!'
      .format(parcelas, produto_final))
