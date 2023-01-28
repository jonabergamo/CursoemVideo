import re
from unidecode import unidecode

frase = str(input('Escreva uma frase: ')).lower().strip().replace(' ', '')

esarf = frase[::-1]
frase = re.sub(r'[^\w\s]', '', frase)
esarf = re.sub(r'[^\w\s]', '', esarf)
print('Sua frase ao contrário fica: {}'.format(esarf.capitalize()))

if unidecode(frase) == unidecode(esarf):
    print('Essa frase é um palindromo!')
else:
    print('Essa frase não é um palindromo!')
