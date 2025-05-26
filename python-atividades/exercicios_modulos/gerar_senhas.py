#Importando módulos e bibliotecas
import random
import string

#Função que gera senhas aleatórias
def gerarSenha(tamanhoSenha):

    #NOssos caracteres armazenam numeros, letras e caracteres especiais
    caracteres = string.digits + string.ascii_letters + string.punctuation

    senha = ''
    for i in range(tamanhoSenha):
        senha += (random.choice(caracteres))

    return senha


numCaracteres = int(input("\nDigite a quantidade de caracters da senhas: "))

senha = gerarSenha(numCaracteres)
print(f"Esta é sua senha: {senha}\n")

