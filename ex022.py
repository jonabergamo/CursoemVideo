nome = str(input('Qual seu nome completo?: ')).strip()
print(nome)
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minuscúlas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)))
print('Seu primeiro nome é {} e ele tem {} letras'.format(nome.split()[0], len(nome.split()[0])))
