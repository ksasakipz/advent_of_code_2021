import sys
import os

def parse_line(line):
    temp1 = line.strip().split(" -> ")
    temp2 = []
    for i in temp1:
        temp2 += i.split(",")
    retval = []
    for j in temp2:
        retval += [int(j)]
    return retval

def main():
    fname = "input.txt"
    x_max = 0
    x_min = 9999
    y_max = 0
    y_min = 9999
    in_file = open(fname, 'r')
    horizontal_lines = []
    vertical_lines = []
    diagonal_up_lines = []
    diagonal_down_lines = []
    retval = 0

    line_count = 0
    while True:
        line = in_file.readline()
        if not line:
            break
        line_count += 1
        coords = parse_line(line)
        x1 = coords[0]
        y1 = coords[1]
        x2 = coords[2]
        y2 = coords[3]
        # Update mins and maxes
        if x1 < x_min:
            x_min = x1
        if x2 < x_min:
            x_min = x2
        if x1 < x_min:
            x_min = x1

        if y1 < y_min:
            y_min = y1
        if y2 < x_min:
            y_min = y2
        if y1 < x_min:
            y_min = y1

        if x1 > x_max:
            x_max = x1
        if x2 > x_max:
            x_max = x2
        if x1 > x_max:
            x_max = x1

        if y1 > y_max:
            y_max = y1
        if y2 > y_max:
            y_max = y2
        if y1 > y_max:
            y_max = y1
        # Determine whether or not we are considering them
        if x1 == x2:
            vertical_lines += [(x1, y1, x2, y2)]
        elif y1 == y2:
            horizontal_lines += [(x1, y1, x2, y2)]
        elif x1 - x2 == y1 - y2:
            diagonal_up_lines += [(x1, y1, x2, y2)]
        elif x2 - x1 == y1 - y2:
            diagonal_down_lines += [(x1, y1, x2, y2)]
        else:
            pass

    grid = [[0 for x in range(x_max + 1)] for y in range(y_max + 1)]
    out_file = open("out0", "w")
    for i in grid:
        out_file.write(str(i) + "\n")
    out_file.close()
    print("x_min: {} | x_max: {} | y_min: {} | y_max: {}".format(x_min, x_max, y_min, y_max))
    for l in horizontal_lines:
        constant = l[1]
        lower_col= min(l[0], l[2])
        upper_col = max(l[0], l[2])

        column = lower_col
        while True:
            if column != upper_col + 1:
                grid[constant][column] += 1
                if grid[constant][column] == 2:
                    retval += 1
                column += 1
            else:
                break
    out_file = open("out1", "w")
    for i in grid:
        out_file.write(str(i) + "\n")
    out_file.close()
    for l in vertical_lines:
        constant = l[0]
        lower_row = min(l[1], l[3])
        upper_row = max(l[1], l[3])
        row = lower_row
        while True:
            if row != upper_row + 1:
                grid[row][constant] += 1
                if grid[row][constant] == 2:
                    retval += 1
                row += 1
            else:
                break
    out_file = open("out2", "w")
    for i in grid:
        out_file.write(str(i) + "\n")
    out_file.close()
    for l in diagonal_up_lines:
        lower_row = min(l[1], l[3])
        upper_row = max(l[1], l[3])
        lower_col= min(l[0], l[2])
        upper_col = max(l[0], l[2])

        row = lower_row
        col = lower_col
        while True:
            if row != upper_row + 1 and col != upper_col + 1:
                grid[row][col] += 1
                if grid[row][col] == 2:
                    retval += 1
                row += 1
                col += 1
            else:
                break
    for l in diagonal_down_lines:
        lower_row = min(l[1], l[3])
        upper_row = max(l[1], l[3])
        lower_col= min(l[0], l[2])
        upper_col = max(l[0], l[2])

        row = lower_row
        col = upper_col
        while True:
            if row != upper_row + 1 and col != lower_col - 1:
                grid[row][col] += 1
                if grid[row][col] == 2:
                    retval += 1
                row += 1
                col -= 1
            else:
                break

    retval2 = 0
    for i in grid:
        for j in i:
            if j > 1:
                retval2 += 1

    out_file = open("out3", "w")
    for i in grid:
        out_file.write(str(i) + "\n")
    out_file.close()

    print("retval2: {}".format(retval2))
    print("line_count: {}".format(line_count))

    return retval

if __name__ == "__main__":
    retval = main()
    print("retval: {}".format(retval))
    
    
