from Domain.Statistic import Statistic
class DuplicateObjectException(Exception):
    def __init__(self):
        super().__init__("Duplicate object detected")


class Repository:
    def __init__(self, file_name):
        self.__file_name = file_name

    def add(self, statistic: Statistic):
        '''
        Adauga statistica in fisier.
        :param statistic: statistica de adaugat la fisier
        :return:
        '''
        if statistic in self.get_all():
            raise DuplicateObjectException()
        try:
            with open(self.__file_name, 'a') as file:
                statistic_line = f'\n{statistic.country},{statistic.year},{statistic.inflation},{statistic.unemployment},{statistic.population}'
                file.write(statistic_line)
        except IOError:
            pass

    def __load_from_file(self):
        """
        Functie privata de citire din fisier a statisticilor.
        :return: statisticile din fisier intr-o lista
        """
        statistics = []
        try:
            with open(self.__file_name, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    line = line.strip()
                    if line:
                        country, year, inflation, unemployment, population = line.split(',')
                        statistics.append(Statistic(country, year, inflation, unemployment, population))
                return statistics
        except IOError:
            pass

    def get_all(self):
        '''
        Returneaza lista de statistici din fisier
        :return: lista de statistici din fisier
        '''
        statistics = self.__load_from_file()
        return statistics
