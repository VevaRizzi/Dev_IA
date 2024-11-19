"""
Qualquer valor entre [0,25], [25,50], [50,75] ou [75,100]
Preciso incluir os números do intervalo.
"""

#if elif else
# numero - float(input("Digite o número para eu dizer o intervalo: "))

numero = round(float(input("Digite um número com no maximo 2 casas decimais")))
intervalo1 = "0,25"


if 0 <= numero <= 25:
    # print(f"Invervalo{intervalo1}")
    print(f"Invervalo[0,25]")
elif 25 < numero <= 50:
    print(f"Invervalo[25,50]")
elif 50 < numero <= 75:
    print(f"Invervalo[50,75]")
elif 75 < numero <= 100:
    print(f"Invervalo[75,100]")
else:
    print("Fora do Intervalo")