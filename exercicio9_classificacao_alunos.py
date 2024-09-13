# Listas para armazenar os nomes e notas dos alunos
notas = [8.5, 6.0, 7.5, 5.0, 9.0]
nomes = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"]

# Calculando a média da turma
media_turma = sum(notas) / len(notas)

# Classificando os alunos com base na nota
print("Classificação dos alunos:")
for nome, nota in zip(nomes, notas):
    if nota >= 7:
        print(f"{nome} - Aprovado")
    else:
        print(f"{nome} - Reprovado")

# Exibindo a média da turma
print(f"\nMédia da turma: {media_turma:.2f}")

