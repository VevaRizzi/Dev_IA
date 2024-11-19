try:
    resultado = 10/0
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida!")

    try:
    resultado = 10/5
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida!")