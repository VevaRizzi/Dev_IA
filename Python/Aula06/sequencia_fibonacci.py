def fibonacci(n):
    """
    Gerar a série de Fibonacci(lógica) até o N-ésimo termo
    """
    #iniciar os primeiros valores da série
    a, b = 0, 1
    resultado = [a]

    #geração d termo (É a lógica por trás da resolução do problema)
    for i in range(1, n):
        resultado.append(b)
        a, b = b, a + b

    #Função devolve o resultado: [0,1,1,2,3]
    print(f"Resultado sem tratamento: {resultado}")
    return resultado

    
def main():
    try:
        N = int(input())
        if N <= 0 or N >= 46:
            raise ValueError("O número precisa estar entre 1 e 46")
        #pega o resultado sem tratar: [1,2,3,4,5]     
        fibonacci_sequence = fibonacci(N)

        #pega o resultado tratado: 
        print(" ".join(map(str, fibonacci_sequence)))

    except ValueError as ve:
        print(f"Erro {ve}")

if __name__ == "__main__":
    main()