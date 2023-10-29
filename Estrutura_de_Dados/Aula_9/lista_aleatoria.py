import random
import time

lista_original = []

def menu():
    print("""
        1-Adicionar numero:
        2-Adicionar aleatoria:
        3-Mostrar lista:
        4-Selection lista:
        5-Bubble Sort:
        6-Insertion Sort:
        7-Merge Sort:
        8-Quick Sort1:
        9-Quick sort2:
        100-Limpar lista:
        0-Sair
    """)

def enfileirar(listagenerica, valor):
    listagenerica.append(valor)
    
def aleatorio(lista, qtd):
    while len(lista) < qtd :
        aleatorio = random.randint(1, 10)
        if aleatorio not in lista:
            enfileirar(lista, aleatorio)
            
def cronometro(algoritmo, lista):
    inicio = time.time()
    algoritmo(lista.copy())
    fim = time.time()
    tempo = fim - inicio
    print(f"Tempo  de processamento: {tempo:.32f} segundos")

def selection_sort(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[i]:
                aux = lista[j]
                lista[j] = lista[i]
                lista[i] = aux   
    
def bubble_sort(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - 1, i, -1):
            if lista[j] < lista[j - 1]:
                aux = lista[j]
                lista[j] = lista[j - 1]
                lista[j - 1] = aux
    
def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and chave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
        
def merge_sort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        metade_esquerda = lista[:meio]
        metade_direita = lista[meio:]

        merge_sort(metade_esquerda)
        
        merge_sort(metade_direita)
        
        i = j = k = 0
        
        while i < len(metade_esquerda) and j < len(metade_direita):
            if metade_esquerda[i] < metade_direita[j]:
                lista[k] = metade_esquerda[i]
                i += 1
            else:
                lista[k] = metade_direita[j]
                j += 1
            k += 1
            
        while i < len(metade_esquerda):
            lista[k] = metade_esquerda[i]
            i += 1
            k += 1
            
        while j < len(metade_direita):
            lista[k] = metade_direita[j]
            j += 1
            k += 1
             
def quick_sort2(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[0]
        menores = [x for x in lista[1:] if x <= pivot]
        maiores = [x for x in lista[1:] if x > pivot]
        ordenados = quick_sort2(menores) + [pivot] + quick_sort2(maiores)
        return ordenados
        
def quick_sort1(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[0]
        menores = []
        maiores = []
        
        for x in lista[1:]:
            if x <= pivot:
                menores.append(x)
            else:
                maiores.append(x)
        menores_ordenados = quick_sort1(menores)
        maiores_ordenados = quick_sort1(maiores)
        ordenados = menores_ordenados + [pivot] + maiores_ordenados
        return ordenados
               
while True:
    menu()
    try:
            opc = int(input("Digite uma opção: "))
    except ValueError:
        print("Opção inválida. Digite um número válido.")
        continue
    if opc == 1:
        entrada = input("Digite os valores para empilhar (separados por vírgula): ")
        valores_separados = entrada.split(",")

        for valor_str in valores_separados:
            try:
                valor = int(valor_str)
                enfileirar(lista_original, valor)
            except ValueError:
                print(f"Valor inválido: {valor_str}")
    elif opc == 2:
        quantidade = int(input("escolha a quantidade de elementos na lista: "))
        aleatorio(lista_original, quantidade)
    elif opc == 3:
        print(lista_original)
    elif opc == 4:
        cronometro(selection_sort, lista_original)
    elif opc ==5: 
        cronometro(bubble_sort, lista_original)
    elif opc ==6: 
        cronometro(insertion_sort, lista_original)
    elif opc ==7: 
        cronometro(merge_sort, lista_original)
    elif opc ==8: 
        cronometro(quick_sort1, lista_original)
    elif opc ==9: 
        cronometro(quick_sort2, lista_original)
    elif opc == 100:
        lista_original.clear()
    elif opc == 0:
        break