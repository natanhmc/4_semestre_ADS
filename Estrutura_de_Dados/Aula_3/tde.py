# Exercicio 1- soma de numeros pares em uma lista. ----------------------------------------------------------

numeros_pares = []

def soma_pares(lista):
    soma = 0
    global numeros_pares
    for item in lista:
        try:
            numero = float(item)
            if numero % 2 == 0:
                soma += numero
                numeros_pares.append(numero)
        except ValueError:
            print (f"valor invalido: {item}.")
    return "A soma dos numeros pares é: " + str(soma)

entrada = input("Informe uma lista de numeros separados por virgula(,):\n").split(",")

resultado_soma = soma_pares(entrada)
print(resultado_soma)


# Exercicio 2- Calcular IMC de uma pessoa -------------------------------------------------------------------

def calcula_IMC(kilos, metros):
    imc = kilos / (metros*metros)
    return float(imc)

def classifica(indice):
    if indice < 18.5:
        print(f"Seu IMC é {indice:.2f}, você está abaixo do peso.")
    elif indice >=18.5 and indice <= 24.9:
        print(f"Seu IMC é {indice:.2f}, você está com peso normal.")
    elif indice >=25 and indice <= 29.9:
        print(f"Seu IMC é {indice:.2f}, você está com sobrepeso.")
    elif indice >=30 and indice <= 34.9:
        print(f"Seu IMC é {indice:.2f}, você está com obesidade 1.")
    elif indice >=35 and indice <= 39.9:
        print(f"Seu IMC é {indice:.2f}, você está com obesidade 2")
    else: 
        print(f"Seu IMC é {indice:.2f}, você está com obesidade 3.")
        

peso = float(input("Informe o seu peso em kilos 'xx.xx': "))
altura = float(input("Informe a sua altura 'x.xx': "))

indice_cru = calcula_IMC(peso, altura)
resultado_imc = classifica(indice_cru)
print(resultado_imc)

# Exercicio 3- Maiores e menores numeros --------------------------------------------------------------------


def verifica_numeros(lista):
    maior = 0
    menor = float(lista[0])
    
    for item in lista:
        try:
            numero = float(item)
            if maior < numero:
                maior = numero
            elif menor > numero:
                menor = numero
                
        except ValueError:
            print (f"valor invalido: {item}.")
    return f"O maior e menor numero respectivamente são: {maior} e {menor}"

entrada = input("Informe uma lista de numeros separados por virgula(,):\n").split(",")

numero_retornados = verifica_numeros(entrada)
print(numero_retornados)
        
# Exercicio 4- Contar vogais --------------------------------------------------------------------------------

def conta_vogais(palavra):
    vogais = "aeiouAEIOU"
    cont = 0
    
    for vogal in palavra:
        if vogal in vogais:
            cont += 1
    return cont

entrada = input("Informe a palavra para contar as vogais: ")
qnt_vogais = conta_vogais(entrada)
print(f"A quantidade de vogais na palavra é de {qnt_vogais}")