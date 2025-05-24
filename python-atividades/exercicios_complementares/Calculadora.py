# ===========================================
# CALCULADORA
# ===========================================
# Desenvolva uma calculadora em Python que realize as quatro operacoes basicas entre dois numeros. 
# A calculadora deve ser capaz de lidar com diversos tipos de erros de entrada e operacao. Siga as especificacoes abaixo:

# - A calculadora deve solicitar ao usuario que insira dois numeros e uma operacao.
# - As operacoes validas sao: + (adicao), - (subtracao), * (multiplicacao) e / (divisao).
# - O programa deve continuar solicitando entradas ate que uma operacao valida seja concluida.

# Trate os seguintes erros:

# - Entrada invalida (nÃ£o numerica) para os numeros
# - Divisao por zero
# - Operacao invalida

# - Use try/except para capturar e tratar os erros apropriadamente.
# - Apos cada erro, o programa deve informar o usuario sobre o erro e solicitar nova entrada.
# - Quando uma operacao e concluida com sucesso, exiba o resultado e encerre o programa.


while True:
    try:
        firstInput = input("Digite o primeiro número: \n")
        firstNumber = float(firstInput)

        secondInput = input("Digite o segundo número: \n")
        secondNumber = float(secondInput)

        operation = input("Digite a operação (+, -, *, /): ")

        if operation not in ['+', '-', '*', '/']:
            print("Operação inválida. Tente novamente.\n")
            continue

        if operation == '+':
            result = firstNumber + secondNumber

        elif operation == '-':
            result = firstNumber - secondNumber

        elif operation == '*':
            result = firstNumber * secondNumber

        elif operation == '/':
            if secondNumber == 0:
                raise ZeroDivisionError("Não é possível dividir por zero.")
            
            result = firstNumber / secondNumber

        print(f"\nResultado: {firstNumber} {operation} {secondNumber} = {result}")
        break

    except ValueError:
        print("Erro: entrada inválida. Certifique-se de digitar números válidos.\n")
        
    except ZeroDivisionError as e:
        print(f"Erro: {e}\n")
