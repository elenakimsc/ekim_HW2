FILEPATH = 'input.txt'


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
        print('Array must contain elements')
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
    s = 0
    for item in array:
        s += item
    return s


def multiply(array):
    if len(array) == 0:
        return 0
    m = 1
    for item in array:
        m *= item
    return m


if __name__ == '__main__':
    arr = read_array(FILEPATH)
    print(min_(arr))
    print(max_(arr))
    print(sum_(arr))
    print(multiply(arr))
