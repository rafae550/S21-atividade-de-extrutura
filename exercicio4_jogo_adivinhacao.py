import random

numero_secreto = random.randint(1, 50)
tentativas = 0

while tentativas < 5: 
    # Solicita um palpite do usuário
    palpite = int(input("Digite seu palpite (entre 1 e 50): "))
    tentativas += 1
    
    # Compara o palpite com o número secreto e fornece dicas
    if palpite < numero_secreto:
        print("O número é maior.")
    elif palpite > numero_secreto:
        print("O número é menor.")
    else:
        print("Parabéns! Você acertou o número.")  # Mensagem de sucesso
        break  # Encerra o laço
else:
    print(f"Você não conseguiu adivinhar. O número era {numero_secreto}.")
