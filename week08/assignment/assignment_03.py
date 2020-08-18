import time

def timer(func, *args, **kwargs):
    def warpper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f'{func.__name__}运行时间: {end_time - start_time}.')
    return warpper

@timer
def sum_10000000():
    sum = 0
    for i in range(10000000):
        sum += i
    print(sum)

if __name__ == "__main__":
    sum_10000000()
