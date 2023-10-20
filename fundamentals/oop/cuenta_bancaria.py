class CuentaBancaria:

    def __init__(self, balance = 0, tasa = 1):
        self.balance = balance
        self.tasa = tasa / 100

    def deposito(self, monto):
        self.balance += monto
        return self

    def retiro(self, monto):
        if(CuentaBancaria.puede_retirar(self.balance, monto)):
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



cuenta_1 = CuentaBancaria(500, 5)
cuenta_2 = CuentaBancaria(200,10)

cuenta_1.deposito(100).deposito(300).deposito(250).retiro(1000).generar_interes().mostrar_info_cuenta()
cuenta_2.deposito(200).deposito(300).retiro(250).retiro(50).retiro(100).retiro(250).generar_interes().mostrar_info_cuenta()

