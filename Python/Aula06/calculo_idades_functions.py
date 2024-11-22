#Função que calcula as idades

def calcular_media_idades():
    """
    Função, apra calcular a média de idades e não considerar a negativa(break)
    """

    soma_idades = 0
    quantidade = 0

    while True:
        idade = int(input())
        
        #se é negativa ou não
        if idade <0:
            break

        #soma as idades
        soma_idades += idade
        quantidade += 1

        #cria o contador de quantidade
    if quantidade > 0:
        media = soma_idades / quantidade
        return f"{media:.2f}"
    else:
        return "Nennuma idade válida inserida"
    
def main():
    try:

        media_idades = calcular_media_idades()

        prin(media_idades)

    except ValueError as ve:
        print(f"Erro {ve}")  