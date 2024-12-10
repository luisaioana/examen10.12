from Domain.Statistic import Statistic


class ValidationException(Exception):
    def __init__(self, message):
        super().__init__(f'ValidationException:{message}')

class Validator:
    def validate(self, statistic: Statistic):
        """
        Valideaza atributele inflatie (numar zecimal > 0), rata somaj (numar zecimal > 0), populatie (numar > 0)
        ale parametrului statistic. Arunca exceptie ValidationException in caz contrar.
        :param statistic:
        :return:
        """
        errors = []
        try:
            statistic.unemployment = float(statistic.unemployment)
            statistic.inflation = float(statistic.inflation)
            if statistic.inflation < 0 or statistic.unemployment < 0:
                errors.append("Inflation and/or unemployment rate should be a positive integer")
        except ValueError:
            errors.append("Unemployment rate and/or inflation should be a float")
        try:
            statistic.population = int(statistic.population)
            if statistic.population < 1:
                errors.append("Population should be a positive integer")
        except ValueError:
            errors.append("Population should be a number")
        if len(errors) > 0:
            error_message = ','.join(errors)
            raise ValidationException(error_message)