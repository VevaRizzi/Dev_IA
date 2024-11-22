N = int(input())

def sequencia_logica(n):
    """
    1a função, imprime a sequência para o número inteiro
    """
for i in range(1, n + 1):
    print(i, i**2, i**3)  
    print(i, i**2 +1, i**3 + 1)
#i**2 é ao quadrado, i elevado a 2.
#i**3 é ao cubo, i elevado a 3.
    
def main():
    try:
        entrada = input("Digite a quantidade de testes: ")
        if not entrada.isdigit():
            raise ValueError("Insira o número positivo: ")
        N = int(entrada)

        # N = int(input("Digite a quantidade de testes: "))
        if N < 1 or N >= 1000:
            raise ValueError("O número deve estar entre 1 e 1000")
        
        sequencia_logical(n)
    except ValueError as ve:
        print(f"Erro: {ve}")

if __name__ == "__main__":
    main()




