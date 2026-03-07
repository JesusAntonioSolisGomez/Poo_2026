class cuentaBancaria:
    def __init__(self, titular, numeroCuenta, saldo):
        self.titular = titular
        self.numeroCuenta = numeroCuenta
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo = self.saldo + cantidad

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo = self.saldo - cantidad
        else:
            print("Fondos insuficientes")

    def consultarSaldo(self):
        return self.saldo

    def mostrarInformacion(self):
        return f"{self.titular} tienes {self.saldo}"


# Crear cuenta1
cuenta1 = cuentaBancaria("Juan Perez", "001234567", 1000.0)

print(cuenta1.mostrarInformacion())

print("depositando dinero en la cuenta de Juan Perez...")

cuenta1.depositar(500.0)
print(cuenta1.mostrarInformacion())

print("retirando dinero de la cuenta de Juan Perez...")

cuenta1.retirar(2000.0)
print(f"Saldo actual: ${cuenta1.consultarSaldo()}")

cuenta1.retirar(2000.0)  # Fondos insuficientes

print("depositando dinero en la cuenta de Juan Perez...")

cuenta1.depositar(500.0)
print(cuenta1.mostrarInformacion())

print("------------")

# Crear cuenta2
cuenta2 = cuentaBancaria("Marcela Garcia", "0056789", 10500.0)

print(cuenta2.mostrarInformacion())

print("depositando dinero en la cuenta de Marcela Garcia...")

cuenta2.depositar(500.0)
print(cuenta2.mostrarInformacion())

print("retirando dinero de la cuenta de Marcela Garcia...") 

cuenta2.retirar(200.0)
print(f"Saldo actual: ${cuenta2.consultarSaldo()}")

print("retirando dinero de la cuenta de Marcela Garcia...")

cuenta2.retirar(20000.0)  # Fondos insuficientes

print("depositando dinero en la cuenta de Marcela Garcia...")

cuenta2.depositar(500.0)
print(cuenta2.mostrarInformacion())


