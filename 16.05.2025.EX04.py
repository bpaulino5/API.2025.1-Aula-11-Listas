#Beatriz Paulino
#EX04 

consumo_medio = []

def calcular_combustivel(n):
    for i in range(n):
        distancia = float(input(f"Digite a distância da {i + 1}ª viagem (em km): "))
        combustivel = float(input(f"Digite o consumo de combustível da {i + 1}ª viagem (em litro): "))
        consumo = distancia / combustivel
        consumo_medio.append(consumo)
    
def calcular_media(consumo_medio, n):
    soma = 0
    for i in range(n):
        soma += consumo_medio[i]
    media = soma / n
    print(f"O consumo médio de combustível é: {media:.2f} km/L")

def main():
    n = int(input("Digite a quantidade de viagens percorridas: "))
    calcular_combustivel(n)
    calcular_media(consumo_medio, n)

main()
