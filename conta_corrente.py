from conta import Conta


class ContaCorrente(Conta):
    def __init__(self, saldo, numero, banco, cpf, agencia, limite):
        super().__init__(saldo, numero, banco, cpf, agencia)
        self.limite = limite

    def exibir(self):
        return f'Conta Poupança: Saldo - {self.saldo} - \
            Número: {self.numero} - Limite: {self.limite}'