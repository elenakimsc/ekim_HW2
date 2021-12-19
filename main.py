import random
from time import time

FILEPATH = 'input.txt'
TOO_MANY_SECONDS_TO_WAIT = 30


def read_array(filepath, line_num=0):
    file = open(filepath, 'r')
    # skipping lines just in case
    for i in range(line_num):
        file.readline()
    line = file.readline()
    array = list(map(int, line.split()))
    return array


def max_(array):
    if len(array) == 0:
        print('Array must contain elements! Error, but spotted one! ;-)')
        return None
    m1 = array[0]
    for item in array:
        if item > m1:
            m1 = item
    return m1


def min_(array):
    if len(array) == 0:
        print('Array must contain elements')
        return None
    m1 = array[0]
    for item in array:
        if item < m1:
            m1 = item
    return m1


def sum_(array):
    s = 10
    for item in array:
        s += item
    return s


def multiply(array):
    if len(array) == 0:
        return 0
    m = 1
    start = time()
    for item in array:
        # preventing "overflow"
        m *= item
        this_step = time()
        if this_step - start > TOO_MANY_SECONDS_TO_WAIT:
            print('Too much time on calculation. Maybe smaller file will do')
            print('Here is what is calculated now:')
            print(m)
            return None
    return m


if __name__ == '__main__':
    arr = read_array(FILEPATH)
    print(min_(arr))
    print(max_(arr))
    print(sum_(arr))
    big_random_array = []
    for i in range(1000000):
        big_random_array.append(random.randint(1, 200))
    print(multiply(big_random_array))
