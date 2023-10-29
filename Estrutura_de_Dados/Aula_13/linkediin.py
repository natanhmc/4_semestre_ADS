import sqlite3
import os

def criar_banco():
    conn = sqlite3.connect('linkediin_network.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contatos (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            perfil_linkedin TEXT
        )           
        ''')
    
    cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS conexoes (
                id INTEGER PRIMARY KEY,
                contato1_id INTEGER,
                contato2_id INTEGER,
                FOREIGN KEY (contato1_id) REFERENCES contatos (id),
                FOREIGN KEY (contato2_id) REFERENCES contatos (id)
            )
        ''')
    
    conn.commit()
    conn.close()
    
def excluir_contato(nome, perfil_linkedin):
    conn = sqlite3.connect('linkediin_network.db')
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM contatos WHERE nome = ? AND perfil_linkedin = ?", (nome, perfil_linkedin))
    contato_id = cursor.fetchone()

    if contato_id:
        contato_id = contato_id[0]

        cursor.execute("DELETE FROM conexoes WHERE contato1_id = ? OR contato2_id = ?", (contato_id, contato_id))

        cursor.execute("DELETE FROM contatos WHERE id = ?", (contato_id,))

        conn.commit()
        print("Perfil Excluído !!")
    else:
        print("Perfil não encontrado !!")
    
def adicionar_contato(nome, perfil_linkedin):
    conn = sqlite3.connect('linkediin_network.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT id FROM contatos WHERE nome = ? AND perfil_linkedin = ?", (nome, perfil_linkedin))
    contato_id = cursor.fetchone()

    if contato_id:
        contato_id = contato_id[0]
        print("Perfil já cadastrado !!")
    else:     
        cursor.execute('INSERT INTO contatos (nome, perfil_linkedin) VALUES (?, ?)', (nome, perfil_linkedin))
    conn.commit()
    conn.close()
    
def listar_contatos():
    conn = sqlite3.connect('linkediin_network.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM contatos')
    contatos = cursor.fetchall()
    
    conn.close()
    return contatos

def adicionar_conexao(contato1_id, contato2_id):
    conn = sqlite3.connect('linkediin_network.db')
    cursor = conn.cursor()
    
    cursor.execute('BEGIN')
    
    try:
        cursor.execute('SELECT * FROM conexoes WHERE (contato1_id = ? AND contato2_id = ?) OR (contato1_id = ? AND contato2_id = ?)',
                       (contato1_id, contato2_id, contato2_id, contato1_id))

        if cursor.fetchone() is None:
            cursor.execute('INSERT INTO conexoes (contato1_id, contato2_id) VALUES (?, ?)',
                           (contato1_id, contato2_id))
        else:
            print("A conexão entre esses contatos ja existe")
        
        conn.commit()
    except sqlite3.IntegrityError:
        conn.rollback()
        print("Ocorreu um erro de coerência. Tente novamente")
        
    conn.close()
    
def listar_conexoes(contato_id):
    conn = sqlite3.connect('linkediin_network.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT contatos.nome
        FROM contatos
        JOIN conexoes ON contatos.id = CASE 
            WHEN conexoes.contato1_id = ? THEN conexoes.contato2_id
            ELSE conexoes.contato1_id
        END
        WHERE conexoes.contato1_id = ? OR conexoes2_id = ?
        ''', (contato_id, contato_id, contato_id))
    
    conexoes = cursor.fetchall()
    conn.close()
    return conexoes

def menu():
    while True:
        print("\n1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Adicionar Conexão")
        print("4. Listar Conexões de um Contato")
        print("5. Excluir Contatos e Conexões")
        print("0. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            nome = input("Nome do Contato: ")
            perfil_linkedin = input("Perfil do contato: ")
            adicionar_contato(nome, perfil_linkedin)
        elif escolha == "2":
            contatos = listar_contatos()
            for contato in contatos:
                print(f"ID : {contato[0]}, Nome: {contato[1]}, Perfil Linkedin: {contato[2]}")
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
        elif escolha == "0":
            break
        else:
            print("Opção inválida. Tente novamente")
            
if __name__ == "__main__":
    criar_banco()
    menu()            
