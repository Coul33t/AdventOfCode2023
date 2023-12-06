from dataclasses import dataclass
import itertools

class Card:
    def __init__(self, data):
        self.data = data
        self.name = ''
        self.winning_numbers = []
        self.choosen_numbers = []
        self.init_data()

    def init_data(self):
        splitted_data = self.data.split(':')
        self.name = splitted_data[0]
        splitted_data = splitted_data[1].split('|')
        self.winning_numbers = [int(x) for x in splitted_data[0].split(' ') if x]
        self.choosen_numbers = [int(x) for x in splitted_data[1].split(' ') if x]
        
    def get_nb_of_same_numbers(self) -> int:
        return len(self.winning_numbers) + len(self.choosen_numbers) - len(set(itertools.chain(self.winning_numbers, self.choosen_numbers)))
    
    def compute_score(self) -> int:
        res = 2 ** (self.get_nb_of_same_numbers() - 1)
        return res if res >= 1 else 0 

@dataclass
class CardAndNumber:
    card: Card
    nb: int

class Stack:
    def __init__(self):
        self.cards = []

    def put_all_cards(self, data) -> None:
        for card_data in data:
            self.cards.append(CardAndNumber(Card(card_data), 1))

    def add_card(self, card: Card) -> None:
        self.cards.append(CardAndNumber(card, 1))

    def reset(self) -> None:
        for card_and_number in self.cards:
            card_and_number.nb = 1

    def process(self) -> None:
        current_idx = 0
        for i, card_and_number in enumerate(self.cards):
            current_idx += 1
            nb_cards_earned = card_and_number.card.get_nb_of_same_numbers()

            for j in range(card_and_number.nb):
                for k in range(current_idx, current_idx + nb_cards_earned):
                    self.cards[k].nb += 1

    def count(self) -> int:
        return sum([x.nb for x in self.cards])

    def process_and_count(self) -> int:
        self.reset()
        self.process()
        return self.count()


def read_input(path: str) -> list:
    with open(path, 'r') as input_file:
        contents = input_file.read().split('\n')
        return contents

def count_points(data: list) -> int:
    points = 0
    for card_data in data:
        new_card = Card(card_data)
        points += new_card.compute_score()

    return points

def count_number_of_cards(data: list) -> int:
    card_stack = Stack()
    card_stack.put_all_cards(data)
    return card_stack.process_and_count()

def main():
    data = read_input('data.txt')
    print(f"Number of points: {count_points(data)}")
    print(f"Number of cards counted: {count_number_of_cards(data)}")



if __name__ == '__main__':
    main()