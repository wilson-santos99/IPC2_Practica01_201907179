# banco.py
# Este módulo contiene la clase Banco, que se encarga de gestionar las cuentas bancarias.

class Banco:
    """
    Clase Banco: Gestiona una lista de cuentas bancarias.
    Permite agregar cuentas y buscar cuentas por su número.
    """

    def __init__(self):
        """
        Constructor de la clase Banco.
        Inicializa una lista vacía para almacenar las cuentas bancarias.
        """
        self.cuentas = []  # Lista para almacenar las cuentas

    def agregar_cuenta(self, cuenta):
        """
        Agrega una cuenta a la lista de cuentas del banco.

        Parámetros:
        - cuenta: Objeto de tipo Cuenta (o sus subclases CuentaAhorro o CuentaMonetaria).
        """
        self.cuentas.append(cuenta)  # Añade la cuenta a la lista
        print(f"Cuenta agregada exitosamente. Número de cuenta: {cuenta.numero_cuenta}")

    def buscar_cuenta(self, numero_cuenta):
        """
        Busca una cuenta en la lista de cuentas del banco por su número de cuenta.

        Parámetros:
        - numero_cuenta: Número de cuenta a buscar (cadena de 16 dígitos).

        Retorna:
        - La cuenta si se encuentra.
        - None si no se encuentra ninguna cuenta con ese número.
        """
        # Recorre todas las cuentas en la lista
        for cuenta in self.cuentas:
            # Compara el número de cuenta con el proporcionado
            if cuenta.numero_cuenta == numero_cuenta:
                return cuenta  # Retorna la cuenta si coincide
        return None  # Retorna None si no se encuentra la cuenta

    def mostrar_todas_las_cuentas(self):
        """
        Muestra la información de todas las cuentas registradas en el banco.
        """
        if not self.cuentas:  # Si no hay cuentas
            print("No hay cuentas registradas en el banco.")
        else:
            print("--- Información de todas las cuentas ---")
            # Recorre todas las cuentas y muestra su información
            for cuenta in self.cuentas:
                print(cuenta.mostrar_informacion())
                print("-----------------------------")