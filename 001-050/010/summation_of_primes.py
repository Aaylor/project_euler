#!/dev/bin/python

import time

def summation_of_prime(n_max=2000000):
    prime_list = [2, 3, 5, 7]
    found = False
    
    while prime_list[-1] < n_max:
        for i in range(2, prime_list[-1], 2):
            test = prime_list[-1] + i
           
            div_max = test ** (1/2)
            for j in prime_list:
                if j <= div_max:
                    if test % j == 0:
                        break
                else:
                    found = True
                    prime_list.append(test)
                    break
            if found:
                found = False
                break

    return sum(prime_list[:-1])

if __name__ == "__main__":
    tStart = time.time()
    print("Answer : {}".format(summation_of_prime()))
    print("Done in {}s".format(time.time() - tStart))
