class ContaRepository:
    def __init__(self, db_connection):
        self.db = db_connection


def criar_conta(self,
        saldo: float,
        numero: int,
        banco: str,
        cpf: str,
        agencia: int,
        rendimento = None,
        limite = None
    ):
    query = '''
        INSERT INTO contas(saldo, numero, banco, agencia, tipo_conta, cpf, rendimento, limite)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    '''

    self.db.execute(query, (saldo, numero, banco, cpf, agencia, rendimento, limite))
