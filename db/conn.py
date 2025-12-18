import mysql.connector
from typing import Optional

class MySQLConfig:
    """Configurações centralizadas do MySQL"""
    HOST = 'localhost'
    USER = 'root'
    PASSWORD = 'Felipe2015#'
    DATABASE = 'banco_digital'
    PORT = 3306

class MySQLConnect:
    def __init__(self, 
                 host: Optional[str] = None, 
                 user: Optional[str] = None, 
                 password: Optional[str] = None, 
                 database: Optional[str] = None,
                 port: Optional[int] = None):
        """
        Inicializa a conexão com MySQL.
        Se os parâmetros não forem fornecidos, usa as configurações padrão.
        """
        self.host = host or MySQLConfig.HOST
        self.user = user or MySQLConfig.USER
        self.password = password or MySQLConfig.PASSWORD
        self.database = database or MySQLConfig.DATABASE
        self.port = port or MySQLConfig.PORT
        self.conn = None
        self.cursor = None
    
    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port
            )
            self.cursor = self.conn.cursor()
            print('Conexão concluída')
        except Exception as e:
            print(f'Deu erro: {e}')
    
    def execute(self, query: str, params: tuple = None):
        try:
            self.cursor.execute(query, params or ())
            self.conn.commit()
        except Exception as e:
            print(f'Erro: {e}')
    
    def fetchall(self):
        return self.cursor.fetchall()
    
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

db = MySQLConnect()