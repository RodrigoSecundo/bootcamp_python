from abc import ABC, abstractmethod
from datetime import datetime


menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo usuário
[nc] Nova conta
[lc] Listar contas
[q] Sair

=> """

AGENCIA_PADRAO = "0001"


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            }
        )


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso = conta.depositar(self.valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso = conta.sacar(self.valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0.0
        self._numero = numero
        self._agencia = AGENCIA_PADRAO
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        if valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
            return False

        if valor > self._saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
            return False

        self._saldo -= valor
        print("Saque realizado com sucesso!")
        return True

    def depositar(self, valor):
        if valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
            return False

        self._saldo += valor
        print("Depósito realizado com sucesso!")
        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500.0, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques
        self._numero_saques = 0

    def sacar(self, valor):
        excedeu_limite = valor > self._limite
        excedeu_saques = self._numero_saques >= self._limite_saques

        if excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
            return False

        if excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
            return False

        sucesso = super().sacar(valor)

        if sucesso:
            self._numero_saques += 1

        return sucesso


class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    @property
    def endereco(self):
        return self._endereco

    @property
    def contas(self):
        return self._contas

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self._contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @property
    def cpf(self):
        return self._cpf


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if isinstance(cliente, PessoaFisica) and cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\nCliente não possui conta!")
        return None

    return cliente.contas[0]


def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente números): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\nJá existe cliente com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    logradouro = input("Informe o logradouro: ")
    numero = input("Informe o número: ")
    bairro = input("Informe o bairro: ")
    cidade = input("Informe a cidade: ")
    estado = input("Informe o estado (sigla): ")

    endereco = f"{logradouro}, {numero} - {bairro} - {cidade}/{estado}"

    novo_cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(novo_cliente)

    print("\nCliente criado com sucesso!")


def criar_conta_corrente(contas, clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente is None:
        print("\nCliente não encontrado, fluxo de criação de conta encerrado!")
        return

    numero_conta = len(contas) + 1
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.adicionar_conta(conta)

    print("\nConta corrente criada com sucesso!")


def listar_contas(contas):
    if not contas:
        print("\nNão há contas cadastradas.")
        return

    for conta in contas:
        linha = f"Agência: {conta.agencia}  |  Conta: {conta.numero}  |  Titular: {conta.cliente.nome}"
        print("=" * len(linha))
        print(linha)


def exibir_extrato(conta):
    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes

    if not transacoes:
        print("Não foram realizadas movimentações.")
    else:
        for transacao in transacoes:
            print(f"{transacao['data']} - {transacao['tipo']}: R$ {transacao['valor']:.2f}")

    print(f"\nSaldo: R$ {conta.saldo:.2f}")
    print("==========================================")


def main():
    clientes = []
    contas = []

    while True:
        opcao = input(menu)

        if opcao == "d":
            cpf = input("Informe o CPF do cliente: ")
            cliente = filtrar_cliente(cpf, clientes)

            if not cliente:
                print("\nCliente não encontrado!")
                continue

            conta = recuperar_conta_cliente(cliente)
            if not conta:
                continue

            valor = float(input("Informe o valor do depósito: "))
            transacao = Deposito(valor)
            cliente.realizar_transacao(conta, transacao)

        elif opcao == "s":
            cpf = input("Informe o CPF do cliente: ")
            cliente = filtrar_cliente(cpf, clientes)

            if not cliente:
                print("\nCliente não encontrado!")
                continue

            conta = recuperar_conta_cliente(cliente)
            if not conta:
                continue

            valor = float(input("Informe o valor do saque: "))
            transacao = Saque(valor)
            cliente.realizar_transacao(conta, transacao)

        elif opcao == "e":
            cpf = input("Informe o CPF do cliente: ")
            cliente = filtrar_cliente(cpf, clientes)

            if not cliente:
                print("\nCliente não encontrado!")
                continue

            conta = recuperar_conta_cliente(cliente)
            if not conta:
                continue

            exibir_extrato(conta)

        elif opcao == "nu":
            criar_cliente(clientes)

        elif opcao == "nc":
            criar_conta_corrente(contas, clientes)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()