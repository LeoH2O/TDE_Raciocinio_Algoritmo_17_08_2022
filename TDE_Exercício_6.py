# Exercício 6

# Entrada de dados
cateto_oposto = float(input("Digite valor do cateto oposto: "))
cateto_adjacente = float(input("Digite valor do cateto adjacente: "))

# Calculo da hipotenusa
hipotenusa = (cateto_oposto **2 + cateto_adjacente **2) ** (1 / 2)

# Mostrar valor da hipotenusa
print("Valor da hipotenusa: " + str(hipotenusa))
