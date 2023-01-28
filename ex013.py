salario = float(input('Qual o salário do funcionario? \nR$'))
aumento = int(input('Quanto de aumento esse funcionario recebeu? \n'))
salarioFinal = salario + (salario*aumento/100)
print('Esse funcionário recebeu {}% de aumento e agora receberá R${:.2f}'.format(aumento, salarioFinal))