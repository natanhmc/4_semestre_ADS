# PILHA -----------------------------------------------------------------------------------------------------
lista = []
lista_2 = []

def obter_numeros(entrada):
    for item in entrada:
        try:
            numero = float(item)
            lista.append(numero)
        except ValueError:
            print (f"valor invalido: {item}, ignorando este valor.")
            
    return lista
        

print ("""
       Menu de Opções:
       1-Para adicionar um numero:
       2-Remover ultimo:
       3-Para limpar a lista
       4-Mostra o ultimo da pilha
       5-Para mostrar a pilha
       6-Para mostrar a pilha excluida
       0-Para sair: 
       """)


while True:
    opc = int(input("Infome a opção :"))
    
    if opc == 1:
        entrada = input("informe uma lista de numeros separados por vircula(,): ").split(",")
        lista = obter_numeros(entrada) 
        print(lista)  
    elif opc == 2:
        lista_2.append(lista[-1])
        lista.pop()   
    elif opc == 3:
        lista.clear()
    elif opc == 4:
        print (lista[-1])
    elif opc == 5:
        print(lista)   
    elif opc == 6:
        print(lista_2)    
    elif opc == 0:
        break
    
    else:
        print ("Opção incorreta!! informe um numero válido!!")
            
            

