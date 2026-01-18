# Lógica de Programação

Este repositório tem como objetivo compartilhar meus estudos de lógica de programação utilizando **Python**. Abaixo, apresento algumas informações introdutórias e um link com a história e detalhes da linguagem.

**Link sugerido:** [Ebook - Introdução ao Python - Editora IFRN](https://memoria.ifrn.edu.br/bitstream/handle/1044/2090/EBOOK%20-%20INTRODU%C3%87%C3%83O%20A%20PYTHON%20%28EDITORA%20IFRN%29.pdf?sequence=1&isAllowed=y)

---

### Instalação

Se você já possui o Python instalado, pode pular esta etapa. Caso não saiba se possui, ou esqueceu como verificar, siga o passo abaixo:

**No CMD (Terminal):**
Digite: `python --version`

O retorno esperado, caso o Python esteja configurado corretamente, será algo como: `Python 3.11.2`

#### Passo a passo para instalação:

1. Acesse o site oficial [python.org](https://www.python.org) e vá à seção de downloads.
2. Escolha a versão estável mais recente (ex: `Python 3.12.x`). Certifique-se de baixar a versão correspondente ao seu sistema operacional (x64 ou x86).
3. Execute o instalador baixado.
4. **IMPORTANTE:** Na primeira tela, marque a opção **"Add Python to PATH"**. Isso permite que você execute o comando `python` em qualquer diretório do seu sistema.
5. Selecione **"Customize installation"** para garantir a instalação de ferramentas essenciais como o **pip** (gerenciador de pacotes) e o **IDLE**.
6. Avance e aguarde a conclusão. Após o término, reinicie o terminal e teste o comando `python --version` novamente.

---

### Linguagem Python

#### Interpretador IDLE

O Python pode ser utilizado de várias formas. O **IDLE** é o ambiente de desenvolvimento integrado simples que acompanha a instalação padrão. Ele é excelente para testes rápidos e aprendizado inicial.

* **Recursos do IDLE:** Possui realce de sintaxe (*syntax highlighting*), execução interativa de código (Shell), depurador (*debugger*) e autocompletar. Sua principal vantagem é o **REPL** (Read-Eval-Print Loop), que permite ver o resultado das instruções imediatamente.

#### PyCharm

Para projetos mais robustos, utilizamos o **PyCharm**. Ele é uma **IDE** (Ambiente de Desenvolvimento Integrado) profissional desenvolvida pela JetBrains, que oferece ferramentas avançadas de análise de código, integração com bancos de dados e sistemas de controle de versão (Git).

---

### Variáveis e Atribuição

1. **Tipagem Dinâmica:** Você não precisa declarar o tipo da variável (ex: int, string). O Python infere o tipo automaticamente com base no valor atribuído.
2. **Atribuição:** Utilizamos o operador `=` para armazenar um valor em uma variável.
3. **Nomenclatura:**
* Pode conter letras, números e *underline* (`_`).
* **Não** pode começar com números.
* Python é **case-sensitive** (diferencia maiúsculas de minúsculas). `valor` e `Valor` são variáveis distintas.


4. **Tipos de Dados Comuns:** `int` (inteiros), `float` (ponto flutuante/decimais), `str` (textos/strings), `list` (listas), `dict` (dicionários) e `bool` (booleanos: True/False).

---

### Expressões e Operadores

#### **Aritméticas:**

* `+`, `-`, `*`, `/` (Divisão real), `//` (Divisão inteira), `%` (Resto), `**` (Exponenciação).
* **Precedência:** Parênteses `()` > Exponenciação `**` > Multiplicação/Divisão > Adição/Subtração.

#### **Relacionais (Comparações):**

* `==` (Igual), `!=` (Diferente), `>`, `<`, `>=`, `<=`.

#### **Lógicas:**

* `and` (E), `or` (OU), `not` (NÃO).

---

### Controle de Fluxo

Python utiliza a **identação** (espaços no início da linha) para organizar os blocos de código.

1. **Condicionais (`if`, `elif`, `else`):** Executam blocos baseados em testes lógicos.
2. **Repetição (`for`):** Ideal para iterar sobre sequências (listas, strings) ou intervalos numéricos usando `range()`.
3. **Repetição (`while`):** Executa enquanto uma condição for verdadeira.
4. **Interrupções:** `break` encerra o loop; `continue` pula para a próxima iteração.

---

### Estruturas de Dados

* **Listas `[]`:** Mutáveis e ordenadas. Podem conter tipos diferentes.
* **Tuplas `()`:** **Imutáveis**. São mais rápidas que as listas e garantem a segurança dos dados contra alterações acidentais.
* **Sets `{}`:** Coleções não ordenadas de elementos **únicos**. Ótimos para operações matemáticas de conjunto (união, interseção).
* **Dicionários `{'chave': 'valor'}`:** Estruturas baseadas em chave-valor. Ideais para organizar dados de forma rotulada (como um cadastro).

---

### Modularização e Funções

Dividir o código em partes menores facilita a manutenção e reutilização.

* **Escopo:** Variáveis **locais** existem apenas dentro da função. Variáveis **globais** são acessíveis em todo o script.
* **Passagem de Parâmetros:**
* **Objetos Imutáveis (int, str):** Comportam-se como "passagem por valor" (a função não altera o original).
* **Objetos Mutáveis (listas, dicionários):** Comportam-se como "passagem por referência" (alterações dentro da função refletem no objeto original).



---

### Bibliotecas

Bibliotecas são coleções de módulos que evitam "reinventar a roda".

* **Standard Library:** Já vem com o Python (ex: `math`, `datetime`, `os`).
* **Third-party (Terceiros):** Instaladas via `pip` (ex: `pandas`, `requests`, `numpy`).

---


### Programação Orientada a Objetos (POO)

A Programação Orientada a Objetos é um paradigma de programação que utiliza "objetos" para representar dados e métodos. Em Python, quase tudo é um objeto. Esse modelo ajuda a organizar códigos complexos, tornando-os mais modulares e reutilizáveis.

#### **Os 4 Pilares da POO**

1. **Abstração:** Esconder detalhes complexos e mostrar apenas as funcionalidades essenciais.
2. **Encapsulamento:** Protege os dados dentro de uma classe, restringindo o acesso direto a variáveis internas.
3. **Herança:** Permite que uma classe (filha) herde características e comportamentos de outra classe (pai).
4. **Polimorfismo:** Permite que diferentes classes sejam tratadas de forma uniforme, mesmo que seus métodos tenham comportamentos diferentes.

#### **Classes e Objetos**

* **Classe:** É o "molde" ou a "planta" para criar algo. Por exemplo, uma planta de uma casa.
* **Objeto:** É a instância real da classe. Por exemplo, a casa construída a partir da planta.

#### **O Método `__init__` e o `self**`

Em Python, o método `__init__` é o **construtor**. Ele é chamado automaticamente quando criamos um novo objeto. O parâmetro `self` é fundamental: ele representa a própria instância do objeto e permite acessar seus atributos e métodos.

**Exemplo prático:**

```python
class Carro:
    # Construtor: define as características (atributos)
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    # Método: define o que o objeto faz (comportamento)
    def acelerar(self):
        print(f"O {self.modelo} está acelerando!")

# Criando um objeto (instanciando a classe)
meu_carro = Carro("Toyota", "Corolla")
print(meu_carro.marca) # Saída: Toyota
meu_carro.acelerar()   # Saída: O Corolla está acelerando!

```

#### **Por que usar POO?**

Utilizar POO em Python facilita a manutenção do sistema. Se você precisar alterar o comportamento de todos os "Carros" do seu programa, basta alterar o código dentro da classe `Carro`, e todos os objetos criados a partir dela serão atualizados automaticamente.

---
