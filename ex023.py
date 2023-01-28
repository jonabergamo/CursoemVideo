digito = int(input('Escreva um número: '))
u = digito // 1 % 10
d = digito // 10 % 10
c = digito // 100 % 10
m = digito // 1000 % 10
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))
