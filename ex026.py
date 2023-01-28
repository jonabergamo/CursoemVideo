frase = str(input('Escreva uma frase: ')).strip().strip()
print('Quantas vezes aparece a letra A: {}'.format(frase.upper().count('A')))
print('Em que posição ela aparece a primeira vez: {}'.format(frase.find('A')+1))
print('Em que posição ela aparece a última vez: {}'.format(frase.rfind('A')+1))
