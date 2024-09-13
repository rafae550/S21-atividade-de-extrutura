numero = int(input("Digite um número para calcular a tabuada: ")) # Solicita um número
if numero > 0: # Verifica se o número é valido (maior que 0)
    for i in range(1, 11): # comando de repetição para imprimir a tabuada do número
        print(f"{numero} x {i} = {numero * i}")  
else:
    print("Número inválido! Deve ser maior que 0.")
