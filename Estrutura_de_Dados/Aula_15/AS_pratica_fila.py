class Fila:
    
    def __init__(self):
        self.itens = []
        
    def enfileirar(self, valor):
        self.itens.append(valor)
        
    def desenfileirar(self):
        if self.vazia():
            print("Fila vazia !!")
        else:
            self.itens.pop(0)
            
    def mostra_primeiro(self):
        if self.vazia():
            print("Fila vazia !!")
        else:
            print("O primeiro elemento da fila é : " ,self.itens[0])
            
    def mostrar_fila(self):
        print(self.itens)
        
    def tamanho(self):
        return len(self.itens)
        
    def vazia(self):
        return len(self.itens) == 0
        
def menu():
    print(
        '''
        1-Enfileirar
        2-Desenfileirar
        3-Mostrar primeiro
        4-Mostrar fila
        5-Mostrar tamanho
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
        fila.mostra_primeiro()
    elif opc == 4:
        fila.mostrar_fila()
    elif opc == 5:
        print("o tamanho da fila é : ", fila.tamanho())
    elif opc == 0:
        break