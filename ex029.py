cores = {
    "vermelho": "\033[31m",
    "amarelo": "\033[33m",
    "azul": "\033[34m",
    "piscando": "\033[5m",
    "reset": "\033[0m"
}
vel = float(input('{}Qual a velocidade do carro?: '.format(cores['azul'])))

if vel > 80:
    print("\n{}Você excedeu o limite permitido que é de 80Km/h\nVocê deve pagar uma multa de "
          "{}R${:.2f}!".format(cores['amarelo'], cores['vermelho'], (vel - 80) * 7))
else:
    print('{}Você dirige bem!'.format(cores['azul']))

print('\n{}Tenha um bom dia! Dirija com segurança!'.format(cores['azul']))
