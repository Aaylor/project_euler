#!/dev/bin/python

#   Find the sum of all the multiples of 3 or 5 below 1000
def _sum():
    return sum([x for x in range(1, 1000) if x % 3 == 0 or x % 5 == 0])

if __name__ == "__main__":
    print("Answer : {0}".format(_sum()))

