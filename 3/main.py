from curses.ascii import isdigit
import numpy as np

COLOURS = ('red', 'green', 'blue')

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def read_input(path: str) -> list:
    with open(path, 'r') as input_file:
        contents = input_file.read().split('\n')
        return contents

def search_for_symbol(data: list, begin_x: int, end_x: int, y: int) -> bool:
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
        
def search_for_gear(data: list, begin_x: int, end_x: int, row_y: int) -> list:
    search_x_begin = begin_x - 1 if begin_x > 0 else begin_x
    search_x_end = end_x + 1 if end_x < len(data[0]) - 1 else end_x

    search_y_begin = row_y - 1 if row_y > 0 else row_y
    search_y_end = row_y + 1 if row_y < len(data) - 1 else row_y

    for x in range(search_x_begin, search_x_end):
        for y in range(search_y_begin, search_y_end + 1):
            if data[y][x] == "*":
                return Point(x, y)

    return Point(-1, -1)

def check_if_has_been_done(current_pair, already_done_pairs) -> bool:
    for pair in already_done_pairs:
        if (current_pair[0] == pair[1] and current_pair[1] == pair[0]) or (current_pair[0] == pair[0] and current_pair[1] == pair[1]):
            return True
    
    return False

def check_second_number(data, begin_x_first_number, end_x_first_number, y_row, gear_coords, already_done_pairs: list):
    gear_val = -1
    
    # First, check around gear to find a number (except the last one)
    nonvalid_coords = [x for x in range(begin_x_first_number, end_x_first_number)]
    new_pair = [-1, -1]

    new_pair[0] = int(''.join(data[y_row][begin_x_first_number:end_x_first_number]))
    
    x_beg = gear_coords.x - 1 if gear_coords.x > 0 else 0
    x_end = gear_coords.x + 1 if gear_coords.x < len(data[0]) - 1 else gear_coords.x

    y_beg = gear_coords.y - 1 if gear_coords.y > 0 else 0
    y_end = gear_coords.y + 1 if gear_coords.y < len(data) - 1 else gear_coords.y

    for x in range(x_beg, x_end + 1):
        for y in range(y_beg, y_end + 1):
            if y == y_row:
                if x in nonvalid_coords:
                    continue
            
            if y != y_row and isdigit(data[y][x]):
                #go left and right to find all digits
                other_number = []
                changing_x = x
                
                while(isdigit(data[y][changing_x])):
                    other_number.insert(0, data[y][changing_x])
                    changing_x -= 1
                    if changing_x == -1:
                        break

                changing_x = x + 1
                while(isdigit(data[y][changing_x])):
                    other_number.append(data[y][changing_x])
                    changing_x += 1
                    if changing_x == len(data[y]):
                        break

                other_number_as_int = int(''.join(other_number))
                new_pair[1] = other_number_as_int

                if not check_if_has_been_done(new_pair, already_done_pairs):
                    gear_val = new_pair[0] * new_pair[1]
                    already_done_pairs.append(new_pair)
                    print(f"New pair: {new_pair}")

                else:
                    print(f"Pair {new_pair} has already been done")
                
    
    return gear_val

def get_gears(data: list) -> list:
    is_digit = False
    begin_x = -1
    valid_numbers = []
    already_done_set = []
    sum_of_gears = 0

    for y, row in enumerate(data):
        begin_x = -1
        for x, char in enumerate(row):
            if isdigit(char):
                if not is_digit:
                    begin_x = x
                is_digit = True

            elif not isdigit(char) and is_digit:
                is_digit = False
                gear_coords = search_for_gear(data, begin_x, x, y)
                if gear_coords.x != -1 and gear_coords.y != -1:
                    print(f"{row[begin_x:x]} has gear")
                    gear_val = check_second_number(data, begin_x, x, y, gear_coords, already_done_set)
                    if gear_val != -1:
                        sum_of_gears += gear_val
                    
                
    return sum_of_gears


def sum_of_list(lst: list) -> int:
    return sum(lst)

def main():
    data = read_input('data.txt')
    #lst_of_numbers = get_list_of_valid_numbers(data)
    #print(f"Sum of valid numbers: {sum_of_list(lst_of_numbers)}")

    print(f"Sum of gears: {get_gears(data)}")

if __name__ == '__main__':
    main()