class Usuario:
    nombre_banco = 'Primer Dojo Nacional'
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.balance_cuenta = 0
    
    def hacer_deposito(self, monto):
        self.balance_cuenta += monto
        return self

    def hacer_retiro(self, monto):
        self.balance_cuenta-=monto
        return self
    
    def mostrar_balance(self):
        print(f'Usuario: {self.name}, Balance: {self.balance_cuenta}',)
        return self
    
    def transferencia(self, destinatario,monto):
        self.balance_cuenta -= monto
        destinatario.balance_cuenta += monto
        print('\n'+f'Se han transferido {monto} al destinatario')
        return self

guido = Usuario('Guido Van Eossum','guiudo@python.com')
monty = Usuario('Montgemery Bernz','Monty@python.com')
homero = Usuario('Homero Simpson', ('homero@python.com'))


guido.hacer_deposito(100).hacer_deposito(200).hacer_deposito(50).hacer_retiro(250).mostrar_balance()

monty.hacer_deposito(500).hacer_deposito(250).hacer_retiro(50).hacer_retiro(100).mostrar_balance()

homero.hacer_deposito(1500).hacer_retiro(200).hacer_retiro(50).hacer_retiro(150).mostrar_balance().transferencia(guido,200).mostrar_balance()
guido.mostrar_balance()
