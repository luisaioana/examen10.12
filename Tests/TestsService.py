import shutil
import unittest
from Domain.Validator import Validator, ValidationException
from Repository.Repository import Repository
from Service.Service import Service

class TestService(unittest.TestCase):
    def setUp(self):
        shutil.copy('test_statistics_default.txt', 'test_statistics.txt')
        repository = Repository('test_statistics.txt')
        validator = Validator()
        self.service = Service(repository, validator)
    def test_add(self):
        self.service.add('test','test','5','5','5')
        self.assertEqual(len(self.service.get_all()), 7)
        with self.assertRaises(ValidationException):
            self.service.add('test','test','a','b','c')
    def test_filter(self):
        list1, list2 = self.service.filter_by_average_inflation(1.5)
        self.assertEqual(len(list1), 2)
        self.assertEqual(len(list2), 2)
        self.assertEqual(list1[0], 'Denmark')
        self.assertEqual(int(list2[0]), 139_200)
        self.assertEqual(list1[1], 'Italy')
        self.assertEqual(int(list2[1]), 3_011_040)
    def tearDown(self):
        with open('test_statistics.txt', 'w'):
            pass

if __name__ == '__main__':
    unittest.main()