
def menu():
    print(
    """
        MENU:
    1- Adicionar no Início
    2- Adicionar no final
    3- Exibir Primeiro
    4- Exibir Último
    5- Remover Primeiro
    6- Remover Último
    7- Exibir Todos
    0- Sair 
    """
    )
    
def adicionar_inicio(deque_qualquer, valor):
    deque_qualquer.insert(0, valor)
    print(f"O valor {valor} foi adicionado ao inicio")
    
def adicionar_final(deque_qualquer, valor):
    deque_qualquer.append(valor)
    print(f"O valor {valor} foi adicionado ao final")
    
def exibir_primeiro(deque_qualquer):
    print(f"O primeiro elemento é {deque_qualquer[0]}")
    
def exibir_ultimo(deque_qualquer):
    print(f"O ultimo elemento é {deque_qualquer[-1]}")
    
def remover_first(deque_qualquer):
    if not deque_qualquer:
        print("deque vasio !!")
    else:
        elemento = deque_qualquer.pop(0)
        print(f"O valor {elemento} foi removido !!")
    
def remover_last(deque_qualquer):
    if not deque_qualquer:
        print("deque vasio !!")
    else:
        elemento = deque_qualquer.pop()
        print(f"O valor {elemento} foi removido !!")
    

meu_deque = ['1' ,'2' ,'3' ,'4' ,'5' ,'6' ,'7' ,'8' ,'9' ,'10']

while True:
        menu()   
        try:
            opc = int(input("Digite uma opção: "))
        except ValueError:
            print("Opção inválida. Digite um número válido.")
            continue

        if opc == 1:
            valor = input("informe o elemento a ser inserido por primeiro: ")
            adicionar_inicio(meu_deque, valor)
    
        elif opc == 2:
            valor = input("Informe o elemento a ser inserido por ultimo: ")
            adicionar_final(meu_deque, valor)
        elif opc == 3:
            exibir_primeiro(meu_deque)
        elif opc == 4:
            exibir_ultimo(meu_deque)
        elif opc == 5:
            remover_first(meu_deque)
        elif opc == 6:
            remover_last(meu_deque)
        elif opc == 7:
            print(meu_deque)
        elif opc == 0:
            break
        else:
            print("Escolha uma opção do MENU!")