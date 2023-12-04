import mysql.connector


class Data:

    db_config = {
        'user':'natanhmc',
        'password':'1q2w3e4r5t',
        'host':'db4free.net',
        'database':'linkedin123',
        'port':3306
    }
    
    def criar_banco(self):
        try:
            self.abrir_banco()
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS Contatos_Natan (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    nome VARCHAR(50),
                    perfil_linkedin VARCHAR(50)
                )           
            ''')
        finally:
            self.fechar_banco()
            
    def abrir_banco(self):
        self.conn = mysql.connector.connect(**self.db_config)
        self.cursor = self.conn.cursor()
        return self.conn, self.cursor
        
    def fechar_banco(self):
        self.conn.commit()
        self.conn.close()