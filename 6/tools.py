import sys
import os

def load_data(fname):
    in_file = open(fname, 'r')
    line = in_file.readline()
    temp = line.strip().split(',')
    for i in range(len(temp)):
        temp[i] = int(temp[i])

    retval = {}
    for i in range(8, -1, -1):
        retval[i] = 0
    for i in temp:
        try:
            retval[i] += 1
        except:
            retval[i] = 1

    return retval

def increment_day(state):
    retval = {}
    for i in range(8, -1, -1):
        retval[i] = 0
    for i in range(8, -1, -1):
        try:
            temp = state[i]
            if i == 0:
                retval[6] += temp
                retval[8] += temp
            else:
                retval[i-1] += temp
        except:
            retval[i] = 0
    return retval

def main(fname):
    data = load_data(fname)

    for i in range(256):
        data = increment_day(data)
        #input("continue?")
        temp = 0
        for key in data:
            temp += data[key]

    retval = 0

    for key in data:
        retval += data[key]

    print(f'data: {data}')
    print(f'retval: {retval}')

    return retval

if __name__ == "__main__":
    retval = main()
    print("retval: {}".format(retval))

    
    
