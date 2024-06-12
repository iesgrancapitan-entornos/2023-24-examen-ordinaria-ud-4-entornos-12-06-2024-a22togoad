"""
Clase Coche base para el Examen de la UD4
Refactorización
Extrae una superclase Vehículo con los campos
    num_serie
    fabricante
    color
:autor: Jaime Rabasco
"""


class Coche:
    """
    Clase Coche
    """
    num_serie = 1
    cilindrada = 1000
    fabricante = 'seat'
    color = 'rojo'

    def __init__(self, num_serie, cilindrada, fabricante, color):
        """
        Constructor de la clase coche
        :param num_serie: Número de serie del coche
        :param cilindrada: Cilindrada del coche
        :param fabricante: Nombre del fabricante del coche
        :param color: Color del coche
        """
        self.num_serie = num_serie
        self.cilindrada = cilindrada
        self.fabricante = fabricante
        self.color = color

    @property
    def num_serie(self):
        """
        Número de serie
        :return: Devuelve el número de serie
        """
        return self.__num_serie

    @num_serie.setter
    def num_serie(self, value):
        """
        Número de serie
        :param value: Valor a establecer
        :return: Establece un número de serie
        """
        self.__num_serie = value

    @property
    def color(self):
        """
        Color del coche
        :return: Devuelve el color del coche
        """
        return self.__color

    @color.setter
    def color(self, value: int):
        """
        Color del coche
        :param value: Valor a establecer
        :return: Establece un color al coche
        """
        self.__color = value

    @property
    def cilindrada(self):
        """
        Cilindrada
        :return: Devuelve la cilindrada del coche
        """
        return self.__cilindrada

    @cilindrada.setter
    def cilindrada(self, value):
        """
        Cilindrada
        :param value: Valor a establecer
        :return: Establece la cilindrada del coche
        """
        self.__cilindrada = value

    @property
    def fabricante(self):
        """
        Nombre del fabricante
        :return: Devuelve el nombre del fabricante
        """
        return self.__fabricante

    @fabricante.setter
    def fabricante(self, value):
        """
        Nombre del fabricante
        :param value: Valor a establecer
        :return: Establece el nombre del fabricante
        """
        self.__fabricante = value


class Vehiculo(Coche):
    """
    Clase Vehiculo que hereda de la clase Coche
    """
    def __init__(self, num_serie, fabricante, color):
        """
        Constructor de la clase Vehiculo
        :param num_serie: Número de serie del vehículo
        :param fabricante: Nombre del fabricante del vehículo
        :param color: Color del vehículo
        """
        super().__init__(num_serie, fabricante, color)
