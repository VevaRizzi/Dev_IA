#Criar o fatorial de N
#(N é a multiplicação de N pelos seus antecessores)

#Inicia nossa função
def calculo_fatorial(n):

    """
    Função calcula o fatorial de um número interiro "N"
    """
    fatorial = 1

    #Cria as regras do número fatorial
    for i in range(2, n + 1):
        fatorial *= i

    return fatorial

#cria a função principal
def main(): #Garante que a função seja executada quando chamda diretamente
    try:
        #entrada dos dados
        N = int(input())

        #Condição de entrada de dados
        if N<= 0 or N>= 13:
            raise ValueError("Número precias estar entre 1 e 12.")

        #Tratativa de dados
        resultado = calculo_fatorial(N)

        #Mostra os dados
        print(resultado)

    except ValueError as ve:
        print(f"Erro {ve}")

if __name__ == "__main__":
    main()