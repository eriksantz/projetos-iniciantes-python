valor = float(input('Qual é o preço do produto? R$'))
novo = valor - (valor * 5/100)
print(f'O produto que custava R${valor:.2f}, na promoção com desconto de 5% vai custar R${novo:.2f}')
