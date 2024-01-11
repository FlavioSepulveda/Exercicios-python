# Calculando a potencia 

# pegando um numero do usuario:
N = input("Digite o valor a seer potenciado: ")
# Convertendo o valor de N pra inteiro
N = int(N)

P = input("Digite o valor da potencia: ")
# Convertendo o valor de P pra inteiro
P = int(P)

# Validando dados
while ((P < 0 or N <= 1)):
    print("Entrada invalida.")
    N = input("Digite o valor a seer potenciado: ")
    N = int(N)
    P = input("Digite o valor da potencia: ")
    P = int(P)

# Fazendo a potenciação:
potencia = 1
if P > 0:
    for j in range(1, P+1): # Sem o +1 o range vai descartar o proximo valor.
        potencia = potencia * N

print()
print(N, "Elevado a", P, ":", potencia)