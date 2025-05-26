#Importando módulos e bibliotecas
import random
import string

#Função que gera senhas aleatórias
def gerarSenha(tamanhoSenha):

    #Nossos caracteres armazenam numeros, letras e caracteres especiais
    caracteres = string.digits + string.ascii_letters + string.punctuation

    senha = ''
    for i in range(tamanhoSenha):
        senha += (random.choice(caracteres))

    return senha

flag = True
while flag:
    try:
        numCaracteres = int(input("\nDigite a quantidade de caracteres da senha: "))
        
        if numCaracteres <= 0:
            print("Por favor, digite um número maior que zero.")
            continue

        senha = gerarSenha(numCaracteres)
        print(f"Esta é sua senha: {senha}\n")

        resposta = input("Deseja continuar? Digite 's' para sim ou 'n' para não: ").strip().lower()
        flag = True if resposta == 's' else False  

    except ValueError:
        print("Entrada inválida! Por favor, digite um número inteiro.")

