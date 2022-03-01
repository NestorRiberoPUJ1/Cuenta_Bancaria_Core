from cuentaBancaria import cuentaBancaria,Usuario

Ahorros = cuentaBancaria(1000, 1.2)
Corriente = cuentaBancaria(0, 1)

Ahorros.deposito(1000).deposito(200).deposito(250).retiro(1800).generar_interes().mostrar_info_cuenta()

Corriente.deposito(2000).deposito(3000).retiro(1000).retiro(100).retiro(250).retiro(500).generar_interes().mostrar_info_cuenta()

cuentaBancaria.imprimirInstancias()


John=Usuario("John","JohnAlex@Castaño.com",{"Ahorros":cuentaBancaria(0,1)})

John.hacer_deposito(1000,"Ahorros")
John.mostrarBalance("Ahorros")
