from multiprocessing import Process, Queue
import time, os
import random


def w(q):
    rd = random.Random()
    for i in range(10):
        tm = rd.randrange(start=1, stop=10, step=1) / 10
        time.sleep(tm)
        q.put("d{} - {}".format(i, tm))


def r(q):
    while True:
        re = q.get(True)
        print(re)


if __name__ == "__main__":
    q = Queue()
    wp = Process(target=w, args=(q,))
    rp = Process(target=r, args=(q,))

    wp.start()
    rp.start()

    wp.join()
    rp.terminate()
