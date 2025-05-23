# ===========================================
#  REGISTRO DE NOTAS
# ===========================================

# - Crie um programa que permita a um professor registrar as notas de uma turma. 
# - O programa deve continuar solicitando notas ate que o professor digite 'fim'. 
# - Notas vÃ¡lidas sÃ£o de 0 a 10. 
# - O programa deve ignorar notas invalidas e continuar solicitando. 
# - No final, deve exibir a mÃ©dia da turma. Notas = [] -> len(Notas)â€‹

grades = []

while True:
    entry = input("Digite uma nota (ou 'fim' para encerrar): ")
    
    if entry.lower() == 'fim':
        break

    try:
        grade = float(entry)
        
        if 0 <= grade <= 10:
            grades.append(grade)

        else:
            print("Nota inválida. Digite um valor entre 0 e 10.")

    except ValueError:

        print("Entrada inválida. Digite um número ou 'fim'.")
        
if len(grades) > 0:

    average = sum(grades) / len(grades)
    print(f"Média da turma: {average:.2f}")

else:
    print("Nenhuma nota válida foi registrada.")
