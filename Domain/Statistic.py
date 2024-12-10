class Statistic:
    def __init__(self, country, year, inflation, unemployment,population):
        self.__country = country
        self.__year = year
        self.__inflation = inflation
        self.__unemployment = unemployment
        self.__population = population

    def __eq__(self, other):
        if isinstance(other, Statistic):
            return self.__country == other.__country and self.__year == other.__year

    @property
    def country(self):
        """
        Getter "property" pentru atributul tara.
        :return: valoarea tarii asociata instantei
        """
        return self.__country

    @property
    def year(self):
        return self.__year

    @property
    def inflation(self):
        return self.__inflation

    @property
    def unemployment(self):
        return self.__unemployment

    @property
    def population(self):
        return self.__population

    @unemployment.setter
    def unemployment(self, value):
        """
        Setter pentru rata de somaj.
        :param value: Noua valoare a ratei de somaj
        :return: None
        """
        self.__unemployment = value

    @population.setter
    def population(self, value):
        self.__population = value
    @inflation.setter
    def inflation(self, value):
        self.__inflation = value
