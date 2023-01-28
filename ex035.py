lado1 = int(input('Digite o comprimento do primeiro lado: '))
lado2 = int(input('Digite o comprimento do segundo lado: '))
lado3 = int(input('Digite o comprimento do terceiro lado: '))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado3 + lado2 > lado1:
    print('As retas formam um triângulo!')
else:
    print('As retas não formam um triângulo!')