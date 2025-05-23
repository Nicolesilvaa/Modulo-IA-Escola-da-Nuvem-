# ===========================================
# CALCULADORA DE IMC
# ===========================================

# Enunciado:
# Desenvolva um programa que calcule o Indice de Massa Corporal (IMC) de uma pessoa.
# O programa deve solicitar o peso (em kg) e a altura (em metros), calcular o IMC e informar a classificacao de acordo com a tabela padrao.

# Instrucoes:
# - Solicite os dados do usuario: peso e altura.
# - Calcule o IMC usando a formula: IMC = peso / (altura ** 2).
# - Exiba o valor do IMC com uma casa decimal e a respectiva classificacao (ex: abaixo do peso, normal, sobrepeso etc.).

# Explicacao:
# - O exercicio envolve entrada de dados numericos com ponto flutuante, calculos matematicos e estruturas condicionais.
# - A classificacao deve seguir os intervalos padrao definidos para o IMC.
# - Apresente o resultado de forma clara e arredondado corretamente

weight = float(input("Informe seu peso em kg: "))
height = float(input("Informe sua altura em metros: "))

bmi = weight / (height ** 2)
formattedBmi = round(bmi, 1)

if bmi < 18.5:
    classification = "Abaixo do peso"

elif 18.5 <= bmi < 24.9:
    classification = "Peso normal"

elif 25.0 <= bmi < 29.9:
    classification = "Sobrepeso"

elif 30.0 <= bmi < 34.9:
    classification = "Obesidade grau I"

elif 35.0 <= bmi < 39.9:
    classification = "Obesidade grau II"
    
else:
    classification = "Obesidade grau III"

print(f"\nSeu IMC é {formattedBmi} - {classification}")
