"""
1: 4.00
2: 4.50
3: 5.00
4: 2.00
5: 1.00
"""


codigo, quantidade = map(int,input("Digite o código do produto e a quantidade (separados por espaço): ").split())

precos = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.00
}

total = precos[codigo]

print("Total: R$:{total: .2f}")

#Continue 