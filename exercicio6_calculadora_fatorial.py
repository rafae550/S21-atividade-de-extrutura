import math

numero = int(input("Digite um número inteiro positivo: ")) # Solicita um número inteiro positivo
if numero >= 0: 
    fatorial = math.factorial(numero) # Calcula o fatorial do número
    print(f"O fatorial de {numero} é {fatorial}.")
else:
    print("Número inválido! O número deve ser positivo.")
