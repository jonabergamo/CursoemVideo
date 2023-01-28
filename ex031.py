dist = float(input('Qual foi a distancia da viagem em km?: '))
if 200 >= dist >= 0:
    print('\nSua passagem vai custar \033[32mR${}\033[0m'.format(dist*0.50))
else:
    print('\nSua passagem passou os 200km e irá custar \033[32mR${}\033[0m'.format(dist*0.45))

