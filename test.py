import unittest

from main import min_, max_, sum_, multiply, read_array
from random import randint
from time import time, ctime


class MyTestCase(unittest.TestCase):
    def test_min(self):
        self.assertEqual(min_([1, 2, 3, 4, 5]), 1)
        self.assertIsNone(min_([]))
        self.assertEqual(min_([1, 1, 1]), 1)
        self.assertEqual(min_([1, 2, 3, 4, -5]), -5)
        rand_arr = [randint(-100, 100), randint(-100, 100), randint(-100, 100)]
        self.assertEqual(min_(rand_arr), min(rand_arr))

    def test_max(self):
        self.assertEqual(max_([1, 2, 3, 4, 5]), 5)
        self.assertIsNone(max_([]))
        self.assertEqual(max_([1, 1, 1]), 1)
        self.assertEqual(max_([1, 2, 3, 4, -5]), 1)
        rand_arr = [randint(-100, 100), randint(-100, 100), randint(-100, 100)]
        self.assertEqual(max_(rand_arr), max(rand_arr))

    def test_sum(self):
        self.assertEqual(sum_([1, 2, 3, 4, 5]), 15)
        self.assertEqual(sum_([]), 0)
        rand_arr = [randint(-100, 100), randint(-100, 100), randint(-100, 100)]
        self.assertEqual(sum(rand_arr), sum_(rand_arr))

    def test_multiply(self):
        self.assertEqual(multiply([1]), 1)
        self.assertEqual(multiply([-1]), -1)
        self.assertEqual(multiply([], 0))
        self.assertEqual(multiply([1, 2, 3, 4, 5]), 120)
        rand_arr = [randint(-100, 100), randint(-100, 100), randint(-100, 100)]
        r_test = rand_arr[0] * rand_arr[1] * rand_arr[2]
        self.assertEqual(r_test, multiply(rand_arr))

    def test_time(self):
        for size_m in [100, 500, 1000]:
            big_random_array = []
            for i in range(size_m):
                big_random_array.append(randint(-5, 5))
            begin = time()
            print(ctime(begin))
            multiply(big_random_array)
            end = time()
            print(ctime(end))
            self.assertLess(end - begin, size_m / 10)

    def custom_test(self):
        '''
        Testing how read_array works
        :return: Nothing
        '''
        self.assertEqual(read_array('read_array_test.txt', 0), [1, 2, 3, 4, 5])
        self.assertEqual(read_array('read_array_test.txt', 1), [10, 0])
        self.assertEqual(read_array('read_array_test.txt', 2), [-1])
        self.assertEqual(read_array('read_array_test.txt', 3), [1, 2, 3, 4])
        self.assertEqual(read_array('read_array_test.txt', 4), [])


if __name__ == '__main__':
    unittest.main()
