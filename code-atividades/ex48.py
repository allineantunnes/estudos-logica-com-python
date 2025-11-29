heroi = {
    "nome": "Aragorn",
    "exp": 5040,
    "nivel": None
}

niveis = {
    "Ferro": {
        "min": 0,
        "max": 1000
    },
    "Bronze": {
        "min": 1001,
        "max": 2000
    },
    "Prata": {
        "min": 2001,
        "max": 5000
    },
    "Ouro": {
        "min": 5001,
        "max": 7000
    },
    "Platina": {
        "min": 7001,
        "max": 8000
    },
    "Ascendente": {
        "min": 8001,
        "max": 9000
    },
    "Imortal": {
        "min": 9001,
        "max": 10000
    },
    "Radiante": {
        "min": 10001,
        "max": float('inf')
    }
};


for nivel, faixa in niveis.items():
    if faixa["min"] <= heroi["exp"] <= faixa["max"]:
        heroi["nivel"] = nivel
        print(f"O Herói {heroi['nome']} está no nível {nivel}")
        break