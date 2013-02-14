#!/dev/bin/python

import time

def fac_rec(n):
    if n == 1:
        return 1
    return n * fac_rec(n-1)

def factorial_digit_sum(n=100):
    return sum(list(map(int, list(str(fac_rec(n))))))

if __name__ == "__main__":
    tStart = time.time()
    print("Answer : {}".format(factorial_digit_sum()))
    print("Done in {}s".format(time.time() - tStart))
