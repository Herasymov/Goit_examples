import multiprocessing
from ctypes import c_char_p


def worker(num, arr, s):
    s.value = b"Hello world"
    num.value = 3.1415927
    for i in range(len(arr)):
        arr[i] = -arr[i]


if __name__ == '__main__':
    num = multiprocessing.Value('d', 0.0)
    arr = multiprocessing.Array('i', range(10))
    s = multiprocessing.Array('c', 15)

    p = multiprocessing.Process(target=worker, args=(num, arr, s))
    p.start()
    p.join()
    print(s.value)
    print(num.value)
    print(arr[:])
