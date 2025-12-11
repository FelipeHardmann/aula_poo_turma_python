from schemas.conta import Conta


class ContaPoupanca(Conta):
    def __init__(self, saldo, numero, banco, cpf, agencia, rendimento):
        super().__init__(saldo, numero, banco, cpf, agencia)
        self.rendimento = rendimento

    def aplicar_rendimento(self):
         self.__saldo += self.saldo * self.rendimento

    def exibir(self):
        return f'Conta Poupança: Saldo - {self.saldo} - \
            Número: {self.numero} - Rendimento: {self.rendimento}'