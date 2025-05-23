# ===========================================
# PALINDROMO
# ===========================================

# Crie uma funcao que verifique se uma palavra ou frase e um palindromo 
# (le-se igual de tras para frente, ignorando espacos e pontuacao). 
# Se o resultado E True, responda â€œSimâ€, se o resultado for False, responda â€œNao"

def isPalindrome(text):

    cleanedText = '' #Para ignorar caracters 
    for char in text:
        if char.isalnum():
            cleanedText += char.lower()
    
    reversedText = ''
    for i in range(len(cleanedText) - 1, -1, -1):
        reversedText += cleanedText[i]
    
    if cleanedText == reversedText:
        return "Sim"
    else:
        return "Não"

phrase = input("Digite uma palavra ou frase: ")
result = isPalindrome(phrase)
print(f"É um palíndromo? {result}")
