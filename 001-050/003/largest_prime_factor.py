#!/dev/bin/python

def largest_prime_number(number):
    divisor = 2
    largest = 0

    while number > 1:
        while number % divisor == 0:
            largest = divisor
            number /= divisor
        divisor += 1

    return largest

if __name__ == "__main__":
    print("Answer : {0}".format(largest_prime_number(600851475143)))