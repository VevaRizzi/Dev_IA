n = int(input()) # 7 casos de teste
# entre o valor X e o valor Y
# ele quer que eu some todos os valores entre X e Y

"""
Se x = 7
y = 4 

7,8,9,10,11 
"""

for _ in range(n): #valor de variável _ (mantém o tipo e descarta a variável)
    x,y = map(int,input().split())
    if x > y:
        x,y = y, x

    soma = sum( i for i in range(x + 1, y) if i % 2 != 0) #é impar
    print(soma)
