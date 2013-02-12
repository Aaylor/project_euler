#!/bin/env/python

import time

def _read_file(filename="largest_product_11.txt"):
    primary_list = []

    _file = open(filename)
    for line in _file:
        line = line[:-1]
        primary_list.append(list(map(int, line.split(" "))))
    return primary_list

def find_largest_product(n_list):
    _max = 0
    _width, _height = len(n_list[0]), len(n_list)

    for i in range(0, _height):
        for j in range(0, _width-3):
            tmp = n_list[i][j] * n_list[i][j+1] * \
                  n_list[i][j+2] * n_list[i][j+3]
            if tmp > _max:
                _max = tmp

    for i in range(0, _height-3):
        for j in range(0, _width):
            tmp = n_list[i][j] * n_list[i+1][j] * \
                  n_list[i+2][j] * n_list[i+3][j]
            if tmp > _max:
                _max = tmp

    for i in range(0, _height-3):
        for j in range(0, _width-3):
            tmp = n_list[i][j] * n_list[i+1][j+1] * \
                  n_list[i+2][j+2] * n_list[i+3][j+3]
            if tmp > _max:
                _max = tmp

            tmp = n_list[i][_width-1-j] * \
                  n_list[i+1][_width-2-j] * \
                  n_list[i+2][_width-3-j] * \
                  n_list[i+3][_width-4-j]
            if tmp > _max:
                _max = tmp
    return _max
        

if __name__ == "__main__":
    tStart = time.time()
    number_list = _read_file()
    print("Answer : {}".format(find_largest_product(number_list)))
    print("Done in {}s".format(time.time() - tStart))
