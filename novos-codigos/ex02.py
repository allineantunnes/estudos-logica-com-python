# Exercício 2
# Algoritimo que usar um dicionario para armazenar os dados de um aluno, como nome, idade e curso. Em seguida, o programa deve imprimir essas informações na tela.
aluno = {
    "nome": "João",
    "idade": 20,
    "curso": "Engenharia"
}
print("Nome:", aluno["nome"])
print("Idade:", aluno["idade"])
print("Curso:", aluno["curso"])

# Adicionando mais informações ao dicionário
aluno["matricula"] = "2023001"
print("Matrícula:", aluno["matricula"])

# Adicionando outro aluno ao dicionário
aluno2 = {
    "nome": "Maria",
    "idade": 22,
    "curso": "Medicina",
    "matricula": "2023002"
}
print("\nInformações do segundo aluno:")
print("Nome:", aluno2["nome"])
print("Idade:", aluno2["idade"])
print("Curso:", aluno2["curso"])
print("Matrícula:", aluno2["matricula"])    
