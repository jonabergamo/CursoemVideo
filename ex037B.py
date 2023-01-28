# cores:|  reset  | amarelo   |    azul   |   verde   |   roxo     | vermelho |
cores = ['\033[0m', '\033[33m', '\033[34m', '\033[32m', '\033[35m', '\033[31m']
# codigo:  | 0 |       | 1 |        | 2 |     | 3 |       | 4 |         | 5 |


num = int(input('Digite um número inteiro: '))
print('''Digite uma das bases para conversão:
[ 1 ] Converter para {}BINÁRIO{}
[ 2 ] Converter para {}OCTAL{}
[ 3 ] Converter para {}HEXADECIMAL{}\n'''
      .format(cores[2], cores[0], cores[2], cores[0], cores[2], cores[0]))

opcao = int(input('Escolha a sua {}opção{}: '.format(cores[4], cores[0])))

if opcao == 1:
    print('\n{}{}{} Convertido para BINÁRIO é {}{}{}'
          .format(cores[2], num, cores[0], cores[2], bin(num)[2:], cores[0]))
elif opcao == 2:
    print('\n{}{}{} Convertido para OCTAL é {}{}{}'
          .format(cores[2], num, cores[0], cores[2], oct(num)[2:], cores[0]))
elif opcao == 3:
    print('\n{}{}{} Convertido para HEXADECIMAL é {}{}{}'
          .format(cores[2], num, cores[0], cores[2], hex(num)[2:].upper(), cores[0]))
else:
    print('\n{}Opção inválida!{}'.format(cores[5], cores[0]))
