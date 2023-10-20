class Usuario:
    nombre_banco = 'Primer Dojo Nacional'
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.balance_cuenta = 0
    
    def hacer_deposito(self, monto):
        self.balance_cuenta += monto

    def hacer_retiro(self, monto):
        self.balance_cuenta-=monto
    
    def mostrar_balance(self):
        print(f'Usuario: {self.name}, Balance: {self.balance_cuenta}',)
    
    def transferencia(self, destinatario,monto):
        self.balance_cuenta -= monto
        destinatario.balance_cuenta += monto
        print(f'Se han transferido {monto} al destinatario')


guido = Usuario('Guido Van Eossum','guiudo@python.com')
monty = Usuario('Montgemery Bernz','Monty@python.com')
homero = Usuario('Homero Simpson', ('homero@python.com'))


guido.hacer_deposito(100)
guido.hacer_deposito(200)
guido.hacer_deposito(50)
guido.hacer_retiro(250)

guido.mostrar_balance()

monty.hacer_deposito(500)
monty.hacer_deposito(250)
monty.hacer_retiro(50)
monty.hacer_retiro(100)

monty.mostrar_balance()

homero.hacer_deposito(1500)
homero.hacer_retiro(200)
homero.hacer_retiro(50)
homero.hacer_retiro(150)

homero.mostrar_balance()
print('\n')
homero.transferencia(guido,200)

homero.mostrar_balance()
guido.mostrar_balance()
