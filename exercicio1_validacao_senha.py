senha_correta = "segura123"

while True:
    senha = input("Digite a senha: ") # Verifica se a senha inserida está correta.
    if senha == senha_correta:
        print("Acesso permitido")  # Mensagem de sucesso.
        break  
    else:
        print("Senha incorreta")  # Mensagem de erro.