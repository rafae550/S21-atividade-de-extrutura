print("Escolha uma operação: +, -, *, /") # Escolha uma operação matemática
operacao = input("Operação: ") # operação de +,-,*,/
num1 = float(input("Primeiro número: ")) # escolha o primeiro número da operação
num2 = float(input("Segundo número: ")) # escolha o segundo número da operação

if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    if num2 != 0:  # Verifica se o divisor é diferente de zero para evitar divisão por zero
        resultado = num1 / num2
    else:
        print("Erro: Divisão por zero!") # Mensagem de erro
        resultado = None
else:
    print("Operação inválida!") # Mensagem de erro
    resultado = None

if resultado is not None:
    print(f"Resultado: {resultado}") # Resultado da operação
