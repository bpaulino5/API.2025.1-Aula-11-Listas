#Beatriz Paulino
#EX02

valor = []

def total(valor):
    soma = 0
    for i in range(len(valor)):
        soma += valor[i]
    return soma
    
def valor_acima_100(valor):
    print("Valores acima de R$100,00:")
    for i in range(len(valor)):
        if valor[i] > 100:
            print(f"Produto {i}: R${valor[i]:.2f}")

def main():
    n = int(input("Produtos comprados:"))
    for i in range(n):
        valor.append(float(input(f"Valor do {i}º produto: ")))

    total_valor = total(valor)
    print(f"Total gasto: R${total_valor:.2f}")
    valor_acima_100(valor)  

main()