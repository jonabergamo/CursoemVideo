vez = 0
soma = 0
n1 = 0
n2 = 0
for choice in range(0, 6):
    palavra = ['primeiro', 'segundo', 'terceiro', 'quarto', 'quinto', 'sexto']
    n1 = int(input('Escreva o {} numero inteiro: '. format(palavra[vez])))
    if n2 != 0:
        n2 = n1
    vez += 1
    if n1 % 2 == 0:
        soma = soma + (n1 + n2)
print(soma)
