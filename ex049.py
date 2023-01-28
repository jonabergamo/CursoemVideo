num = int(input('\nEscolha um número: '))
mult = 0
for c in range(0, 10):
    mult += 1
    final = mult * num
    print('{} x {} = {}'.format(num, mult, final))
