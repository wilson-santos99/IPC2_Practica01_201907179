# cuenta_monetaria.py
# Este módulo contiene la clase CuentaMonetaria, que hereda de la clase base Cuenta.
# La clase CuentaMonetaria añade funcionalidades específicas para cuentas monetarias, como un límite de crédito.
# Se ha añadido manejo de excepciones para evitar errores inesperados.

from modulos.cuenta import Cuenta  # Importar la clase base Cuenta

class CuentaMonetaria(Cuenta):
    """
    Clase CuentaMonetaria: Representa una cuenta monetaria bancaria.
    Hereda de la clase Cuenta y añade un límite de crédito para permitir retiros adicionales.
    """

    def __init__(self, titular, saldo_inicial=0, limite_credito=1000):
        """
        Constructor de la clase CuentaMonetaria.

        Parámetros:
        - titular: Nombre del titular de la cuenta (str).
        - saldo_inicial: Saldo inicial de la cuenta (float). Por defecto es 0.
        - limite_credito: Límite de crédito adicional para la cuenta (float). Por defecto es 1000.

        Excepciones:
        - ValueError: Si el saldo inicial o el límite de crédito son negativos.
        """
        try:
            if saldo_inicial < 0:
                raise ValueError("El saldo inicial no puede ser negativo.")
            if limite_credito < 0:
                raise ValueError("El límite de crédito no puede ser negativo.")
            
            # Llama al constructor de la clase base (Cuenta)
            super().__init__(titular, saldo_inicial)
            self.limite_credito = limite_credito  # Asigna el límite de crédito
        except ValueError as e:
            print(f"Error al crear la cuenta monetaria: {e}")
            raise  # Relanza la excepción para que el programa no continúe con valores inválidos

    def retirar(self, cantidad):
        """
        Sobrescribe el método retirar de la clase base para permitir retiros que excedan el saldo,
        siempre y cuando no superen el límite de crédito.

        Parámetros:
        - cantidad: Cantidad a retirar (float).

        Retorna:
        - True si el retiro fue exitoso.
        - False si el retiro no fue posible (supera el saldo + límite de crédito).

        Excepciones:
        - ValueError: Si la cantidad es negativa o cero.
        """
        try:
            if cantidad <= 0:
                raise ValueError("La cantidad a retirar debe ser positiva.")
            if (self.saldo + self.limite_credito) < cantidad:
                raise ValueError("Fondos insuficientes (incluyendo límite de crédito).")
            
            self.saldo -= cantidad  # Actualiza el saldo
            return True  # Retiro exitoso
        except ValueError as e:
            print(f"Error al retirar: {e}")
            return False  # Retiro fallido

    def mostrar_informacion(self):
        """
        Muestra la información de la cuenta monetaria, incluyendo el límite de crédito.

        Retorna:
        - Una cadena con la información de la cuenta (str).
        """
        return (super().mostrar_informacion() +
                f"\nLímite de crédito: {self.limite_credito:.2f}")