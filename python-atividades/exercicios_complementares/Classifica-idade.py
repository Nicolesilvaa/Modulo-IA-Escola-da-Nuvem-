# ===========================================
# CLASSIFICADOR DE IDADE
# ===========================================

# Enunciado:
# Crie um programa que solicite a idade do usuario e classifique-o em uma das seguintes categorias:
# - Crianca (0 a 12 anos)
# - Adolescente (13 a 17 anos)
# - Adulto (18 a 59 anos)
# - Idoso (60 anos ou mais)

# Instrucoes:
# - Solicite que o usuario digite sua idade.
# - O programa deve interpretar o valor digitado e classifica-lo de acordo com as faixas etÃ¡rias.
# - O resultado da classificacao deve ser exibido de forma clara.

# Explicacao:
# - Esse exercicio utiliza estruturas condicionais para tomar decisoes baseadas em faixas numericas.
# - Importante tratar casos invalidos, como idades negativas.
# - A logica deve garantir que nenhuma faixa se sobreponha ou fique sem cobertura.

age = input("\nDigite sua idade: ")

try:
    ageInt = int(age)
    
    if ageInt < 0:
        print("Idade inválida. Por favor, insira um número não negativo.\n")

    elif ageInt <= 12:
        print("Classificação: Criança\n")

    elif 13 <= ageInt <= 17:
        print("Classificação: Adolescente\n")

    elif 18 <= ageInt <= 59:
        print("Classificação: Adulto\n")

    else:
        print("Classificação: Idoso\n")

except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro válido.\n")
