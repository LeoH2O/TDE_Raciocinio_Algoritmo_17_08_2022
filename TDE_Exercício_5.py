# Exercício 5

# Entrada de dados
prod_preco = float(input("Digite o valor do produto: R$"))
# Juros de 5%
prod_porc = prod_preco * 0.05

# 3 parcelas com 5% de juros
tres_parc = (prod_preco / 3) + prod_porc
tres_total = tres_parc * 3

# 2 parcelas sem juros
duas_parc = prod_preco / 2

# preço a vista com 5% desconto
vista_valor = prod_preco - prod_porc

# Mostrar o valor total e o valor de cada parcela em 3 meses com 5% de juros
print("Valor de cada 3 parcelas(5% juros): R$" + str(tres_parc))
print("Valor total a ser pago em 3 parcelas: R$" + str(tres_total))

# Mostrar o valor de cada parcela em 2 meses sem juros
print("Valor de cada 2 parcelas(sem juros): R$" + str(duas_parc))

# Mostrar o valor a vista com desconto de 5%
print("Valor do preço a vista(5% desconto): R$" + str(vista_valor))