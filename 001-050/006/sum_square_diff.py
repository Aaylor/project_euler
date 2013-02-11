#!/dev/bin/python

import time

def sum_square_diff(n_max):
    sum_of_the_square = sum([x**2 for x in range(1,n_max+1)])
    square_of_the_sum = (((n_max*(n_max+1))//2)**2)
    return square_of_the_sum - sum_of_the_square

if __name__ == "__main__":
    tStart = time.time()
    print("Answer : {0}".format(sum_square_diff(100)))
    print("Done in {0}s".format(time.time() - tStart))

