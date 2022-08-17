# Exercício 8

# Valores
preco_lata = 50
pi = 3.14

# Entrada de dados
tanque_raio = float(input("Valor do raio do tanque: "))
tanque_altura = float(input("Valor da altura do tanque: "))

# Área da base do tanque
area_base = pi * tanque_raio **2

# Área lateral do tanque
area_lateral = 2 * pi * tanque_raio * tanque_altura

# Área do tanque
area_total = area_base + area_lateral

# Calculo para descobrir quantas latas serão necessárias 1L= 3m² /  cada lata = 5L
area_metro = area_total / 3
area_litro = area_metro / 5

# Calculo custo para pintar o cilindro
custo_lata = area_litro * preco_lata

# Mostrar quantidade de latas e custo
print("Será necessário: " + str(area_litro) + " lata(s)")
print("O custo será: R$ " + str(custo_lata))
