# Crie um codigo em python para calcular o tempo de uma viagem dando opções de ônibus, carro, moto e avião com base na distância e na velocidade do veículo.,

def calcular_tempo_viagem(distancia, velocidade, meio_de_transporte):
    # Calcula o tempo de viagem
    tempo = distancia / velocidade

    # Retorna o tempo de viagem
    return tempo

def main():
    # Solicita ao usuário a distância da viagem em quilômetros
    distancia = float(input("Digite a distância da viagem (em quilômetros): "))

    # Solicita ao usuário a velocidade do veículo em km/h
    velocidade = float(input("Digite a velocidade do veículo (em km/h): "))

    # Solicita ao usuário o meio de transporte desejado
    meio_de_transporte = input("Escolha o meio de transporte (onibus, carro, moto, aviao): ").lower()

    # Verifica o meio de transporte e calcula o tempo de viagem correspondente
    if meio_de_transporte == "onibus":
        tempo_viagem = calcular_tempo_viagem(distancia, velocidade, meio_de_transporte)
        print("Tempo de viagem de ônibus: {:.2f} horas".format(tempo_viagem))
    elif meio_de_transporte == "carro":
        tempo_viagem = calcular_tempo_viagem(distancia, velocidade, meio_de_transporte)
        print("Tempo de viagem de carro: {:.2f} horas".format(tempo_viagem))
    elif meio_de_transporte == "moto":
        tempo_viagem = calcular_tempo_viagem(distancia, velocidade, meio_de_transporte)
        print("Tempo de viagem de moto: {:.2f} horas".format(tempo_viagem))
    elif meio_de_transporte == "aviao":
        tempo_viagem = calcular_tempo_viagem(distancia, velocidade, meio_de_transporte)
        print("Tempo de viagem de avião: {:.2f} horas".format(tempo_viagem))
    else:
        print("Meio de transporte não reconhecido. Por favor, escolha entre onibus, carro, moto ou aviao.")

if __name__ == "__main__":
    main()
