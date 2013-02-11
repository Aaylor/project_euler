#!/dev/bin/python

import time

def largest_prime_number(number):
    divisor = 1

    while number > 1:
        divisor += 1
        while number % divisor == 0:
            number /= divisor

    return divisor

if __name__ == "__main__":
    start = time.time()
    print("Answer : {0}".format(largest_prime_number(600851475143)))
    print("Done in {0}s".format(time.time() - start))
