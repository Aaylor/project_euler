#!/dev/bin/python

import time

def find_prime_number(n_max):
    prime_numbers = [2, 3, 5, 7]
    while len(prime_numbers) != n_max:
        for i in range(2, prime_numbers[-1], 2):
            found = False
            test = prime_numbers[-1] + i
            for j in prime_numbers:
                if j <= (test ** (1/2)):
                    if test % j == 0:
                        break
                else:
                    prime_numbers.append(test)
                    found = True
                    break
            if found:
                break
    return prime_numbers[-1]

if __name__ == "__main__":
    tStart = time.time()
    print("Answer : {0}".format(find_prime_number(10001)))
    print("Done in {0}s".format(time.time() - tStart))

