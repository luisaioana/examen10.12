import shutil
import unittest

from Domain.Statistic import Statistic
from Repository.Repository import Repository, DuplicateObjectException


class TestRepository(unittest.TestCase):
    def setUp(self):
        shutil.copy('test_statistics_default.txt', 'test_statistics.txt')
        self.repository = Repository("test_statistics.txt")

    def test_add(self):
        self.assertEqual(len(self.repository.get_all()), 6)
        self.repository.add(Statistic("test", "test", "test", "test", "test"))
        self.assertEqual(len(self.repository.get_all()), 7)
        with self.assertRaises(DuplicateObjectException):
            self.repository.add(Statistic("test", "test", "test", "test", "test"))

    def test_get_all(self):
        self.assertEqual(len(self.repository.get_all()), 6)
        self.assertEqual(self.repository.get_all()[0].year, "2024")
        self.assertEqual(self.repository.get_all()[0].country, "Denmark")

    def tearDown(self):
        with open('test_statistics.txt', 'w'):
            pass

if __name__ == '__main__':
    unittest.main()
