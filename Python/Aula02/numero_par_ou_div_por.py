#enquanto o número(index) estiver entre (1 e 100)
#Se o número for divisível por dois com resto zero ou divisível por três com resto 0

# isso seria o chamado LOOP, e o for fará o loop 
# enquanto a condição for verdadeira

for i in range(1, 100):
    if i % 2 == 0 or i % 3 == 0:
        print(f"O número {i} é divisível por 2 ou por 3")

for i in range(1, 100):
    if i % 2 == 0 or i % 3 == 0:
        print(f"O número {i} é divisível por 2")

for i in range(1, 101):
    if i % 2 == 0 or i % 3 == 0:
        print(f"O número {i} é divisível por 10")
              
