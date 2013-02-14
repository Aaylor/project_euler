#!/dev/bin/python

import time

def self_power(n_max=1000):
    return str(sum([x**x for x in range(1, 1001)]))[-10:]

if __name__ == "__main__":
    tStart = time.time()
    print("Answer : {}".format(self_power()))
    print("Done in {}s".format(time.time() - tStart))
