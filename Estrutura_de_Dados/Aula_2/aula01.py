lista = []

print ("""
       Menu de Opções:
       1-Para adicionar um numero:
       2-Para excluir o primeiro elemento:
       3-Para excluir o ultimo elemento:
       4-Para adicionar um numero em primeiro lugar:
       5-Para mostrar a lista (array):
       6-Para excluir os numeros inpares:
       7-Para excluir os numeros pares:
       0-Para sair: 
       """)


while True:
    opc = int(input("Infome a opção :"))
    
    if opc == 1:
        num = int(input("Informe o numero:"))
        lista.append(num)
        
    elif opc == 2:
        lista.pop(0)
        
    elif opc == 3:
        lista.pop()
        
    elif opc == 4:
        num = int(input("Informe o numero:"))
        lista.insert(0,num)

    elif opc == 5:
        print (lista)
        
    elif opc == 6:
        for item in lista:
            if item % 2 == 1:
                lista.remove(item)
                
    elif opc == 7:
        for item in lista:
            if item % 2 == 0:
                lista.remove(item)
                
    elif opc == 0:
        break
    
    else:
        print ("Opção incorreta!! informe um numero válido!!")
            