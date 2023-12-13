from dataclasses import dataclass
from enum import Enum

class Directions(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

POSSIBLE_DIR = {'|': [Directions.NORTH, Directions.SOUTH],
                '-': [Directions.WEST, Directions.EAST],
                'L': [Directions.NORTH, Directions.EAST],
                'J': [Directions.NORTH, Directions.WEST],
                '7': [Directions.SOUTH, Directions.WEST],
                'F': [Directions.SOUTH, Directions.EAST]}

@dataclass
class Point:
    x: int
    y: int

class PipeMap:
    def __init__(self, data):
        self.pipe_map = data
        self.starting_tile = None
        self.current_tile = None

    def find_starting_tile(self):
        for i, row in enumerate(self.pipe_map):
            for j, col in enumerate(row):
                if col == 'S':
                    self.starting_tile = Point(j, i)


    def get_next_tile(self, next_dir: Directions) -> Point:
        if next_dir == Directions.NORTH:
            return Point(self.starting_tile.x, self.starting_tile.y - 1)

        elif next_dir == Directions.EAST:
            return Point(self.starting_tile.x + 1, self.starting_tile.y)

        elif next_dir == Directions.SOUTH:
            return Point(self.starting_tile.x, self.starting_tile.y + 1)

        elif next_dir == Directions.WEST:
            return Point(self.starting_tile.x - 1, self.starting_tile.y)


    def find_first_direction(self) -> Directions:
        if self.starting_tile.y > 0:
            north_char = self.pipe_map[self.starting_tile.y - 1][self.starting_tile.x]

            if north_char in POSSIBLE_DIR.keys() and Directions.NORTH in POSSIBLE_DIR[north_char]:
                return Directions.NORTH

        elif self.starting_tile.x < len(self.pipe_map[0]) - 1:

            east_char = self.pipe_map[self.starting_tile.y][self.starting_tile.x + 1]

            if east_char in POSSIBLE_DIR.keys() and Directions.EAST in POSSIBLE_DIR[east_char]:
                return Directions.EAST

        elif self.starting_tile.y < len(self.pipe_map) - 1:

            south_char = self.pipe_map[self.starting_tile.y + 1][self.starting_tile.x]

            if south_char in POSSIBLE_DIR.keys() and Directions.SOUTH in POSSIBLE_DIR[south_char]:
                return Directions.SOUTH

        elif self.starting_tile.x > 0:

            west_char = self.pipe_map[self.starting_tile.y][self.starting_tile.x - 1]

            if west_char in POSSIBLE_DIR.keys() and Directions.WEST in POSSIBLE_DIR[west_char]:
                return Directions.WEST

        else:
            print("Well, that's unexpected.")
                

    def find_nb_step_for_furthest(self) -> int:
        steps = 0
        distance = 0
        current_chr = 'S'

        next_dir = self.find_first_directions()
        self.current_tile = self.starting_tile

        # do : run through the pipe maze







def read_input(path: str) -> list:
    with open(path, 'r') as input_file:
        contents = input_file.read().split('\n')
        return contents


def main():
    data = read_input('data.txt')


if __name__ == '__main__':
    main()