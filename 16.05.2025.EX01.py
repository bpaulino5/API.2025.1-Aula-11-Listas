#16/05/2025 - Beatriz Paulino
#EX01
dias_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
temperaturas = []

def calcular_media(temperaturas):
    soma = 0
    for t in temperaturas:
        soma += t
    media = soma / 7
    print(f"A temperatura média da semana é: {media:.2f}°C")
    return media

def temperaturas_acima_media(temperaturas,media):
    print("Temperaturas acima da média:")
    for i in range(7):
        if temperaturas[i] > media:
            print(f"{dias_semana[i]}: {temperaturas[i]:.2f}°C") 

def main():
    print("Digite a temperatura média de cada dia da semana:")
    for i in range(7):
        temp = float(input(f"{dias_semana[i]}: "))
        temperaturas.append(temp)
    media = calcular_media(temperaturas)
    temperaturas_acima_media(temperaturas, media)

main()