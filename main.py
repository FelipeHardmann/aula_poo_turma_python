# Justamente o arquivo principal
# SOLID

# Solid - Single Responsibility Principle

from repository.conta_repository import ContaRepository
from schemas.conta_corrente import ContaCorrente
from schemas.conta_poupaca import ContaPoupanca
from time import sleep


nova_conta = ContaCorrente(
    10_000,
    12345,
    'Nu Instituição S/A',
    '12345678910',
    246,
    1_000
)

cr = ContaRepository()

# cr.criar_conta(
#     saldo=nova_conta.saldo,
#     agencia=nova_conta.agencia,
#     numero=nova_conta.numero,
#     banco=nova_conta.banco,
#     tipo_conta=1,
#     cpf=nova_conta._cpf,
#     limite=nova_conta.limite
# )

# lista de contas
# lista_contas =cr.listar_contas()

# for conta in lista_contas:
#     print(conta)

# listar conta por id

# print(cr.buscar_conta_por_id(2))

# atualizar saldo

# print(cr.buscar_conta_por_id(2))

# sleep(5)

# cr.atualizar_saldo(2, 2_000)

# sleep(5)

# print(cr.buscar_conta_por_id(2))

# print(cr.listar_contas())

# sleep(5)

# cr.deletar_conta(3)

# sleep(5)

# print(cr.listar_contas())
