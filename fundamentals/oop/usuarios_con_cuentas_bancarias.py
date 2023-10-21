class Cuenta:

    def __init__(self, balance = 0, tasa = 1):
        self.balance = balance
        self.tasa = tasa / 100

    def deposito(self, monto):
        
        self.balance += monto
        return self

    def retiro(self, monto):
        if(Cuenta.puede_retirar(self.balance, monto)):
            self.balance -= monto
            return self
        else:
            print('Fondos Insuficientes: cobrando una tarifa de $5')
            self.balance -= 5
        return self

    def mostrar_info_cuenta(self):
        print(f'Balance: {self.balance}, Interes: {self.tasa}')
        return self
    def generar_interes(self):
        if(self.balance > 0 ):
            self.balance += (self.balance * self.tasa)
            return self
        else:
            return self
    @staticmethod
    def puede_retirar(balance,monto):
        if(balance - monto < 0 ):
            return False
        else:
             return True

class Usuario:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cuenta = Cuenta(tasa=0.02, balance=0)

    def hacer_deposito(self,monto):
        self.cuenta.balance += monto
        print('Tu nuevo balance es:', self.mostrar_balance())
        return self
    
    def hacer_retiro(self, monto):
        self.cuenta.balance -= monto
        print('Tu nuevo balance es:', self.mostrar_balance())
        return self
    def mostrar_balance(self):
        print(f'Tu balance es: ${self.cuenta.balance}')
benjamin = Usuario('benjamin','benjamin@python.com')

benjamin.hacer_deposito(200).hacer_retiro(50)
