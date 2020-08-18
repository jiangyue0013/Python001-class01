def my_map(func, iterables):
    for args in iterables:
        yield func(args)


def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

if __name__ == "__main__":
    list1 = [1, 2, 3]
    res = my_map(add, list1)
    for i in res:
        print(i)