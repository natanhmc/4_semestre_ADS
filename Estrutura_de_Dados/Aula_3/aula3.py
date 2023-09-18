# try:
#     numero = int(input("degite um numero interiro:"))
#     if numero % 2 == 0:
#         print ("numero é par")
#     else:
#         print ("numero é impar")
# except ValueError:
#     print ("Erro: Digite um numero valido ")
# else:
#     print ("Operação concluida com sucesso !!")
# finally:
#     print ("fim da execução")

# ------------------------------------------------------------------------------------------------------
# lista = []

# try:
#     lista = int(input("informe uma lista de numeros separados por vircula(,): ").split(","))
#     for item in lista:
#         if item == int:
#             valor = valor + item
#         else:
#             lista.remove(item)
# except :
#     print ("nao deu")

# -------------------------------------------------------------------------------------------------------

# lista = []

# entrada = input("informe uma lista de numeros separados por vircula(,): ").split(",")

# for item in entrada:
#     try:
#         numero = float(item)
#         lista.append(numero)
#     except ValueError:
#         print (f"valor invalido: {item}, ignorando este valor.")
        
# print (f"os numeros validos sao {lista}")

# soma = 0 

# for num in lista:
#     soma += num
    
# print ("o valor total é ", soma)    

# -------------------------------------------------------------------------------------------------------


# def saldacao(nome):
#     print ("Olá, " + nome + " !Bem vindo(a)")
    
# nome_entrada = input("informe seu nome:")

# saldacao(nome_entrada)

# def calcular_media(nota1, nota2):
#     media = (nota1 + nota2) / 2
#     return media

# resultado = calcular_media(7.5, 8.2)
# print ("A media é: ", resultado)

# -------------------------------------------------------------------------------------------------------

# def dividir(a, b):
#     quociente = a // b
#     resto = a % b
#     return quociente, resto

# resultado_quociente, resultado_resto = dividir(10, 3)
# print (resultado_quociente, resultado_resto)

# -------------------------------------------------------------------------------------------------------

# texto = "Olá, mundo!"
# tamanho = len(texto)
# print(tamanho)


# lista = []

# entrada = input("informe uma lista de numeros separados por vircula(,): ").split(",")

# def obter_numeros(entrada):
#     for item in entrada:
#         try:
#             numero = float(item)
#             lista.append(numero)
#         except ValueError:
#             print (f"valor invalido: {item}, ignorando este valor.")
            
#     print (f"os numeros validos sao {lista}")

# def obter_soma(lista_recebida):
#     soma = 0 

#     for num in lista_recebida:
#         soma += num
        
#     print ("o valor total é ", soma)

def calculo_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificacao_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Acima do peso (sobrepeso)"
    elif imc < 35:
        return "Obesidade I"
    elif imc < 40:
        return "Obesidade II"
    else:
        return "Obesidade III"
    
def valida_entrada(valor):
        try:
            numero = float(valor)
            return numero
        except ValueError:
            print(f"Digite um valor adequado! diferente de : {valor}")
            return 0
        
peso = 0
altura = 0
        
while peso == 0:
    peso = valida_entrada(input("Digite o peso (em quilogramas): "))
    
while altura == 0:
    altura = valida_entrada(input("Digite a altura (em metros): "))


imc = calculo_imc(peso, altura)
classificacao = classificacao_imc(imc)

print(f"IMC: {imc:.2f}")
print(f"Classificação: {classificacao}")
