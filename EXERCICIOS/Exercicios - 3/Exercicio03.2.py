# Calculando variação percentual
# Limpando a tela do sistema operacional com a importação do módulo OS.
import os
# Acessando comandos do sistema operacional
os.system("cls") or None

# Solicitando valor inicial
while True:
    valIni = input('Insira o valor inicial: ')
    valIni = int(valIni)

    if valIni > 0:
        break

print()
# Solicitando valor final
while True:
    valFin = input('Insira o valor Final: ')
    valFin = int(valFin)

    if valIni >= 0:
        break

print()

# Criando as variaveis:
difVal = valFin - valIni
Perc = (abs(difVal) / valIni) * 100

# Iniciando as condicionais:
if difVal < 0:
    print('A variação percentual foi de -', Perc, "%")
else:
    print('A variação percentual foi de +', Perc, "%")

