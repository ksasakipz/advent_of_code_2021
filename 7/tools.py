import sys
import os
import tools

def parse_line(line):
    temp1 = line.strip().split(" -> ")
    temp2 = []
    for i in temp1:
        temp2 += i.split(",")
    retval = []
    for j in temp2:
        retval += [int(j)]
    return retval

def load_data(fname):
    in_file = open(fname, 'r')
    line = in_file.readline()
    retval = line.strip().split(',')
    for i in range(len(retval)):
        retval[i] = int(retval[i])

    return retval

def main():
    fname = "input.txt"
    data = load_data(fname)
    retval = sum(data)
    dest = 0

    for destination in range(max(data)+ 1):
        current = 0
        for i in data:
            print(f'destination: {destination} | i: {i} | current: {current} | abs(i-destination): {abs(i-destination)}')
            current += abs(i - destination)

        print()
        print(f'retval: {retval} | current: {current} | dest: {dest} | destination: { destination}')
        print()
        if current < retval:
            retval = current
            dest = destination + 1
    print(f'retval: {retval} | dest: {dest}')
    print(f'data: {data}')

    return retval

if __name__ == "__main__":
    retval = main()
    print("retval: {}".format(retval))
    
    
