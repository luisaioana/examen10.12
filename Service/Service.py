from Domain.Statistic import Statistic
from Domain.Validator import Validator
from Repository.Repository import Repository


class Service:
    def __init__(self,repository: Repository, validator:Validator):
        self.__repository = repository
        self.__validator = validator

    def add(self, country, year, inflation, unemployment, population):
        """
        Adauga o statistica cu atributele date in parametri in fisier.
        :param country: tara statisticii
        :param year: anul statisticii s.a.m.d.
        :param inflation:
        :param unemployment:
        :param population:
        :return:
        """
        statistic = Statistic(country, year, inflation, unemployment, population)
        self.__validator.validate(statistic)
        self.__repository.add(statistic)

    def filter_by_average_inflation(self, average_rate):
        """
        Returneaza 2 liste: prima cu tarile ce au rata inflatiei sub parametrul average_rate, iar a doua
        cu numarul maxim de someri pentru perioada inregistrata (index lista1 asociat index lista 2)
        :param average_rate:
        :return:
        """
        countries = []
        countries_with_property = []
        for statistic in self.__repository.get_all():
            if statistic.country not in countries:
                countries.append(statistic.country)
        for country in countries:
            sum_of_inflations= 0
            num_of_inflations = 0
            for statistic in self.__repository.get_all():
                if statistic.country == country:
                    sum_of_inflations += float(statistic.inflation)
                    num_of_inflations += 1
            if sum_of_inflations / num_of_inflations < float(average_rate):
                countries_with_property.append(country)
        maximum_unemployed = []
        for country in countries_with_property:
            maximum_unemployed_for_country = -1
            for statistic in self.__repository.get_all():
                if statistic.country == country:
                    unemployed_for_year = float(statistic.unemployment)*int(statistic.population)/100
                    if  unemployed_for_year > maximum_unemployed_for_country:
                        maximum_unemployed_for_country = unemployed_for_year
            maximum_unemployed.append(maximum_unemployed_for_country)
        return countries_with_property, maximum_unemployed

    def get_all(self):
        """
        Returneaza toate statisticile din fisier sub forma de lista.
        :return:
        """
        return self.__repository.get_all()






