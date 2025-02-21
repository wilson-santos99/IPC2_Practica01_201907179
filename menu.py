# menu.py
# Este módulo contiene la lógica del menú interactivo en consola para gestionar cuentas bancarias.
# Se ha añadido manejo de excepciones para evitar errores inesperados.

from modulos.banco import Banco
from modulos.cuenta_ahorro import CuentaAhorro
from modulos.cuenta_monetaria import CuentaMonetaria

def mostrar_menu_principal():
    """
    Muestra el menú principal de la aplicación.
    """
    print("---Menu Bancario---")
    print("1. Abrir Cuenta")
    print("2. Gestionar Cuenta")
    print("3. Salir")

def mostrar_menu_gestion():
    """
    Muestra el menú de gestión de cuentas.
    """
    print("---Menu Bancario---")
    print("1. Ver información de cuentas")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Calcular interés (Solo Cuenta de Ahorro)")
    print("5. Regresar")

def main():
    """
    Función principal que maneja la lógica del programa.
    """
    banco = Banco()  # Crear una instancia del banco para gestionar cuentas

    while True:
        try:
            mostrar_menu_principal()
            opcion = input("Seleccione una opción: ")

            # Opción 1: Abrir una nueva cuenta
            if opcion == "1":
                print("1. Cuenta de ahorro")
                print("2. Cuenta monetaria")
                print("3. Regresar")
                tipo_cuenta = input("Seleccione una opción: ")

                if tipo_cuenta == "1":
                    try:
                        titular = input("Ingrese el nombre del titular: ")
                        saldo_inicial = float(input("Ingrese el saldo inicial: "))
                        tasa_interes = float(input("Ingrese la tasa de interés: "))
                        cuenta = CuentaAhorro(titular, saldo_inicial, tasa_interes)
                        banco.agregar_cuenta(cuenta)
                        print(f"Cuenta de ahorro creada exitosamente. Número de cuenta: {cuenta.numero_cuenta}")
                    except ValueError as e:
                        print(f"Error al crear la cuenta de ahorro: {e}")

                elif tipo_cuenta == "2":
                    try:
                        titular = input("Ingrese el nombre del titular: ")
                        saldo_inicial = float(input("Ingrese el saldo inicial: "))
                        limite_credito = float(input("Ingrese el límite de crédito: "))
                        cuenta = CuentaMonetaria(titular, saldo_inicial, limite_credito)
                        banco.agregar_cuenta(cuenta)
                        print(f"Cuenta monetaria creada exitosamente. Número de cuenta: {cuenta.numero_cuenta}")
                    except ValueError as e:
                        print(f"Error al crear la cuenta monetaria: {e}")

                elif tipo_cuenta == "3":
                    continue  # Regresar al menú principal
                else:
                    print("Opción no válida.")

            # Opción 2: Gestionar una cuenta existente
            elif opcion == "2":
                try:
                    numero_cuenta = input("Ingrese el número de cuenta: ")
                    cuenta = banco.buscar_cuenta(numero_cuenta)
                    if cuenta:
                        while True:
                            try:
                                mostrar_menu_gestion()
                                opcion_gestion = input("Seleccione una opción: ")

                                # Opción 1: Ver información de la cuenta
                                if opcion_gestion == "1":
                                    print(cuenta.mostrar_informacion())

                                # Opción 2: Depositar dinero
                                elif opcion_gestion == "2":
                                    try:
                                        cantidad = float(input("Ingrese la cantidad a depositar: "))
                                        if cuenta.depositar(cantidad):
                                            print(f"Depósito exitoso. Nuevo saldo: {cuenta.saldo:.2f}")
                                        else:
                                            print("Depósito fallido.")
                                    except ValueError as e:
                                        print(f"Error al depositar: {e}")

                                # Opción 3: Retirar dinero
                                elif opcion_gestion == "3":
                                    try:
                                        cantidad = float(input("Ingrese la cantidad a retirar: "))
                                        if cuenta.retirar(cantidad):
                                            print(f"Retiro exitoso. Nuevo saldo: {cuenta.saldo:.2f}")
                                        else:
                                            print("Retiro fallido.")
                                    except ValueError as e:
                                        print(f"Error al retirar: {e}")

                                # Opción 4: Calcular interés (solo para cuentas de ahorro)
                                elif opcion_gestion == "4":
                                    if isinstance(cuenta, CuentaAhorro):
                                        interes = cuenta.calcular_interes()
                                        print(f"Interés de {interes:.2f} añadido a la cuenta de ahorro.")
                                    else:
                                        print("Esta operación solo es válida para cuentas de ahorro.")

                                # Opción 5: Regresar al menú principal
                                elif opcion_gestion == "5":
                                    break

                                else:
                                    print("Opción no válida.")
                            except Exception as e:
                                print(f"Error inesperado: {e}")
                    else:
                        print("Cuenta no encontrada.")
                except Exception as e:
                    print(f"Error al gestionar la cuenta: {e}")

            # Opción 3: Salir del programa
            elif opcion == "3":
                print("Saliendo del sistema...")
                break

            else:
                print("Opción no válida.")
        except Exception as e:
            print(f"Error inesperado: {e}")

# Punto de entrada del programa
if __name__ == "__main__":
    main()