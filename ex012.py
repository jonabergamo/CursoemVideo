preco = float(input('Qual o preço do produto? \nR$'))
desconto = int(input('Qual a porcentagem de desconto? \n'))
valorFinal = (preco - ((preco*desconto)/100))
print('O produto que custava R${}, na promoção com desconto de {}% vai custar R${:.2f}'
      .format(preco, desconto, valorFinal))
