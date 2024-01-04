# EXERCICIO EXTRA -

'''
    O principal objetivo deste mine projeto é construir uma tabuada
'''

# Variaveis -

valor = int(input('Escolha o valor a ser multiplicado: '))

limMin = 1
limMax = 10

# Criando uma lista que vai armazenar os valores
tabuada = [resultado for resultado in range(limMin, limMax + 1)]

# Imprimindo na tela a tabuada:
for resultado in tabuada:
    print(valor, " X ", resultado, " = ", resultado * valor)
else:
    print('Fim.')