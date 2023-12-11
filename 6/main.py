from dataclasses import dataclass

DEBUG = False
@dataclass
class Race:
    time: int
    distance: int

    def get_number_of_winning_distances(self):
        nb_of_win = 0
        for i in range(self.time):
            if DEBUG:
                print(f"Holding button for {i}ms, leaving {self.time - i}ms to run = {i * (self.time - i)}")

            if i * (self.time - i) > self.distance:
                nb_of_win += 1

        return nb_of_win


def read_input(path: str) -> list:
    with open(path, 'r') as input_file:
        contents = input_file.read().split('\n')
        return contents

def reformat_data(data: list) -> list:
    races = []
    idx = 0

    times = [int(x) for x in data[0].split(':')[-1].split(' ') if x]
    distances = [int(x) for x in data[1].split(':')[-1].split(' ') if x]

    for i, _ in enumerate(times):
        races.append(Race(times[i], distances[i]))
    
    return races

def get_product_of_winning_distances(races: list) -> int:
    final_product = 1
    for race in races:
        final_product *= race.get_number_of_winning_distances()

    return final_product

def reformat_single_data(data: list) -> Race:
    time = int(''.join([x for x in data[0].split(':')[-1].split(' ') if x]))
    distance = int(''.join([x for x in data[1].split(':')[-1].split(' ') if x]))
    return Race(time, distance)

def main():
    data = read_input('data.txt')
    races = reformat_data(data)
    print(f"Product of winning distances: {get_product_of_winning_distances(races)}")
    race = reformat_single_data(data)
    print(f"Number of winning distances: {race.get_number_of_winning_distances()}")



if __name__ == '__main__':
    main()