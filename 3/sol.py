import re              

class Solution:
    def __init__(self):
        self.data = self.get_data()

    def get_data(self): 
        with open('data.txt', 'r') as input_file:
            contents = input_file.read().split('\n')
            return contents

    def check_string(self, string):
        return list(zip(re.findall(r'(?!\.)\W', string), [x.start(0) for x in re.finditer(r'(?!\.)\W', string)]))

    def check_for_symbols(self, line, starting_line, ending_line, start, end):
            symbols_above = self.check_string(self.data[starting_line][start:end])
            symbols_inline = self.check_string(line[start:end])
            symbols_below = self.check_string(self.data[ending_line][start:end])

            return symbols_above, symbols_inline, symbols_below

    def get_numbers(self, row):
        return list(zip(re.findall(r'(\d+)', row), [x.start(0) for x in re.finditer(r'(\d+)', row)]))

    def solve(self):
        matches = []
        mapping = {}
        gear_ratios = []

        for line_idx, line in enumerate(self.data):
            numbers = self.get_numbers(line)
            for number, idx in numbers:
                starting_line = line_idx-1 if line_idx > 0 else 0
                ending_line = line_idx+1 if line_idx+1 < len(self.data) else -1
                start = idx-1 if idx > 0 else 0
                end = len(number)+idx+1 if idx+1 < len(line) else -1

                above, inline, below = self.check_for_symbols(line, starting_line, ending_line, start, end)

                if any([above, inline, below]):
                    matches.append(int(number))

                for row_idx, found in [(starting_line, above),(line_idx, inline), (ending_line, below)]:
                    for match in found:
                        if match[0] == '*':
                            name = str(row_idx)+'_'+str(match[1]+start)
                            n = f'{line_idx}_{idx}_{number}'

                            if name in mapping:
                                mapping[name].add(n)
                            else:
                                mapping[name] = set({n})

        for value in mapping.values():
            if len(value) == 2:
                ratio_1, ratio_2 = value
                ratio_1 = int(ratio_1.split('_')[-1])
                ratio_2 = int(ratio_2.split('_')[-1])
                gear_ratios.append(ratio_1*ratio_2)

        print(f'Part One: {sum(matches)}')
        print(f'Part Two: {sum(gear_ratios)}')


if __name__ == '__main__':
    solution = Solution()
    solution.solve()