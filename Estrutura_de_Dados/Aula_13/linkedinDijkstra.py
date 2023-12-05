import mysql.connector
import heapq

db_config = {
    'user':'natanhmc',
    'password':'1q2w3e4r5t',
    'host':'db4free.net',
    'database':'linkedin123',
    'port':3306
}

def criar_banco():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contatos (
            id INT PRIMARY KEY AUTO_INCREMENT,
            nome VARCHAR(50),
            perfil_linkedin VARCHAR(50)
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conexoes (
            id INT PRIMARY KEY AUTO_INCREMENT,
            contato1_id INT,
            contato2_id INT,
            FOREIGN KEY (contato1_id) REFERENCES contatos(id),
            FOREIGN KEY (contato2_id) REFERENCES contatos(id)
        );
    ''')

    conn.commit()
    conn.close()


def adicionar_contato(nome, perfil_linkedin):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT * FROM contatos WHERE perfil_linkedin = %s', (perfil_linkedin,))
        if cursor.fetchone() is None:
            cursor.execute('INSERT INTO contatos (nome, perfil_linkedin) VALUES (%s, %s)', (nome, perfil_linkedin))
            conn.commit()
        else:
            print("Contato já cadastrado.")
    except mysql.connector.Error as erro:
        print(f"Ocorreu um erro {erro}. Tente novamente.")


    conn.close()

def listar_contatos():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM contatos')
    contatos = cursor.fetchall()

    conn.close()
    return contatos


def adicionar_conexao(contato1_id, contato2_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute('BEGIN')
    
    try:
        cursor.execute('SELECT * FROM conexoes WHERE (contato1_id = %s AND contato2_id = %s) OR (contato1_id = %s AND contato2_id = %s)',
                      (contato1_id, contato2_id, contato2_id, contato1_id))

        if cursor.fetchone() is None:
            cursor.execute('INSERT INTO conexoes (contato1_id, contato2_id) VALUES (%s, %s)', (contato1_id, contato2_id))
        else:
            print("A conexão entre esses contatos já existe.")
        
        conn.commit()
        
    except mysql.connector.Error as erro:
        conn.rollback()
        print(f"Ocorreu um erro {erro}. Tente novamente.")
        
    conn.close()

def listar_conexoes(contato_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute('''
        SELECT contatos.id
        FROM contatos
        JOIN conexoes ON contatos.id = CASE
            WHEN conexoes.contato1_id = %s THEN conexoes.contato2_id
            ELSE conexoes.contato1_id
        END
        WHERE conexoes.contato1_id = %s OR conexoes.contato2_id = %s
    ''', (contato_id, contato_id, contato_id))

    conexoes = cursor.fetchall()
    conn.close()
    return conexoes

def excluir_contato(id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM conexoes WHERE contato1_id = %s OR contato2_id = %s', (id, id))
    cursor.execute('DELETE FROM contatos WHERE id = %s', (id))

    conn.commit()
    conn.close()

def excluir_conexao(id1, id2):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM conexoes WHERE (contato1_id = %s AND contato2_id = %s) OR (contato1_id = %s AND contato2_id = %s)', (id1, id2, id2, id1))

    conn.commit()
    conn.close()




def listar_conexoes(contato_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute('''
        SELECT contato1_id, contato2_id
        FROM conexoes
        WHERE contato1_id = %s OR contato2_id = %s
    ''', (contato_id, contato_id))

    conexoes = cursor.fetchall()
    conn.close()
    return conexoes

def encontrar_contatos_sem_conexao():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()


    cursor.execute('''
        SELECT contatos.id, contatos.nome
        FROM contatos
        WHERE contatos.id NOT IN (
            SELECT DISTINCT contato1_id FROM conexoes
            UNION
            SELECT DISTINCT contato2_id FROM conexoes
        )
    ''')

    contatos_sem_conexao = cursor.fetchall()
    conn.close()
    return contatos_sem_conexao



def construir_grafo(conexoes):
    graph = {}

    for conexao in conexoes:
        contato1_id, contato2_id = conexao[0], conexao[1]

        if contato1_id not in graph:
            graph[contato1_id] = []
        if contato2_id not in graph:
            graph[contato2_id] = []


        graph[contato1_id].append((contato2_id, 1))  
        graph[contato2_id].append((contato1_id, 1)) 

    return graph



def adicionar_conexoes_ao_grafo(graph, conexoes):
    for conexao in conexoes:
        contato_id, _ = conexao[0], conexao[1]

        for outra_conexao in conexoes:
            outra_contato_id, _ = outra_conexao[0], outra_conexao[1]

            if contato_id != outra_contato_id and (outra_contato_id, 1) not in graph[contato_id]:
                graph[contato_id].append((outra_contato_id, 1))

    return graph



def encontrar_caminho_mais_curto(contato1_id=int, contato2_id=int):
    conexoes = listar_conexoes(contato1_id) + listar_conexoes(contato2_id)

    graph = construir_grafo(conexoes)

    print("Grafo:")
    for key, value in graph.items():
        print(f"{key}: {value}")

    caminho_minimo = dijkstra(graph, int(contato1_id), int(contato2_id))

    if caminho_minimo is not None:
        distancia_minima, caminho = caminho_minimo
        print(f"A distância mínima entre os contatos {contato1_id} e {contato2_id} é: {distancia_minima}")
        print(f"Caminho: {caminho}")
    else:
        print(f"Não há caminho entre os contatos {contato1_id} e {contato2_id}")


def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]
    visited = set()

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node == end:
            return current_distance, visited

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return None


def menu():
    while True:
        print("\n1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Adicionar Conexão")
        print("4. Listar Conexões de um Contato")
        print("5. Excluir contato")
        print("6. Excluir Conexão" )
        print("7. Verificar se todos tem alguma conexão")
        print("8. Caminho mais curto")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do contato: ")
            perfil_linkedin = input("Perfil do LinkedIn: ")
            adicionar_contato(nome, perfil_linkedin)
        elif escolha == "2":
            contatos = listar_contatos()
            print("Lista de Contatos:")
            for contato in contatos:
                print(f"ID: {contato[0]}, Nome: {contato[1]}, Perfil LinkedIn: {contato[2]}")
        elif escolha == "3":
            contato1_id = int(input("ID do primeiro contato: "))
            contato2_id = int(input("ID do segundo contato: "))
            adicionar_conexao(contato1_id, contato2_id)
        elif escolha == "4":
            contato_id = int(input("ID do contato: "))
            conexoes = listar_conexoes(contato_id)
            print("Conexões do Contato:")
            for conexao in conexoes:
                print(conexao[0])
        elif escolha == "5":
            id = input("Informe o ID do contato a ser excluído: ")
            excluir_contato(id)
        elif escolha == "6":
            id1 = input("Informe o ID do primeiro contato: ")
            id2 = input("Informe o ID do segundo contato: ")
            excluir_conexao(id1, id2)

        elif escolha == "7":
            contatos_sem_conexao = encontrar_contatos_sem_conexao()
            if contatos_sem_conexao:
                print("Contatos sem conexões:")
                for contato in contatos_sem_conexao:
                    print(f"ID: {contato[0]}, Nome: {contato[1]}")
            else:
                print("Todos os contatos têm pelo menos uma conexão.")

        elif escolha == "8":
            contato1_id = input("Informe o ID do primeiro contato: ")
            contato2_id = input("Informe o ID do segundo contato: ")
            encontrar_caminho_mais_curto(contato1_id, contato2_id)
        elif escolha == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    criar_banco()
    menu()
