salario = float(input('Qual o seu salário?: '))
if salario > 1250:
    aumento = 10
    salario = salario + (salario * 10) / 100
else:
    aumento = 15
    salario = salario + (salario * 15) / 100
print('seu aumento foi de \033[34m{}%\033[0m e seu novo salário é \033[32mR${:.2f}'.format(aumento, salario))
