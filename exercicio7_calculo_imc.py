peso = float(input("Digite o peso (kg): ")) 
altura = float(input("Digite a altura (m): "))
imc = peso / (altura ** 2)

if imc < 18.5: # Classifica o IMC e exibe a categoria
    classificacao = "Abaixo do peso" # Abaixo do peso
elif 18.5 <= imc < 25:
    classificacao = "Peso normal" # Peso normal
elif 25 <= imc < 30:
    classificacao = "Sobrepeso" # Sobrepeso
else:
    classificacao = "Obesidade" # Obesidade

print(f"IMC: {imc:.2f} - {classificacao}") 
