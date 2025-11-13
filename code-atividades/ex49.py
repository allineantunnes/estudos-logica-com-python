from datetime import datetime

#!/usr/bin/env python3
# ex49.py - Cumprimenta o usuário conforme o horário do dia


def saudacao_por_hora(hora: int) -> str:
    if 6 <= hora < 12:
        return "Bom dia"
    if 12 <= hora < 18:
        return "Boa tarde"
    return "Boa noite"

def main():
    nome = input("Digite seu nome: ").strip()
    if not nome:
        nome = "usuário"
    agora = datetime.now()
    hora = agora.hour
    minuto = agora.minute
    saudacao = saudacao_por_hora(hora)
    print(f"{saudacao}, {nome}! São {hora:02d}:{minuto:02d}.")

if __name__ == "__main__":
    main()