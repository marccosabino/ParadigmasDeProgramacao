class animal:
    def __init__(self,nome, diaNascimento):
        self.nome = nome
        self.diaNascimento = diaNascimento
    
    def latir(self):
        return f"Au, Au!!!"

meuCachorro = animal("bela",12)
print(meuCachorro.nome)
print(meuCachorro.diaNascimento)
print(meuCachorro.latir())


class ContaBancaria:
    def __init__(self, cliente, saldo1,saldo2,saldo3):
        self.cliente = cliente.nome 
        self.saldo1 = saldo1
        self._saldo2 = saldo2
        self.__saldo3 = saldo3
    
    def deposito(self, saldoDepositado):
        self.saldoDepositado = saldoDepositado
        self.__saldo3 = self.__saldo3 + saldoDepositado
        
    def sacar(self, valorSaque):
        self.__valorSaque = valorSaque
        if self.__saldo3 >= self.__valorSaque:
            self.__saldo3 = self.__saldo3 -self.__valorSaque

    def consultaSaldo(self):
        return self.__saldo3

class Cliente:
    def __init__(self, nome, tipodaConta, cpf):
        self.nome = nome 
        self.__tipodaConta = tipodaConta
        self.__cpf = cpf
    
    def consultaCliente(self):
        return (self.__nome, self.__tipodaConta)

clienteTiago = Cliente("Tiago", "Corrente", 00000000000)
contaTiago = ContaBancaria(clienteTiago, 150, 150, 150)
contaTiago.saldo1 = 200
contaTiago._saldo2 = 200
print(contaTiago.saldo1)
print(contaTiago._saldo2)
print(contaTiago.consultaSaldo())