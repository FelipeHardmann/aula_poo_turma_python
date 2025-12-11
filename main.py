'''
Fazer a atividade do seguinte, o usuário ter a possibilidade de escolher a conta
Qual valor ele vai depositar, qual valor ele vai sacar da conta e as transferências
entre contas, conta corrente e faz pix para uma pessoa que tem conta Poupança
'''

from schemas.conta_corrente import ContaCorrente
from schemas.conta_poupaca import ContaPoupanca
from random import randint


lista = []

while True:
    print('''
        Bem-vindo ao meu Banco
        Digite 1 para criar uma Conta Corrente
        Digite 2 para criar uma Conta Poupança
    ''')

    op = int(input('Escolha: '))

    if op == 1:
        saldo = float(input('Digite o saldo a ser depositado: '))
        cpf = input('Digite seu CPF: ')
        c1 = ContaCorrente(
            agencia=222,
            saldo=saldo,
            banco='Bank',
            cpf=cpf,
            numero=randint(1000, 9999),
            limite=1_000
        )

    lista.append(c1)

    tarefas = int(input('''
        Digite o que deseja fazer:
        1 - Transferir valor:
        2 - Exibir dados:
        4 - Finalizar:
    '''))

    if tarefas == 1:
        for contas in lista:
            print(contas.__dict__)
        conta_para_transferir = int(input('Digite a posição da conta que deseja transferir: '))
        valor = float(input('Digite o valor que deseja transferir: '))
        c1.transferir_saldo(valor=valor, conta=lista[conta_para_transferir-1])

        print(c1.__dict__)

        print(lista[conta_para_transferir-1])

    elif tarefas == 4:
        print('Processo finalizado!')
        continue
