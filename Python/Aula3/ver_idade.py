#Esse código verifica a idade se é maior de idade, se é adolescente ou se é uma criança

idade = input("Digite a sua idade: ")

#se vc tiver mais de 18 anos, vc é maior de idade
if idade >= 18:
    print("Vocé é maior de idade")

#se vc tiver menor de 18 anos, vc é menos de idade
elif 12 <= idade < 18:
    print("Vocé é menor de idade")

#se vc tiver menos de 12 anos vc é uma criança
else:
    print("Vocé é uma criança")