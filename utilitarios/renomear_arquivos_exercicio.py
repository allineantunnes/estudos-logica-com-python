import os
import re

# 02/10/2025
# Desenvolvido por @LeonardoAragaoDev 
# em contribuição com o repositório para aula 
# de contribuição em um projeto Open Source da DIO.

# --- CONFIGURAÇÃO ---
# O diretório onde os arquivos de exercícios ('.' significa o diretório atual)
DIRETORIO_RAIZ = './code-atividades' 
# Padrão de nome de arquivo esperado: "ex" seguido por um número e ".py"
# O padrão de busca foi alterado para ser mais genérico e pegar todos os .py
# para então renomear:
PADRAO_BUSCA = re.compile(r".*\.py$", re.IGNORECASE) 
# PADRAO_ARQUIVO_EXISTENTE verifica se o arquivo *já* tem o formato "ex[número].py"
PADRAO_ARQUIVO_EXISTENTE = re.compile(r"^ex(\d+)\.py$", re.IGNORECASE)


def padronizar_arquivos_por_contagem(diretorio):
    """
    Lista todos os arquivos .py na pasta, calcula o padding com base na contagem total
    e renomeia sequencialmente (ex001.py, ex002.py, etc.).
    """
    if not os.path.isdir(diretorio):
        print(f"Erro: O diretório '{diretorio}' não foi encontrado.")
        return

    # 1. Coletar e ordenar todos os arquivos .py que parecem ser exercícios
    arquivos_py = []
    for nome_arquivo in os.listdir(diretorio):
        # AQUI usamos o PADRAO_ARQUIVO_EXISTENTE se o objetivo é só renomear
        # arquivos que *já* estão no formato "ex[número].py", mas sem o padding correto.
        # Se você quiser renomear QUALQUER .py, use PADRAO_BUSCA.
        # Mantendo a lógica anterior que pega arquivos que já estão no padrão "ex[num].py" (mas podem estar mal formatados)
        if PADRAO_ARQUIVO_EXISTENTE.match(nome_arquivo):
            arquivos_py.append(nome_arquivo)

    if not arquivos_py:
        print("Nenhum arquivo .py com o padrão 'ex[número].py' encontrado no diretório.")
        return

    # IMPORTANTE: Garante uma ordem lógica para a sequenciação.
    arquivos_py.sort(key=str.lower)

    total_arquivos = len(arquivos_py)
    # Inicializa o contador de renomeações
    arquivos_renomeados = 0 

    # 2. Determinar o número mínimo de dígitos (padding)
    padding_necessario = len(str(total_arquivos))
    
    # Lógica de padding ajustada para garantir um mínimo de 2 ou 3 dígitos se necessário
    if total_arquivos > 9 and padding_necessario < 2:
        padding_necessario = 2 
    elif total_arquivos > 99 and padding_necessario < 3:
        padding_necessario = 3
    
    # 3. Renomear os arquivos sequencialmente
    print(f"Total de arquivos encontrados: {total_arquivos}. Padding necessário: {padding_necessario} dígitos.")

    for indice, nome_original in enumerate(arquivos_py, start=1):
        # O número sequencial (1, 2, 3, ...) formatado com zeros à esquerda
        novo_numero_str = str(indice).zfill(padding_necessario)
        
        # Constrói o novo nome no formato ex[número].py
        novo_nome = f"ex{novo_numero_str}.py"
        
        caminho_antigo = os.path.join(diretorio, nome_original)
        caminho_novo = os.path.join(diretorio, novo_nome)
        
        # Verifica se o nome precisa ser alterado
        if nome_original != novo_nome:
            try:
                os.rename(caminho_antigo, caminho_novo)
                print(f"Renomeado: {nome_original} -> {novo_nome}")
                # Incrementa o contador
                arquivos_renomeados += 1
            except FileNotFoundError:
                print(f"Aviso: Arquivo {nome_original} não encontrado, pode já ter sido renomeado.")
        else:
            # Caso o arquivo já esteja com o nome padronizado
            pass # Não precisa imprimir nada ou incrementar o contador

    # --- NOVO FEEDBACK ---
    print("-" * 30)
    if arquivos_renomeados > 0:
        print(f"Processo de padronização concluído. {arquivos_renomeados} arquivo(s) renomeado(s).")
    else:
        print("Nenhum arquivo com o nome fora do padrão para ser renomeado.")


if __name__ == "__main__":
    padronizar_arquivos_por_contagem(DIRETORIO_RAIZ)