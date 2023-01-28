num_original = int(input('\033[96mEscreva um número inteiro qualquer: \033[0m'))
base_choice = int(input('\033[94m\nDigite a base de conversão: \n\n\033[34m1\033[0m para ''binário\n\033[34m2\033[0m '
                        'para octal\n\033[34m3\033[0m para hexadecimal\n\033[0m\n'))

resultado = ""

"""
Conversão de um número de decimal para binário, octal ou hexadecimal
"""

if base_choice == 1:
    tabela = '01'
    base_text = "binário"
    base = 2
elif base_choice == 2:
    tabela = '01234567'
    base_text = "octal"
    base = 8
elif base_choice == 3:
    tabela = '0123456789ABCDEF'
    base_text = "hexadecimal"
    base = 16
else:
    print('Opção inválida!')
    exit()

num = num_original

while num > 0:
    resto = num % base
    resultado = tabela[resto] + resultado
    num = num // base

# exibir o resultado
if 1 <= base_choice <= 3:
    print("\nO \033[32m{}\033[0m em \033[34m{}\033[0m é \033[35m{}\033[0m".format(num_original, base_text, resultado))
else:
    print('Opção inválida!')
