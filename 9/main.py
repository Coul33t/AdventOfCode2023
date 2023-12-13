def read_input(path: str) -> list:
    with open(path, 'r') as input_file:
        contents = input_file.read().split('\n')
        return contents

def format_data(data: list) -> list:
    f_data = []
    for d in data:
        f_data.append([int(x) for x in d.split(' ')])

    return f_data

def compute_diff(lst: list) -> list:
    return [lst[i] - lst[i-1] for i in range(1, len(lst))]


def extrapolate(lst: list) -> int:
    all_lst = [lst]
    all_lst.append(compute_diff(lst))
    last_vals = [all_lst[-1][-1]]

    while any(all_lst[-1]):
        all_lst.append(compute_diff(all_lst[-1]))
        last_vals.append(all_lst[-1][-1])

    all_lst.reverse()
    last_vals.reverse()

    for i, val in enumerate(last_vals):
        all_lst[i + 1].append(all_lst[i][-1] + all_lst[i + 1][-1])
    
    return all_lst[-1][-1]

def extrapolate_first(lst: list) -> int:
    lst.reverse()
    
    all_lst = [lst]
    all_lst.append(compute_diff(lst))
    last_vals = [all_lst[-1][-1]]

    while any(all_lst[-1]):
        all_lst.append(compute_diff(all_lst[-1]))
        last_vals.append(all_lst[-1][-1])

    all_lst.reverse()
    last_vals.reverse()

    for i, val in enumerate(last_vals):
        all_lst[i + 1].append(all_lst[i][-1] + all_lst[i + 1][-1])
    
    return all_lst[-1][-1]

    
def sum_of_extrapolations(data: list) -> int:
    return sum([extrapolate(x) for x in data])
    
def sum_of_extrapolations_first(data: list) -> int:
    return sum([extrapolate_first(x) for x in data])

def main():
    data = read_input('data.txt')
    data = format_data(data)
    print(f'Sum of extrapolated values: {sum_of_extrapolations(data)}')
    print(f'Sum of extrapolated first values: {sum_of_extrapolations_first(data)}')


if __name__ == '__main__':
    main()