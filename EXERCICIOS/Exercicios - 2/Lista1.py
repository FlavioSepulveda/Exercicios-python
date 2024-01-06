# Objetivo: Criar uma lista desordenada de nomes
lista1 = ['Carlos', 'Marcelo', 'Julio', 'Luis', 'Caio']
# Coletar o nome do usuario
nome = str(input('Insira seu nome: '))
# Colocar o nome do usuario na lista
lista1.append(nome)
# Organizar a lista em ordem alfabetica
lista1.sort()
# Escrever na tela a lista da maneira que achar melhor;
if nome in lista1:
    for x in lista1:
        print(x)