
# 🐍 Lógica de Programação com Python

Este repositório tem como objetivo compartilhar a minha jornada de estudos em lógica de programação utilizando a linguagem **Python**. Aqui você encontrará conceitos introdutórios, exemplos práticos e anotações essenciais.

> **Material de Apoio:** [Ebook - Introdução ao Python (Editora IFRN)](link_aqui)

---

## 📋 Índice
1. [Instalação e Configuração](#-instalação-e-configuração)
2. [Ferramentas (IDEs)](#-ferramentas-ides)
3. [Variáveis e Tipos de Dados](#-variáveis-e-tipos-de-dados)
4. [Expressões e Operadores](#-expressões-e-operadores)
5. [Controle de Fluxo](#-controle-de-fluxo)
6. [Estruturas de Repetição](#-estruturas-de-repetição)
7. [Estruturas de Dados](#-estruturas-de-dados)
8. [Modularização e Funções](#-modularização-e-funções)
9. [Cores no Terminal](#-cores-no-terminal)
10. [Glossário](#-glossário)

---

## 🛠 Instalação e Configuração

Se você já tem o Python instalado, pode pular esta etapa! Caso contrário, ou se quiser verificar, siga os passos abaixo.

### Verificar Instalação
No terminal (ou CMD), digite:
```bash
python --version
# Ou
python3 --version

```

*Retorno esperado:* `Python 3.11.x` (ou superior).

### Passo a Passo (Windows)

1. Acesse o site oficial: [python.org](https://www.python.org/downloads/).
2. Baixe a versão estável mais recente (ex: 3.11+).
3. Execute o instalador.
4. **IMPORTANTE:** Marque a opção **"Add Python to PATH"** na primeira tela. Isso permite executar o Python de qualquer lugar no terminal.
5. Selecione "Install Now" ou "Customize installation" se desejar escolher locais específicos.
6. Após finalizar, abra o CMD (Win + R > `cmd`) e digite `python` para testar.

---

## 💻 Ferramentas (IDEs)

### IDLE

O IDLE é a IDE padrão que vem instalada junto com o Python.

* **Prós:** Simples, leve, possui *highlight* de sintaxe e depurador.
* **Uso:** Ótimo para testes rápidos e para quem está começando a aprender a sintaxe básica sem distrações.

### PyCharm

Uma das IDEs mais populares para desenvolvimento profissional em Python, criada pela JetBrains.

* **Prós:** Autocomplete inteligente, ferramentas de refatoração, integração com Git e ambiente robusto.
* **Uso:** Recomendado para projetos maiores e organização de múltiplos arquivos.

---

## 📦 Variáveis e Tipos de Dados

Em Python, a tipagem é dinâmica (você não precisa declarar o tipo explicitamente).

* **Regras de Nomenclatura:**
* Podem conter letras, números e `_`.
* Não podem começar com números.
* *Case-sensitive* (`valor` é diferente de `Valor`).



### Tipos Primitivos

| Tipo | Descrição | Exemplo |
| --- | --- | --- |
| `int` | Inteiros | `10`, `-5` |
| `float` | Ponto Flutuante | `10.5`, `3.14` |
| `str` | Strings (texto) | `"Olá"`, `'Python'` |
| `bool` | Booleanos | `True`, `False` |
| `list` | Listas | `[1, 2, 3]` |
| `dict` | Dicionários | `{'chave': 'valor'}` |

> Consulte os exemplos na pasta: `ex001`

---

## 🧮 Expressões e Operadores

### Aritméticos

Precedência: `()` → `**` → `* / // %` → `+ -`

```python
5 + 3        # 8 (Soma)
2 ** 3       # 8 (Exponenciação)
10 // 3      # 3 (Divisão inteira)
10 % 3       # 1 (Resto da divisão)

```

### Lógicos

Usados para conectar condições.

* `and`: Retorna True se ambos forem verdadeiros.
* `or`: Retorna True se pelo menos um for verdadeiro.
* `not`: Inverte o valor (True vira False).

### Relacionais

Comparação entre valores. Retorna sempre `True` ou `False`.

* `==` (Igual), `!=` (Diferente), `>` (Maior), `<` (Menor), `>=` (Maior Igual), `<=` (Menor Igual).

> Consulte os exemplos: `ex002`, `ex003`

---

## 🚦 Controle de Fluxo

Estruturas condicionais permitem que o código tome decisões.

```python
if condicao:
    # executa se verdadeiro
elif outra_condicao:
    # executa se a primeira for falsa e esta verdadeira
else:
    # executa se nenhuma das anteriores for verdadeira

```

---

## 🔄 Estruturas de Repetição

### While (Enquanto)

Repete um bloco enquanto a condição for verdadeira. Usado quando não sabemos o número exato de repetições.

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1

```

### For (Para)

Itera sobre uma sequência (lista, string, range).

```python
for item in range(0, 5):
    print(item)

```

> **Controle:**
> * `break`: Interrompe o loop.
> * `continue`: Pula para a próxima iteração.
> 
> 

> Consulte os exemplos: `ex006`, `ex007`

---

## 📚 Estruturas de Dados

### 1. Listas `[]`

Mutáveis, ordenadas e aceitam duplicatas.

```python
lista = [1, "Python", 3.5]
lista.append(4) # Adiciona item

```

### 2. Tuplas `()`

**Imutáveis** (não podem ser alteradas após criadas). Mais rápidas que listas e protegem os dados.

```python
tupla = (1, 2, 3)

```

### 3. Sets (Conjuntos) `{}`

Desordenados e **não aceitam duplicatas**. Ótimos para operações matemáticas (união, interseção).

```python
conjunto = {1, 2, 3, 3} # Resulta em {1, 2, 3}

```

### 4. Dicionários `{}`

Estrutura de Chave: Valor. As chaves devem ser únicas.

```python
pessoa = {'nome': 'Everton', 'idade': 25}
print(pessoa['nome'])

```

---

## 🧩 Modularização e Funções

Dividir para conquistar! Modularizar torna o código reutilizável e legível.

### Funções

```python
def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Mundo"))

```

### Escopo

* **Local:** Variável existe apenas dentro da função.
* **Global:** Variável acessível em todo o código.

### Bibliotecas

Use o `pip` para instalar bibliotecas de terceiros e `import` para usá-las.

* **Padrão:** `os`, `math`, `datetime` (já vêm no Python).
* **Terceiros:** `pandas`, `flask` (instalar via pip).

> Consulte os exemplos: `ex030`, `ex035`, `ex036`

---

## 🎨 Cores no Terminal (ANSI)

Você pode estilizar a saída no terminal usando códigos ANSI.
Sintaxe: `\033[style;text;backm`

**Exemplos básicos:**

* `\033[31m`: Texto Vermelho
* `\033[32m`: Texto Verde
* `\033[1m`: Negrito
* `\033[0m`: Resetar formatação (Sempre use ao final!)

> Consulte o exemplo: `ex004`

---

## 📖 Glossário

* **Interpretador:** É o programa responsável por ler o seu código fonte (escrito em Python) e executá-lo instrução por instrução. Diferente de linguagens compiladas, o Python é interpretado em tempo de execução.
* **Linguagem de Máquina:** É a linguagem de mais baixo nível, composta apenas por códigos binários (0s e 1s), que é a única coisa que o processador do computador realmente entende diretamente. O interpretador Python traduz seu código para algo que a máquina possa processar.

---

*Bons estudos!* 🚀

