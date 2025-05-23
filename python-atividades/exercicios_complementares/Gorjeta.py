# ===========================================
# GORJETA
# ===========================================

# Enunciado: 
# Crie uma funcao que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de gorjeta desejada.
# Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.â€‹

# â€‹ParÃ¢metros:â€‹

# - valor_conta (float): O valor total da contaâ€‹
# - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)â€‹

# â€‹Retorna:â€‹
# O valor da gorjeta calculadaâ€‹â€‹

def calculateTip(billAmount, tipPercentage):
    tipValue = billAmount * (tipPercentage / 100)

    return tipValue

billAmount = float(input("Digite o valor da conta: "))
tipPercentage = float(input("Digite a porcentagem da gorjeta (ex: 10, 15, 20): "))

tip = calculateTip(billAmount, tipPercentage)
print(f"Gorjeta: R${tip:.2f}")
