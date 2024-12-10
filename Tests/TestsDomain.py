import unittest

from Domain.Statistic import Statistic
from Domain.Validator import ValidationException, Validator


class TestDomain(unittest.TestCase):
    def setUp(self):
        self.validator = Validator()
        pass
    def test_getters(self):
        statistic = Statistic('Romania',"2024",'1.2','3','18_000_000')
        self.assertEqual(statistic.year,"2024")
        self.assertEqual(statistic.country,'Romania')
        self.assertEqual(statistic.inflation, '1.2')
        self.assertEqual(statistic.unemployment, '3')
        self.assertEqual(statistic.population, '18_000_000')
    def test_setters(self):
        statistic = Statistic('Romania', "2024", '1.2', '3', '18_000_000')
        statistic.inflation = "1.4"
        statistic.unemployment = "7"
        statistic.population = "17_070_000"
        self.assertEqual(statistic.inflation,"1.4")
        self.assertEqual(statistic.unemployment,"7")
        self.assertEqual(statistic.population,"17_070_000")

    def test_validator(self):
        statistic = Statistic('Romania', "2024", 'test', '3', '18_000_000')
        with self.assertRaises(ValidationException):
            self.validator.validate(statistic)
        statistic = Statistic('Romania', "2024", '6', 'test', '18_000_000')
        with self.assertRaises(ValidationException):
            self.validator.validate(statistic)
        statistic = Statistic('Romania', "2024", '6', '3', 'test')
        with self.assertRaises(ValidationException):
            self.validator.validate(statistic)
        statistic = Statistic('Romania', "2024", '-6', '3', '8')
        with self.assertRaises(ValidationException):
            self.validator.validate(statistic)
        statistic = Statistic('Romania', "2024", '6', '-3', '8')
        with self.assertRaises(ValidationException):
            self.validator.validate(statistic)
        statistic = Statistic('Romania', "2024", '6', '3', '-8')
        with self.assertRaises(ValidationException):
            self.validator.validate(statistic)
    def test_eq(self):
        statistic1 = Statistic('Romania', "2024", '0', '0', '0')
        statistic2 = Statistic('Romania', "2024", '1', '1', '1')
        self.assertEqual(statistic1, statistic2)


    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()