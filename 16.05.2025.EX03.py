#Beatriz Paulino
#EX03

notas = []

def calcular_media(notas):
    soma = 0 
    for nota in notas:
        soma += nota
    media = soma / len(notas)
    print(f"A média das notas é: {media:.2f}")
    return media

def notas_acima_media(notas, media):
    print("Notas acima da média: ")
    for i in range(len(notas)):
        if notas[i] > media:
            print(f"Nota {i+1}: {notas[i]:.2f}")

def notas_abaixo_media(notas, media):
    print("Notas abaixo da média: ")
    for i in range(len(notas)):
        if notas[i] < media:
            print(f"Nota {i+1}: {notas[i]:.2f}")    

def main():
    n = int(input("Quantas notas você deseja inserir? "))
    for i in range(n):
        nota = float(input(f"Digite a {i+1}ª nota: "))
        notas.append(nota)
    
    media = calcular_media(notas)
    notas_acima_media(notas, media)
    notas_abaixo_media(notas, media)

main()