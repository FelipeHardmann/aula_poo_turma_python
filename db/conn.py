import mysql.connector


class MySQLConnect:
    def __init__(self, host: str, user: str, password: str, database: str):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
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

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
