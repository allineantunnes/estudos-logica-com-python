# Tratamento de Erro em Python
# O try-except é usado para capturar e tratar erros (exceções) de forma controlada

# Exemplo 1: Tratamento básico de erro
print("=== Exemplo 1: Divisão por zero ===")
try:
    numero = 10
    divisor = 0
    resultado = numero / divisor
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero!")

# Exemplo 2: Múltiplos tipos de erro
print("\n=== Exemplo 2: Múltiplos erros ===")
try:
    lista = [1, 2, 3]
    print(lista[10])  # Índice fora do alcance
except IndexError:
    print("Erro: Índice não existe na lista!")
except ValueError:
    print("Erro: Valor inválido!")

# Exemplo 3: Capturar qualquer erro (genérico)
print("\n=== Exemplo 3: Erro genérico ===")
try:
    numero = int("abc")  # Não pode converter string para inteiro
except Exception as e:
    print(f"Erro capturado: {e}")

# Exemplo 4: Usando else (executado se não houver erro)
print("\n=== Exemplo 4: Try-Except-Else ===")
try:
    numero = 20
    divisor = 2
    resultado = numero / divisor
except ZeroDivisionError:
    print("Erro: Divisão por zero!")
else:
    print(f"Sucesso! Resultado: {resultado}")

# Exemplo 5: Usando finally (sempre executado)
print("\n=== Exemplo 5: Try-Except-Finally ===")
try:
    arquivo = open("arquivo.txt", "r")
    conteudo = arquivo.read()
except FileNotFoundError:
    print("Erro: Arquivo não encontrado!")
finally:
    print("Bloco finally sempre é executado (limpeza de recursos)")

# Exemplo 6: Lançar um erro customizado
print("\n=== Exemplo 6: Raise (lançar erro) ===")
def verificar_idade(idade):
    if idade < 0:
        raise ValueError("Idade não pode ser negativa!")
    return f"Idade válida: {idade} anos"

try:
    print(verificar_idade(-5))
except ValueError as erro:
    print(f"Erro capturado: {erro}")

# Para quem estiver com dificuldades de intender sobre o assunto, você pode usar o Copilot para te auxiliar em seu entendimento, ou usando uma IA como o Chat GPT ou o Gemini.