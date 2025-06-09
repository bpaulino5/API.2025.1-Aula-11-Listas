#Beatriz Paulino
#EX06

tarefas = ["Estudar",
           "Comprar pão",
           "Fazer Exercício",
           "Responder e-mails"]

nova_tarefa = input("Digite um nova tarefa: ")
tarefas.append(nova_tarefa)
print(f"Lista de tarefas: {tarefas}")
tarefas.remove(tarefas[1])
tarefas.reverse()
print(f"Lista de tarefas após remoção e reversão: {tarefas}")


