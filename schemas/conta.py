from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, saldo: float, numero: int, banco: str, cpf: str, agencia: int):
        self.__saldo = saldo
        self.numero = numero
        self.banco = banco
        self._cpf = cpf
        self.agencia = agencia

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def novo_saldo(self, valor):
        self.saldo = valor

    def transferir_saldo(self, valor: float, conta) -> str:
        if valor > self.saldo:
            return f'O valor é maior do que seu saldo: {self.saldo}'
        self.__saldo -= valor
        conta.__saldo += valor
        return f'Seu saldo atual é de: {self.saldo}'

    @abstractmethod
    def exibir(self):
        ...