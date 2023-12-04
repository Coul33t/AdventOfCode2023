from curses.ascii import isdigit
import numpy as np

COLOURS = ('red', 'green', 'blue')

def read_input(path: str) -> list:
    with open(path, 'r') as input_file:
        contents = input_file.read().split('\n')
        return contents

def search_for_symbol(data: list, begin_x: int, end_x: int, y: int):
    search_x_begin = begin_x - 1 if begin_x > 0 else begin_x
    search_x_end = end_x + 1 if end_x < len(data[0]) - 1 else end_x

    search_y_begin = y - 1 if y > 0 else y
    search_y_end = y + 1 if y < len(data) - 1 else y

    for x in range(search_x_begin, search_x_end):
        for y in range(search_y_begin, search_y_end + 1):
            if data[y][x] != '.' and not isdigit(data[y][x]):
                return True

    return False


def get_list_of_valid_numbers(data: list) -> list:

    is_digit = False
    begin_x = -1
    valid_numbers = []

    for y, row in enumerate(data):
        begin_x = -1
        for x, char in enumerate(row):
            if isdigit(char):
                if not is_digit:
                    begin_x = x
                is_digit = True

            elif not isdigit(char) and is_digit:
                is_digit = False
                if search_for_symbol(data, begin_x, x, y):
                    print(f"{row[begin_x:x]} has symbol")
                    valid_numbers.append(int(row[begin_x:x]))

                else:
                    print(f"{row[begin_x:x]} has no symbol")

            # Edge case when a number is at the end of a line
            if is_digit and x == len(row) - 1:
                if search_for_symbol(data, begin_x, x + 1, y):
                    print(f"{row[begin_x:x+1]} has symbol")
                    valid_numbers.append(int(row[begin_x:x+1]))

                else:
                    print(f"{row[begin_x:x+1]} has no symbol")

    return valid_numbers
        


def sum_of_list(lst: list) -> int:
    return sum(lst)

def main():
    data = read_input('data.txt')
    lst_of_numbers = get_list_of_valid_numbers(data)
    print(f"Sum of valid numbers: {sum_of_list(lst_of_numbers)}")

if __name__ == '__main__':
    main()