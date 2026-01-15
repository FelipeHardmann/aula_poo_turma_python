from db.conn import db

class ContaRepository:
    """Repository para gerenciar contas no banco de dados"""
    
    def __init__(self):
        self.db = db
    # Create
    def criar_conta(self,
            saldo: float,
            numero: int,
            banco: str,
            tipo_conta: int,
            cpf: str,
            agencia: int,
            rendimento = 0,
            limite = 0
        ):
        '''Método para Criar a nossa Conta no banco de dados'''
        self.db.connect()
        query = '''
            INSERT INTO contas(saldo, numero, banco, agencia, tipo_conta, cpf, rendimento, limite)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        '''
        self.db.execute(query, (saldo, numero, banco, agencia, tipo_conta, cpf, rendimento, limite))
        print('Conta Criada com sucesso!!')
        self.db.close()

    def listar_contas(self):
        """Lista todas as contas"""
        self.db.connect()
        query = "SELECT * FROM contas"
        contas = self.db.fetchall(query)
        self.db.close()
        return contas
    
    def buscar_conta_por_id(self, conta_id: int):
        """Busca uma conta por ID"""
        self.db.connect()
        query = "SELECT * FROM contas WHERE id = %s"
        conta = self.db.fetchall(query, (conta_id,))
        self.db.close()
        return conta[0] if conta else None
    
    def atualizar_saldo(self, conta_id: int, novo_saldo: float):
        """Atualiza o saldo de uma conta"""
        self.db.connect()
        query = "UPDATE contas SET saldo = %s WHERE id = %s"
        self.db.execute(query, (novo_saldo, conta_id))
        self.db.close()
        print(f"Saldo da conta {conta_id} atualizado!")
    
    def deletar_conta(self, conta_id: int):
        """Deleta uma conta"""
        self.db.connect()
        query = "DELETE FROM contas WHERE id = %s"
        self.db.execute(query, (conta_id,))
        self.db.close()
        print(f"Conta {conta_id} deletada!")