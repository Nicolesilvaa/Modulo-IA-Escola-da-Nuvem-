# ===========================================
# VERIFICADOR DE SENHAS
# ===========================================

# - Crie um programa que verifique se uma senha e forte. 
# - Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um numero. 
# - O programa deve continuar pedindo senhas ate que uma senha valida seja inserida ou o usuario digite 'sair'.

def isStrongPassword(password):
    if len(password) < 8:
        return False

    if not any(char.isdigit() for char in password):
        return False
    return True


while True:
    userInput = input("Digite uma senha (ou 'sair' para encerrar): ")

    if userInput.lower() == 'sair':
        print("Encerrando o programa.")
        break

    if isStrongPassword(userInput):
        print("Senha forte! ")
        break

    else:
        print("Senha fraca! Ela deve ter pelo menos 8 caracteres e conter pelo menos um número.\n")
