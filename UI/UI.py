from Service.Service import Service


class UI:
    def __init__(self, service: Service):
        self.__service = service

    def add(self):
        country = input("country:")
        year = input("year:")
        inflation = input("inflation:")
        unemployment = input("unemployment:")
        population = input("population:")
        self.__service.add(country, year, inflation, unemployment, population)
    def print_both_lists(self, list1, list2):
        if list1 == [] or list2 == []:
            return False
        for index in range(len(list1)):
            print(f'{list1[index]}, {int(list2[index])}')
    def filter_by_average_inflation(self):
        average_inflation = input("average inflation:")
        countries_with_property, maximum_unemployed = self.__service.filter_by_average_inflation(average_inflation)
        self.print_both_lists(countries_with_property, maximum_unemployed)

    def menu(self):
        print('MENU')
        print('1. Add')
        print('2.Countries with medium inflation less than a number')
        print('e.Exit')

    def run(self):
        while True:
            self.menu()
            option = input('OPTION:')
            try:
                if option == '1':
                    self.add()
                if option == '2':
                    self.filter_by_average_inflation()
                if option == 'e':
                    break
            except Exception as e:
                print(e)