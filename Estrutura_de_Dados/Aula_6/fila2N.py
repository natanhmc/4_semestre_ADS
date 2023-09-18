def menu():
    print(
    """
    1-Emfileirar #enqueue
    2-Desenfileirar #dequeue
    3-exibir primeriro #first
    4-Exibir fila
    5-enfileirar prioritario
    6-desenfileirar prioritario
    7-exibir primeiro prioritario
    8-exibir fila prioritario
    9-chamar proximo
    10-exibir historico
    0-sair
    """
    )
    
def enfileirar(fila_qualquer, numero):
    fila_qualquer.append(numero)
    print(f"O valor {numero} foi enfileirado !!")
    
def desenfileirar(fila_qualquer):
    if not fila_qualquer:
        print("Fila vazia !!")
    else:
        numero = fila_qualquer[0]
        enfileirar(historico,numero)
        fila_qualquer.pop(0)
        print(f"O valor {numero} foi desenfileirado !!")
    
def mostrar(fila_qualquer):
    if not fila_qualquer:
        print("Fila vazia !!")
    else:
        print(fila_qualquer)
        
def print_pilha(uma_pilha):
    if not uma_pilha:
        print("A pilha está vazia.")
    else:
        print("Conteúdo da pilha:")
        for valor in reversed(uma_pilha):
            print(valor)
        

    
fila = []
fila_prioritario = []
contador = 0
historico = []

while True:
    menu()   
    try:
        opc = int(input("Digite uma opção: "))
    except ValueError:
        print("Opção inválida. Digite um número válido.")
        continue
    if opc == 1:
        entrada = input("Digite os valores para enfileirar (separados por vírgula): ")
        valores_separados = entrada.split(",")
        for i in valores_separados:
            enfileirar(fila, i)
            
    elif opc == 2:
        desenfileirar(fila)
    elif opc == 3:
        print(fila[0])
    elif opc == 4:
        mostrar(fila)
    elif opc == 5:
        entrada = input("Digite os valores para enfileirar (separados por vírgula): ")
        valores_separados = entrada.split(",")
        for i in valores_separados:
            enfileirar(fila_prioritario, i)
    elif opc == 6:
        desenfileirar(fila_prioritario)

    elif opc == 7:
        print(fila_prioritario[0])

    elif opc == 8:
        mostrar(fila_prioritario)
    elif opc == 9:
            
        if contador < 3:
            if not fila_prioritario:
                print("fila vazia !!")
                contador = 4
            else:
                mostrar(f"Chamando {fila_prioritario[0]}")
                desenfileirar(fila_prioritario)
                contador += 1
        elif contador >= 4:
            if not fila:
                print("fila vazia !!")
            else:
                mostrar(f"Chamando {fila[0]}")
                desenfileirar(fila)
                contador = 0

    elif opc == 10:
            print_pilha(historico)
    elif opc == 0:
        break
    else:
        print("Escolha uma opção valida")
    