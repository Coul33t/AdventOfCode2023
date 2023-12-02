import numpy as np

COLOURS = ('red', 'green', 'blue')

def read_input(path: str) -> list:
    with open(path, 'r') as input_file:
        contents = input_file.read().split('\n')
        return contents

def split_string_to_dict(input_str: str) -> dict:
    number_of_balls = {'red': 0, 'green': 0, 'blue': 0}
    for single_colour in input_str:
        splitted = [x for x in single_colour.split(' ') if x]
        number_of_balls[splitted[-1]] = int(splitted[0])

    return number_of_balls

def sum_of_possible_games(data: list, repartition: dict) -> int:
    sum_of_ok_games = 0

    for game in data:
        game_idx = int(game.split(':')[0].split(' ')[1])
        number_of_balls = {'red': 0, 'green': 0, 'blue': 0}
        balls = [x.split(',') for x in game.split(':')[-1].split(';')]
        
        is_ok = True
        
        # each draw in a game
        for drawn in balls:
            if not is_ok:
                break

            is_ok = True

            number_of_balls = split_string_to_dict(drawn)

            for key, value in number_of_balls.items():
                if value > repartition[key]:
                    is_ok = False
                    break

        if is_ok:
            sum_of_ok_games += game_idx

        

    return sum_of_ok_games

def min_number_of_cube(game: list) -> dict:
    min_number = {'red': 0, 'green': 0, 'blue': 0}

    for drawn in game:
        number_of_balls = split_string_to_dict(drawn)

        for key, value in number_of_balls.items():
            if min_number[key] < value:
                min_number[key] = value

    return min_number

def power_of_min_sets(data: list) -> int:
    sum_of_powers = 0

    for game in data:
        balls = [x.split(',') for x in game.split(':')[-1].split(';')]
        min_number = min_number_of_cube(balls)
        sum_of_powers += np.prod([x for _, x in min_number.items()])

    return sum_of_powers

def main():
    data = read_input('data.txt')
    first_repartition = {'red': 12, 'green': 13, 'blue': 14}
    print(f"Sum of possible games: {sum_of_possible_games(data, first_repartition)}")
    print(f"Sum of power of min sets: {power_of_min_sets(data)}")

if __name__ == '__main__':
    main()