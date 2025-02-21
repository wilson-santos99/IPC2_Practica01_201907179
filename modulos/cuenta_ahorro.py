# cuenta_ahorro.py
# Este módulo contiene la clase CuentaAhorro, que hereda de la clase base Cuenta.
# La clase CuentaAhorro añade funcionalidades específicas para cuentas de ahorro, como el cálculo de intereses.

from modulos.cuenta import Cuenta  # Importar la clase base Cuenta

class CuentaAhorro(Cuenta):
    """
    Clase CuentaAhorro: Representa una cuenta de ahorro bancaria.
    Hereda de la clase Cuenta y añade una tasa de interés para calcular intereses.
    """

    def __init__(self, titular, saldo_inicial=0, tasa_interes=0.05):
        """
        Constructor de la clase CuentaAhorro.

        Parámetros:
        - titular: Nombre del titular de la cuenta (str).
        - saldo_inicial: Saldo inicial de la cuenta (float). Por defecto es 0.
        - tasa_interes: Tasa de interés de la cuenta (float). Por defecto es 0.05 (5%).
        """
        # Llama al constructor de la clase base (Cuenta)
        super().__init__(titular, saldo_inicial)
        self.tasa_interes = tasa_interes  # Asigna la tasa de interés

    def calcular_interes(self):
        """
        Calcula el interés basado en el saldo actual y la tasa de interés.
        Luego, añade el interés al saldo de la cuenta.

        Retorna:
        - El monto del interés calculado (float).
        """
        interes = self.saldo * self.tasa_interes  # Calcula el interés
        self.depositar(interes)  # Añade el interés al saldo
        return interes  # Retorna el monto del interés

    def mostrar_informacion(self):
        """
        Muestra la información de la cuenta de ahorro, incluyendo la tasa de interés.

        Retorna:
        - Una cadena con la información de la cuenta (str).
        """
        # Llama al método mostrar_informacion de la clase base y añade la tasa de interés
        return (super().mostrar_informacion() +
                f"\nTasa de interés: {self.tasa_interes * 100:.2f}%")