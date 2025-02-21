# cuenta.py
# Este módulo contiene la clase base Cuenta, que representa una cuenta bancaria genérica.
# Proporciona las funcionalidades básicas como depósitos, retiros y mostrar información.
# Se ha añadido manejo de excepciones para evitar errores inesperados.

import random  # Importar el módulo random para generar números de cuenta aleatorios

class Cuenta:
    """
    Clase Cuenta: Representa una cuenta bancaria genérica.
    Contiene atributos como titular, número de cuenta y saldo, y métodos para gestionar la cuenta.
    """

    def __init__(self, titular, saldo_inicial=0):
        """
        Constructor de la clase Cuenta.

        Parámetros:
        - titular: Nombre del titular de la cuenta (str).
        - saldo_inicial: Saldo inicial de la cuenta (float). Por defecto es 0.

        Excepciones:
        - ValueError: Si el saldo inicial es negativo.
        """
        try:
            if saldo_inicial < 0:
                raise ValueError("El saldo inicial no puede ser negativo.")
            self.titular = titular  # Asigna el nombre del titular
            self.numero_cuenta = self.generar_numero_cuenta()  # Genera un número de cuenta único
            self.saldo = saldo_inicial  # Asigna el saldo inicial
        except ValueError as e:
            print(f"Error al crear la cuenta: {e}")
            raise  # Relanza la excepción para que el programa no continúe con valores inválidos

    def generar_numero_cuenta(self):
        """
        Genera un número de cuenta aleatorio de 16 dígitos.

        Retorna:
        - Una cadena con el número de cuenta generado (str).
        """
        return ''.join([str(random.randint(0, 9)) for _ in range(16)])  # Genera 16 dígitos aleatorios

    def depositar(self, cantidad):
        """
        Realiza un depósito en la cuenta.

        Parámetros:
        - cantidad: Cantidad a depositar (float).

        Retorna:
        - True si el depósito fue exitoso.
        - False si la cantidad es inválida (negativa o cero).

        Excepciones:
        - ValueError: Si la cantidad es negativa o cero.
        """
        try:
            if cantidad <= 0:
                raise ValueError("La cantidad a depositar debe ser positiva.")
            self.saldo += cantidad  # Añade la cantidad al saldo
            return True  # Depósito exitoso
        except ValueError as e:
            print(f"Error al depositar: {e}")
            return False  # Depósito fallido

    def retirar(self, cantidad):
        """
        Realiza un retiro de la cuenta.

        Parámetros:
        - cantidad: Cantidad a retirar (float).

        Retorna:
        - True si el retiro fue exitoso.
        - False si la cantidad es inválida (negativa o cero) o si no hay suficiente saldo.

        Excepciones:
        - ValueError: Si la cantidad es negativa o cero.
        """
        try:
            if cantidad <= 0:
                raise ValueError("La cantidad a retirar debe ser positiva.")
            if self.saldo < cantidad:
                raise ValueError("Saldo insuficiente para realizar el retiro.")
            self.saldo -= cantidad  # Resta la cantidad del saldo
            return True  # Retiro exitoso
        except ValueError as e:
            print(f"Error al retirar: {e}")
            return False  # Retiro fallido

    def mostrar_informacion(self):
        """
        Muestra la información básica de la cuenta.

        Retorna:
        - Una cadena con la información de la cuenta (str).
        """
        return (f"Titular: {self.titular}\n"
                f"Número de cuenta: {self.numero_cuenta}\n"
                f"Saldo: {self.saldo:.2f}")