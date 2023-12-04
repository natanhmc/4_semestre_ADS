from collections import deque

class Fila:
    def __init__(self):
        self.itens = deque()

    def enfileirar(self, valor):
        self.itens.append(valor)

    def desenfileirar(self):
        if len(self.itens) == 0:
            print("Fila vazia, não é possível desenfileirar.")
        else:
            return self.itens.popleft()

    def mostra_primeiro(self):
        if len(self.itens) == 0:
            print("Fila vazia, não é possível desenfileirar.")
        else:
            return self.itens[0]
        
    def mostrar_fila(self):
        return list(self.itens)
    
     
def menu():
    print(
        '''
        1-Enfileirar
        2-Desenfileirar
        3-Mostrar primeiro
        4-Mostrar fila
        '''
    )

fila = Fila()

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
            fila.enfileirar(i)
    elif opc == 2:
        fila.desenfileirar()
    elif opc == 3:
        print(fila.mostra_primeiro())
    elif opc == 4:
        print(fila.mostrar_fila())
    elif opc == 0:
        break