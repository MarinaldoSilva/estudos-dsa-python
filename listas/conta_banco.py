class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def verificar_saldo(self, valor):
        if self.saldo >= valor:
            return True
        return False
    
    def depositar(self, valor):
        self.saldo += valor
        return self.saldo
    
    def sacar(self, valor):
        if self.verificar_saldo(valor):
            self.saldo -= valor
            return True
        else:
            return False
    
    def ver_saldo(self):
        return f"Saldo atual: {self.saldo}"