print('Protótipo de calculadora Python Nº2')
# Solicitar valores ao usuário
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro Valor: '))
#  Verificar se o segundo valor é zero para evitar divisão por zero
if  n2 != 0:
    s = n1 + n2
    m = n1 * n2
    d = n1 / n2
    di = n1 // n2
    e = n1 ** n2
# Exibir resultados
    print('O valor da soma é {}, o produto é {} e a divisão é {}'.format(s,m,d))
    print('A divisão inteira é {} e a potência {}'.format(di,e))
else:
    print('Não é possível dividir por zero')
 
