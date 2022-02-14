import threading
import time


class Thr1(threading.Thread):
    def __init__(self, var):
        threading.Thread.__init__(self)
        self.var = var

    def run(self):
        num = 1
        while num < 10:
            y = num*num + num / (num - 10)
            num += 1
            print("num =", num, " function y =", y)
            time.sleep(self.var)


x = Thr1(0.9)
x.start()
time.sleep(3)
print("MainThread is finished")
