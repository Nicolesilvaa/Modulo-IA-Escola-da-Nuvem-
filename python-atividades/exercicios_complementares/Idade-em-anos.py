# ===========================================
# IDADE EM ANOS
# ===========================================

# Crie uma funcao que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.

def calculateAgeInDays(birthYear):

    currentYear = 2025
    ageInYears = currentYear - birthYear
    ageInDays = ageInYears * 365

    return ageInDays


birthYear = int(input("Digite seu ano de nascimento: "))
days = calculateAgeInDays(birthYear)
print(f"Sua idade aproximada em dias é: {days} dias")
