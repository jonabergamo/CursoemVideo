n = 0
soma = 0

for c in range(1, 500):
    n += 1
    if n % 2 != 0 and n % 3 == 0:
        print(n)
        soma += n

print(soma)
