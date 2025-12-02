# Algoritmo: Gerenciador de Notas de Alunos
# Demonstra conceitos de variáveis e listas em Python
# Testedo em: Python 3.8+
# ========== VARIÁVEIS ==========
nome_escola = "Escola de Programação"
ano_letivo = 2024
professor = "João Silva"

print("=" * 50)
print(f"Bem-vindo ao {nome_escola}")
print(f"Professor: {professor} | Ano: {ano_letivo}")
print("=" * 50)
print()

# ========== LISTAS ==========
# Lista de nomes dos alunos
alunos = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"]

# Lista de notas (correspondentes aos alunos)
notas = [8.5, 9.0, 7.5, 9.5, 8.0]

# Lista vazia para armazenar resultados
situacao = []

print("ALUNOS E SUAS NOTAS:")
print("-" * 50)

# ========== PROCESSAMENTO ==========
# Iterar sobre os alunos e suas notas
for i in range(len(alunos)):
    aluno = alunos[i]
    nota = notas[i]
    
    # Determinar a situação do aluno
    if nota >= 7.0:
        status = "Aprovado"
    else:
        status = "Reprovado"
    
    # Adicionar resultado à lista
    situacao.append(status)
    
    # Exibir informações
    print(f"{aluno:15} | Nota: {nota:5.1f} | {status}")

print("-" * 50)
print()

# ========== ESTATÍSTICAS ==========
print("ESTATÍSTICAS DA TURMA:")
print("-" * 50)

# Calcular média
media_turma = sum(notas) / len(notas)
print(f"Média da turma: {media_turma:.2f}")

# Nota máxima
nota_maxima = max(notas)
indice_max = notas.index(nota_maxima)
print(f"Maior nota: {nota_maxima} ({alunos[indice_max]})")

# Nota mínima
nota_minima = min(notas)
indice_min = notas.index(nota_minima)
print(f"Menor nota: {nota_minima} ({alunos[indice_min]})")

# Quantidade de aprovados
aprovados = situacao.count("Aprovado")
reprovados = situacao.count("Reprovado")
print(f"Aprovados: {aprovados} | Reprovados: {reprovados}")

print("-" * 50)
print()

# ========== LISTAS AVANÇADAS ==========
print("INFORMAÇÕES COMBINADAS (Dicionário dentro de Lista):")
print("-" * 50)

# Criar uma lista de dicionários
dados_alunos = []
for i in range(len(alunos)):
    dados_alunos.append({
        "nome": alunos[i],
        "nota": notas[i],
        "situacao": situacao[i]
    })

# Exibir dados estruturados
for dado in dados_alunos:
    print(f"{dado['nome']}: {dado['nota']} - {dado['situacao']}")

print()
print("=" * 50)
print("Algoritmo finalizado com sucesso!")
print("=" * 50)
