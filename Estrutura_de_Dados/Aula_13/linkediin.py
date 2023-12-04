import mysql.connector

db_config = {
    'user': 'natanhmc',
    'password': '1q2w3e4r5t',
    'host': 'db4free.net',
    'database': 'linkedin123',
    'port': 3306
}

def criar_banco():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contatos (
            id INT PRIMARY KEY AUTO_INCREMENT,
            nome VARCHAR(50),
            perfil_linkedin VARCHAR(50)
        )           
        ''')
    
    cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS conexoes (
                id INT PRIMARY KEY AUTO_INCREMENT,
                contato1_id INT,
                contato2_id INT,
                FOREIGN KEY (contato1_id) REFERENCES contatos (id),
                FOREIGN KEY (contato2_id) REFERENCES contatos (id)
            )
        ''')
    
    conn.commit()
    conn.close()
    
def adicionar_contato(nome, perfil_linkedin):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        cursor.execute("SELECT id FROM contatos WHERE nome = %s AND perfil_linkedin = %s", (nome, perfil_linkedin))
        contato_id = cursor.fetchone()

        if contato_id:
            contato_id = contato_id[0]
            print("Perfil já cadastrado !!")
        else:
            cursor.execute("INSERT INTO contatos (nome, perfil_linkedin) VALUES (%s, %s)", (nome, perfil_linkedin))

        conn.commit()
        print("Contato criado com sucesso!!!")
    except mysql.connector.Error as err:
        print(f"Erro ao adicionar contato: {err}")
    finally:
        if 'conn' in locals():
            conn.close()
            
def listar_contatos():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM contatos')
    contatos = cursor.fetchall()
    
    conn.close()
    return contatos

def excluir_contato(nome, perfil_linkedin):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM contatos WHERE nome = %s AND perfil_linkedin = %s", (nome, perfil_linkedin))
    contato_id = cursor.fetchone()

    if contato_id:
        contato_id = contato_id[0]

        cursor.execute("DELETE FROM conexoes WHERE contato1_id = %s OR contato2_id = %s", (contato_id, contato_id))

        cursor.execute("DELETE FROM contatos WHERE id = %s", (contato_id,))

        conn.commit()
        print("Perfil Excluído !!")
    else:
        print("Perfil não encontrado !!")
    

def adicionar_conexao(contato1_id, contato2_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    cursor.execute('BEGIN')
    
    try:
        cursor.execute('SELECT * FROM conexoes WHERE (contato1_id = %s AND contato2_id = %s) OR (contato1_id = %s AND contato2_id = %s)',
                       (contato1_id, contato2_id, contato2_id, contato1_id))

        if cursor.fetchone() is None:
            cursor.execute('INSERT INTO conexoes (contato1_id, contato2_id) VALUES (%s, %s)',
                           (contato1_id, contato2_id))
            print("Conexão criada com sucesso!!")
        else:
            print("A conexão entre esses contatos ja existe")
        
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Erro ao adicionar conexão: {err}")
        conn.rollback()
    finally:
        if 'conn' in locals():
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
        SELECT contatos.nome
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

# def carregar

def menu():
    while True:
        print("\n1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Adicionar Conexão")
        print("4. Listar Conexões de um Contato")
        print("5. Excluir Contatos e Conexões")
        print("6. Excluir Conexão")

        print("0. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            nome = input("Nome do Contato: ")
            perfil_linkedin = input("Perfil do contato: ")
            adicionar_contato(nome, perfil_linkedin)
        elif escolha == "2":
            contatos = listar_contatos()
            for contato in contatos:
                print(f"ID : {contato[0]}\n,Nome: {contato[1]}\n, Perfil Linkedin: {contato[2]}")
        elif escolha == "3":
            contato1_id = int(input("ID do primeiro contato: "))
            contato2_id = int(input("ID do segundo contato: "))
            adicionar_conexao(contato1_id, contato2_id)
        elif escolha == "4":
            contato_id = int(input("ID do contato: "))
            conexoes = listar_conexoes(contato_id)
            print("Conexões do contato: ")
            for conexao in conexoes:
                print(conexao[0])
        elif escolha == "5":
            nome = input("Nome do Contato: ")
            perfil_linkedin = input("Perfil do contato: ")
            excluir_contato(nome, perfil_linkedin)
        elif escolha == "6":
            contato1 = int(input("ID do primeiro contato: "))
            contato2 = int(input("ID do segundo contato: "))
            excluir_conexao(contato1, contato2)
        elif escolha == "0":
            break
        else:
            print("Opção inválida. Tente novamente")
            
if __name__ == "__main__":
    criar_banco()
    menu()            
