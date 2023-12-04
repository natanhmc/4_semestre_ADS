import mysql.connector
from Data import Data

class Contato:
      
    def adicionar_contato(self, nome, perfil_linkedin, data):
        try:
            data.abrir_banco()
            
            data.cursor.execute('SELECT * FROM Contatos_Natan WHERE perfil_linkedin = %s', (perfil_linkedin,))
            if data.cursor.fetchone() is None:
                data.cursor.execute('INSERT INTO Contatos_Natan (nome, perfil_linkedin) VALUES (%s, %s)', (nome, perfil_linkedin))
                data.conn.commit()
                print("Contato adicionado com sucesso.")
            else:
                print("Contato já cadastrado.")
        except mysql.connector.Error as erro:
            print(f"Ocorreu um erro {erro}. Tente novamente.")
        finally:
            data.fechar_banco() 
            
    def listar_contatos(self, data):
        try:
            data.abrir_banco()
            data.cursor.execute('SELECT * FROM Contatos_Natan')
            contatos = data.cursor.fetchall()
            return contatos
        except mysql.connector.Error as erro:
            print(f"Ocorreu um erro {erro}. Tente novamente.")
        finally:
            data.fechar_banco() 
        
    def excluir_contato(self, id, data):
        try:
            data.abrir_banco()
            data.cursor.execute('DELETE FROM Contatos_Natan WHERE id = %s', (id,))
        except mysql.connector.Error as erro:
            print(f"Ocorreu um erro {erro}. Tente novamente.")
        finally:
            data.fechar_banco() 