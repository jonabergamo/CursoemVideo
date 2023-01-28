a = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
vez = 0
pa = 0
vezes = 0
for vezes in range(0, 10):
    if vez == 0:
        pa += a
    else:
        pa = a + (vezes * r)
    vezes += 1
    print(pa)
