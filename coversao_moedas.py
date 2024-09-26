valor = float(input('Quanto dinheiro você possui no seu banco digital? R$'))
dolar = valor / 5.44
euro = valor / 6.08
print(f'Com R${valor:.2f} você pode comprar US${dolar:.2f}')
print(f'Com R${valor:.2f} você pode comprar EUR{euro:.2f}')
