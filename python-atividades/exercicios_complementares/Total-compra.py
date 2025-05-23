# ===========================================
#  TOTAL DA COMPRA
# ===========================================

# Objetivo:
# Calcular o valor total a ser pago por um determinado numero de unidades de um produto.

# Instrucoes:
# - Escreva um programa que armazene o nome de um produto, seu preco unitario e a quantidade comprada.
# - Calcule o valor total da compra e apresente uma descricao detalhada da transacao.

# Explicacao:
# - O valor total e obtido multiplicando o preco unitario pela quantidade comprada.
# - Alem do calculo, a clareza na apresentacao das informacoes e essencial para a compreensao do usuario.
# - O programa deve fornecer uma visao geral da compra, como se fosse um recibo simples.

productName = "Caneta"
unitPrice = 2.50
quantityBought = 4

totalPrice = unitPrice * quantityBought

print("\n----- Recibo de Compra -----")
print(f"Produto: {productName}")
print(f"Preço unitário: R$ {unitPrice:.2f}")
print(f"Quantidade: {quantityBought}")
print(f"Total a pagar: R$ {totalPrice:.2f}")
print("----------------------------\n")
