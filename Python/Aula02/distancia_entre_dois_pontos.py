#Exercício 2.5
#Cálculo da disância entre dois pontos
#distancia = raiz de (x2 - x1)  **2 + (y2 - y1) **2

x1, x2 = map(float, input("Digite as coordenadas x1 e x2:").split())
y1, y2 = map(float, input("Digite as coordenadas y2 e y2:").split())

distancia = math.sqrt((x2 - x1) **2 + (y2 - y1)**2)

print(f"{distancia: .4f}")