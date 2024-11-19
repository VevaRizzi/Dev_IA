matricula = int(input("Digite a matricula do colaborador: "))
horas_trabalhadas = int(input("Digite quantas horas trabalhadas o colaborador teve: "))
valor_hora = float(input("Digite o valor que o colaborador recebe por hora: "))
#lembrete: float para número com casa decimal


salario = horas_trabalhadas * valor_hora

print(f"NUMBER = {matricula}")
print(f"SALARY = U$ {salario: .2f}") #.2f seria a quantidade de casas decimais, após a virgula

