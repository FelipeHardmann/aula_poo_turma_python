import mysql.connector
from typing import Optional

class MySQLConfig:
    """Configurações centralizadas do MySQL"""
    HOST = 'localhost' # 'aws-postgresql-001.c3nwwjzswu6u.us-east-1.rds.amazonaws.com' exemploooooo!!!!!!!
    USER = 'root' # 'admin' exemploooooo!!!!!!!
    PASSWORD = 'Felipe2015#' # 'senhaadmin123' exemploooooo!!!!!!!
    DATABASE = 'banco_digital' # 'aws_postgresql_001' exemploooooo!!!!!!!
    PORT = 3306 # 5432 exemploooooo!!!!!!!

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
    
    def fetchall(self, query, params: tuple = None):
        self.cursor.execute(query, params or ())
        return self.cursor.fetchall()
    
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

db = MySQLConnect()