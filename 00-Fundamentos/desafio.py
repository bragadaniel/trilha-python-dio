menu = """
[c] Cadastrar clientes
[l] Listar Clientes
[a] Criar conta
[v] Visualizar contas
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
usuarios = []
contas = []
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = '0001'


def deposito_conta(valor=0.0, saldo=0, extrato="", /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato


def saque_conta(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques


def extrato_consulta(saldo=0, /, *, extrato=""):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def cadastro_usuario(usuarios, /, *, nome, data_nascimento, cpf, endereco):
    for user in usuarios:
        if user['cpf'] == cpf:
            print('CPF já cadastrado')
            return usuarios
    usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    }
    usuarios.append(usuario)
    print('Usuário cadatrado com sucesso!')

    return usuarios


def listar_clientes(usuarios=[]):
    if not usuarios:
        return print('Não existe clientes cadastrados!')

    print("-----------Clientes--------------")
    for usuario in usuarios:
        print(f"Nome: {usuario['nome']}")
        print(f"CPF: {usuario['cpf']}")
        print("--------------------------------")


def criar_conta(contas, usuarios, /, *, cpf):
    usuario = None
    for u in usuarios:
        if u["cpf"] == cpf:
            usuario = u
            break

    if usuario is None:
        print("Erro: Usuário com esse CPF não encontrado.")
        return contas

    numero_conta = len(contas) + 1
    conta = {
        "agencia": "0001",
        "numero_conta": numero_conta,
        "usuario": usuario
    }

    contas.append(conta)
    print(f"Conta criada com sucesso! Número da conta: {numero_conta}")

    return contas


def listar_contas(contas):
    if not contas:
        return print("Não existe contas cadastradas")

    print("-----------Contas--------------")
    for conta in contas:
        print(f"Conta numero: {conta['numero_conta']}")
        print(f"Nome: {conta['usuario']['nome']}")
        print(f"CPF: {conta['usuario']['cpf']}")


while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = deposito_conta(valor, saldo, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        saldo, extrato, numero_saques = saque_conta(saldo=saldo,
                                                    valor=valor,
                                                    extrato=extrato,
                                                    limite=limite,
                                                    numero_saques=numero_saques,
                                                    LIMITE_SAQUES=LIMITE_SAQUES)
    elif opcao == "e":
        extrato_consulta(saldo, extrato=extrato)
    elif opcao == "c":
        nome = str(input("Informe o nome completo: "))
        data_nascimento = str(input("Informe data nascimento: "))
        cpf = str(input("Informe CPF: "))
        endereco = str(input("Informe endereço: "))
        usuarios = cadastro_usuario(usuarios, nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    elif opcao == "l":
        listar_clientes(usuarios)
    elif opcao == 'a':
        cpf = str(input("Informe o cpf: "))
        contas = criar_conta(contas, usuarios, cpf=cpf)
    elif opcao == 'v':
        listar_contas(contas=contas)
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
