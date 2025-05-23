# =============================================================
#  CALCULO DO VOLUME DE UMA CAIXA RETANGULAR
# =============================================================

# Objetivo:
# Multiplicar tres valores correspondentes as dimensoes de uma caixa e calcular seu volume.

# Instrucoes:
# - Escreva um programa que armazene os valores de comprimento, largura e altura de uma caixa.
# - Calcule o volume e exiba o resultado.

# Explicacao:
# - O volume de uma caixa retangular e calculado multiplicando-se as tres dimensoes.
# - Essa e uma aplicacao pratica de multiplicacao entre variaveis.
# - O resultado final deve ser exibido com clareza para o usuario.

length = float(input("Informe o comprimento da caixa: "))
width = float(input("Informe a largura da caixa: "))
height = float(input("Informe a altura da caixa: "))

volume = length * width * height

print(f"\nO volume da caixa retangular é {volume}")
