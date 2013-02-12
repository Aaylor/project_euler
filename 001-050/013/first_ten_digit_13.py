#!/bin/env/python

import time        

def read_file(filename="first_ten_digit_13.txt"):
    primary_list = []
    _file = open(filename)
    
    for line in _file:
        primary_list.append(int(line))
    return primary_list

def first_ten_digit(n_list):
    return str(sum(n_list))[:10]

if __name__ == "__main__":
    tStart = time.time()
    n_list = read_file()
    print("Answer : {}".format(first_ten_digit(n_list)))
    print("Done in {}s".format(time.time() - tStart))
