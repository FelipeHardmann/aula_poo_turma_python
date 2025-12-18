from repository.conta_repository import ContaRepository
from schemas.conta_corrente import ContaCorrente
from schemas.conta_poupaca import ContaPoupanca


# Criamos os Schema
nova_conta = ContaCorrente(
    10_000,
    12345,
    'Nu Instituição S/A',
    '12345678910',
    246,
    1_000
)

cr = ContaRepository()

cr.criar_conta(
    saldo=nova_conta.saldo,
    agencia=nova_conta.agencia,
    numero=nova_conta.numero,
    banco=nova_conta.banco,
    tipo_conta=1,
    cpf=nova_conta._cpf,
    limite=nova_conta.limite
)

