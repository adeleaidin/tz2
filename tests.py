import time
import unittest
from functions import _max, _min, _mult, _razmah, _sum  # мой тест
class TestAllMethods(unittest.TestCase):
        file = list(map(int, open('file').readline().split(' ')))
        def test_min(self):
                timeStart = time.time()
                self.assertEqual(_min(self.file), 2)
                print('Время работы функции test_min = ', time.time() - timeStart)
        def test_max(self):
                timeStart = time.time()
                self.assertEqual(_max(self.file), 13)
                print('Время работы функции test_max = ', time.time() - timeStart)
        def test_sum(self):
                timeStart = time.time()
                self.assertEqual(_sum(self.file), 28)
                print('Время работы функции test_sum = ', time.time() - timeStart)
        def test_mult(self):
                timeStart = time.time()
                self.assertEqual(_mult(self.file), 1040)
                print('Время работы функции test_mult = ', time.time() - timeStart)
        def test_razmah(self):
                timeStart = time.time()
                self.assertEqual(_razmah(self.file), 11)
                print('Время работы функции test_razmah = ', time.time() - timeStart)

        file2 = list(map(int, open('file2').readline().split(' ')))
        def test_min2(self):
                timeStart = time.time()
                self.assertEqual(_min(self.file2), 3)
                print('Время работы функции test_min2 = ', time.time() - timeStart)
        def test_max2(self):
                timeStart = time.time()
                self.assertEqual(_max(self.file2), 12)
                print('Время работы функции test_max2 = ', time.time() - timeStart)
        def test_sum2(self):
                timeStart = time.time()
                self.assertEqual(_sum(self.file2), 30)
                print('Время работы функции test_sum2 = ', time.time() - timeStart)
        def test_mult2(self):
                timeStart = time.time()
                self.assertEqual(_mult(self.file2), 1944)
                print('Время работы функции test_mult2 = ', time.time() - timeStart)
        def test_razmah2(self):
                timeStart = time.time()
                self.assertEqual(_razmah(self.file2), 9)
                print('Время работы функции test_razmah2 = ', time.time() - timeStart)

        file3 = list(map(int, open('file3').readline().split(' ')))
        def test_min3(self):
                timeStart = time.time()
                self.assertEqual(_min(self.file3), 1)
                print('Время работы функции test_min3 = ', time.time() - timeStart)
        def test_max3(self):
                timeStart = time.time()
                self.assertEqual(_max(self.file3), 10)
                print('Время работы функции test_max3 = ', time.time() - timeStart)
        def test_sum3(self):
                timeStart = time.time()
                self.assertEqual(_sum(self.file3), 23)
                print('Время работы функции test_sum3 = ', time.time() - timeStart)
        def test_mult3(self):
                timeStart = time.time()
                self.assertEqual(_mult(self.file3), 350)
                print('Время работы функции test_mult3 = ', time.time() - timeStart)
        def test_razmah3(self):
                timeStart = time.time()
                self.assertEqual(_razmah(self.file3), 9)
                print('Время работы функции test_razmah3 = ', time.time() - timeStart)

        file4 = list(map(int, open('file4').readline().split(' ')))
        def test_min4(self):
                timeStart = time.time()
                self.assertEqual(_min(self.file4), 0)
                print('Время работы функции test_min4 = ', time.time() - timeStart)
        def test_max4(self):
                timeStart = time.time()
                self.assertEqual(_max(self.file4), 9999)
                print('Время работы функции test_max4 = ', time.time() - timeStart)
        def test_sum4(self):
                timeStart = time.time()
                self.assertEqual(_sum(self.file4), 49995000)
                print('Время работы функции test_sum4 = ', time.time() - timeStart)
        def test_mult4(self):
                timeStart = time.time()
                self.assertEqual(_mult(self.file4), 0)
                print('Время работы функции test_mult4 = ', time.time() - timeStart)
        def test_razmah4(self):
                timeStart = time.time()
                self.assertEqual(_razmah(self.file4), 9999)
                print('Время работы функции test_razmah4 = ', time.time() - timeStart)


if __name__ == '__main__':
    unittest.main()