from dataclasses import dataclass


class SingleMap:
    def __init__(self, lst):
        self.dest_r_start = lst[0]
        self.src_r_start = lst[1]
        self.range_length = lst[2]

class InputMapping:
    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.sorted_data = {}
        self.process_raw_data()

    def process_raw_data(self):
        current_key = ''

        for line in self.raw_data:
            
            if 'seeds' in line:
                self.sorted_data['seeds'] = [int(x) for x in line.split(':')[1].split(' ') if x]
            
            else:
                if not line:
                    continue

                if not line[0].isdigit():
                    current_key = line.split(':')[0].split(' ')[0]
                    self.sorted_data[current_key] = []

                else:
                    self.sorted_data[current_key].append(SingleMap([int(x) for x in line.split(' ') if x]))


def read_input(path: str) -> list:
    with open(path, 'r') as input_file:
        contents = input_file.read().split('\n')
        return contents


def main():
    data = read_input('data_test.txt')
    input_mapping = InputMapping(data)
    breakpoint()



if __name__ == '__main__':
    main()