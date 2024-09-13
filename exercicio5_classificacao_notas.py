while True:
    soma_notas = 0
    num_alunos = int(input("Quantos alunos? ")) # coleta o número de alunos
    for i in range(num_alunos):
        nota = float(input(f"Digite a nota do aluno {i + 1}: ")) # coleta as notas dos alunos
        soma_notas += nota # calcula a soma
    
    media = soma_notas / num_alunos # calcula a média das notas 
    if media >= 7:
        print("Aprovado") # classifica a média e exibe o resultado
    elif media >= 5:
        print("Recuperação") # classifica a média e exibe o resultado
    else:
        print("Reprovado") # classifica a média e exibe o resultado
    
    continuar = input("Deseja inserir notas de outros alunos? (s/n): ") # pergunta ao usúario se deseja continuar
    if continuar.lower() != 's':
        break
