#Beatriz Paulino
#EX05

pontuacao = []
def crescente(pontuacao):
    for i in range(len(pontuacao)):
        for j in range(i + 1, len(pontuacao)):
            if pontuacao[i] > pontuacao[j]:
                pontuacao[i], pontuacao[j] = pontuacao[j], pontuacao[i]
    print(f"Pintuação em ordem cresecente: {pontuacao}")
    print(f"O jogador com a maior pontuação é o {len(pontuacao)}º jogador com {pontuacao[-1]} pontos.")
    return pontuacao

def main():
    cont = 1
    while cont <= 10:
        pontuacao.append(int(input(f"Digite a pontuação do {cont}º jogador: ")))
        cont += 1
    crescente(pontuacao)

main()

