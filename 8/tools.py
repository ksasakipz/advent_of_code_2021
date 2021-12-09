import sys
import os
import tools

def parse_line(line):
    temp1 = line.strip().split("|")
    assert len(temp1) == 2
    first_half = temp1[0].strip().split(" ")
    second_half= temp1[1].strip().split(" ")

    retval = first_half + second_half
    retval = decode(retval)
    return retval

def decode(numbers):
    finished = False
    fivers = False
    sixers = False
    d = {}
    for i in range(10):
        d[i] = 0
    for i in range(len(numbers)):
        if len(numbers[i]) == 2:
            d[1] = ''.join(sorted(numbers[i]))
        elif len(numbers[i]) == 3:
            d[7] = ''.join(sorted(numbers[i]))
        elif len(numbers[i]) == 4:
            d[4] = ''.join(sorted(numbers[i]))
        elif len(numbers[i]) == 7:
            d[8] = ''.join(sorted(numbers[i]))
        elif len(numbers[i]) == 5:
            fivers = True
        elif len(numbers[i]) == 6:
            sixers = True
        else:
            raise Exception("ack")
    
    if sixers:
        pass
    if fivers:
        pass
    
    while not finished:
        break
        pass
        
    retval = 0
    return numbers

def load_data(fname):
    in_file = open(fname, 'r')
    retval = 0

    while True:
        line = in_file.readline()
        if not line:
            break
        x = parse_line(line)

        for i in x[10:]:
            if len(i) == 2 or len(i) == 4 or len(i) == 3 or len(i) == 7:
                retval += 1

    return retval

def main():
    fname = "test_input.txt"
    retval = load_data(fname)

    print(f'retval: {retval}')

    return retval

if __name__ == "__main__":
    retval = main()
    print("retval: {}".format(retval))

    
    
