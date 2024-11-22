import random
#valor é um número randomico, entre 1 e 10mil
#apresentar o maior valor lido e o menor valor lido randomicamente e mostra o índice dele.

def main():
    valor = [random.randint(1,10000) for _ in range(100)]

    maior = (max(valor))
    posicao = valor.index(maior)+1

    resultado = {
        "Números": valor,
        "Maior valor": maior,
        "Posição": posicao
    }

    print("\n Números gerados: ")
    print(valor)
    print("\nMaior valor:", maior)
    print("Posição do Maior Valor: ",posicao)

    # if __name__ == "__main__":
    #     main()