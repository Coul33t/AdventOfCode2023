import re

NUMBERS = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9')

TRANSLATION = {'one': '1',    '1': '1',
               'two': '2',    '2': '2',
               'three': '3',  '3': '3',
               'four': '4',   '4': '4',
               'five': '5',   '5': '5',
               'six': '6',    '6': '6',
               'seven': '7',  '7': '7',
               'eight': '8',  '8': '8',
               'nine': '9',   '9': '9'}

def read_input(path: str) -> list:
    with open(path, 'r') as input_file:
        contents = input_file.read().split('\n')
        return contents

def get_calibration_values(lines: list) -> list:
    calibration_values = []
    for val in lines:
        calib_val = [x for x in val if x.isdecimal()]
        if len(calib_val) == 1:
            calib_val.append(calib_val[0])

        calibration_values.append(int(calib_val[0] + calib_val[-1]))

    return calibration_values

def get_first_litteral(numbers_litteral: dict) -> int:
    smallest_idx_and_val = [9999999, -1]
    biggest_idx_and_val = [0, -1]

    for key, value in numbers_litteral.items():
        if not value:
            continue

        smallest = min(value)
        biggest = max(value)

        if smallest < smallest_idx_and_val[0]:
            smallest_idx_and_val[0] = smallest
            smallest_idx_and_val[1] = TRANSLATION[key]

        if biggest > biggest_idx_and_val[0]:
            biggest_idx_and_val[0] = biggest
            biggest_idx_and_val[1] = TRANSLATION[key]

    if biggest_idx_and_val[1] == -1:
        biggest_idx_and_val[1] = smallest_idx_and_val[1]

    return int(smallest_idx_and_val[1] + biggest_idx_and_val[1])


def get_calibration_values_part_two(lines: list) -> list:
    calibration_values = []

    for val in lines:
        numbers_litteral = {}
        for number in NUMBERS:
            numbers_litteral[number] = [m.start() for m in re.finditer(number, val)]
        
        calibration_values.append(get_first_litteral(numbers_litteral))
            
    return calibration_values

def sum_list(lst: list) -> int:
    return sum(lst)

def main():
    data = read_input('data.txt')
    values = get_calibration_values(data)
    print(f"Sum of calibration values: {sum_list(values)}")
    values_part_2 = get_calibration_values_part_two(data)
    print(f"Sum of calibration values part 2: {sum_list(values_part_2)}")

if __name__ == '__main__':
    main()