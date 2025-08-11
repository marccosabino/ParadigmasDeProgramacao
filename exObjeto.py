class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def __str__(self):
        return f'{self.nome} (CPF: {self.cpf})'


class ContaBancaria:
    def __init__(self, cliente, saldo1, saldo2, saldo3):
        self.cliente = cliente      # Associação: cliente é um objeto da classe Cliente
        self.saldo1 = saldo1        # Público
        self._saldo2 = saldo2       # Protegido
        self.__saldo3 = saldo3      # Privado

    def consultaSaldo1(self):
        return self.saldo1

    def consultaSaldo2(self):
        return self._saldo2

    def consultaSaldo3(self):
        return self.__saldo3

    def exibirDadosConta(self):
        print(f'Cliente: {self.cliente}')
        print(f'Saldo 1 (público): R$ {self.saldo1}')
        print(f'Saldo 2 (protegido): R$ {self._saldo2}')
        print(f'Saldo 3 (privado): R$ {self.__saldo3}')


# Criando um cliente
clienteMarco = Cliente('Marco Sabino', '123.456.789-00')

# Criando uma conta associada ao cliente
contaMarco = ContaBancaria(clienteMarco, 150.0, 200.0, 250.0)

# Exibindo os dados da conta
contaMarco.exibirDadosConta()

# Acessos diretos
print("\nAcessos diretos:")
print(contaMarco.saldo1)        # Acesso direto (público)
print(contaMarco._saldo2)       # Acesso direto (protegido, mas permitido)
# print(contaMarco.__saldo3)    # Isso dá erro!

# Acesso correto ao atributo privado:
print(contaMarco.consultaSaldo3())
