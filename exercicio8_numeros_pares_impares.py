numero = int(input("Digite um número: ")) # Solicita um número
for i in range(1, numero + 1): # Laço de repetição para imprimir todos os números de 1 até o número inserido
    if i % 2 == 0: # Verifica se o número é par ou ímpar e exibe a mensagem correspondente
        print(f"{i} é par") 
    else:
        print(f"{i} é ímpar")
