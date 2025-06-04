class Cliente:
    def __init__(self, nome: str, cpf: str, endereco: str):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco

    def __str__(self):
        return f"{self.nome} - CPF: {self.cpf}"


class Conta:
    def __init__(self, numero: int, cliente: Cliente, agencia: str = "0001"):
        self.numero = numero
        self.cliente = cliente
        self.agencia = agencia
        self.saldo = 0.0
        self.historico = []

    def depositar(self, valor: float) -> bool:
        if valor > 0:
            self.saldo += valor
            self.historico.append(f"Depósito: +R${valor:.2f}")
            return True
        return False

    def sacar(self, valor: float) -> bool:
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.historico.append(f"Saque: -R${valor:.2f}")
            return True
        return False

    def __str__(self):
        return f"Conta {self.numero} - Agência {self.agencia} - Cliente: {self.cliente.nome}"


class ContaCorrente(Conta):
    def __init__(self, numero: int, cliente: Cliente, limite: float = 500.0, limite_saques: int = 3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
        self.saques_realizados = 0

    def sacar(self, valor: float) -> bool:
        if self.saques_realizados >= self.limite_saques:
            print("Limite de saques diários atingido.")
            return False
        if valor > self.limite:
            print("Valor excede o limite permitido por saque.")
            return False
        if super().sacar(valor):
            self.saques_realizados += 1
            return True
        return False


class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []

    def cadastrar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)

    def adicionar_conta(self, conta: Conta):
        self.contas.append(conta)

    def buscar_cliente(self, cpf: str):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente
        return None
class Cliente:
    def __init__(self, nome: str, cpf: str, endereco: str):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco

    def __str__(self):
        return f"{self.nome} - CPF: {self.cpf}"


class Conta:
    def __init__(self, numero: int, cliente: Cliente, agencia: str = "0001"):
        self.numero = numero
        self.cliente = cliente
        self.agencia = agencia
        self.saldo = 0.0
        self.historico = []

    def depositar(self, valor: float) -> bool:
        if valor > 0:
            self.saldo += valor
            self.historico.append(f"Depósito: +R${valor:.2f}")
            return True
        return False

    def sacar(self, valor: float) -> bool:
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.historico.append(f"Saque: -R${valor:.2f}")
            return True
        return False

    def __str__(self):
        return f"Conta {self.numero} - Agência {self.agencia} - Cliente: {self.cliente.nome}"


class ContaCorrente(Conta):
    def __init__(self, numero: int, cliente: Cliente, limite: float = 500.0, limite_saques: int = 3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
        self.saques_realizados = 0

    def sacar(self, valor: float) -> bool:
        if self.saques_realizados >= self.limite_saques:
            print("Limite de saques diários atingido.")
            return False
        if valor > self.limite:
            print("Valor excede o limite permitido por saque.")
            return False
        if super().sacar(valor):
            self.saques_realizados += 1
            return True
        return False


class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []

    def cadastrar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)

    def adicionar_conta(self, conta: Conta):
        self.contas.append(conta)

    def buscar_cliente(self, cpf: str):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente
        return None
