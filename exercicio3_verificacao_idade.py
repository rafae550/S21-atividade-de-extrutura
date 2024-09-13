while True:
    # Solicita a idade do usuário ou -1 para parar
    idade = int(input("Digite a idade (ou -1 para parar): "))
    
    # Encerra o laço se o usuário inserir -1
    if idade == -1:
        break
    # Classifica a idade e exibe a categoria
    elif idade < 18:
        print("Menor de idade")
    elif 18 <= idade <= 65:
        print("Adulto")
    else:
        print("Idoso")
