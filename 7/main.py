from dataclasses import dataclass


CARDS_ORDER = ('A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2')
ALL_HANDS = ('High Card', 'One pair', 'Two pairs', 'Three of a kind', 'Full house', 'Four of a kind', 'Five of a kind')

@dataclass
class Hand:
    cards: list
    bid: int
    type: str = 'None'
    rank: int = 0

    def get_type(self):
        # All distinct
        if len(set(self.cards)) == len(self.cards):
            self.type = 'High card'

        # All the same
        elif len(set(self.cards)) == 1:
            self.type = 'Five of a kind'

        # Only 2 different cards: could be 4 of a kind or full house
        elif len(set(self.cards)) == 2:
            # if there's 4 of the first card OR 1 card alone (meaning that the rest are the 4 same cards), it's a four of a kind
            # (works because of the set length == 2 before)
            if self.cards.count(self.cards[0]) == 1 or self.cards.count(self.cards[0]) == 4:
                self.type = 'Four of a kind'

            # Else it's a full house
            else:
                self.type = 'Full house'


        # 3 different cards & 2 of the same card
        elif len(set(self.cards)) == len(self.cards) - 1:
            self.type = 'One pair'

        # Differenciate between Three of a kind and Two pair
        else:
            for card in self.cards:
                if self.cards.count(card) == 3:
                    self.type = 'Three of a kind'
                    break
            
            # For-Else: goes into the "else" if the loop ended without a break 
            else:
                self.type = 'Two pairs'




def split_data_into_hands(data: list) -> list:
    hands = []

    for single_data in data:
        splitted = single_data.split(' ')
        hands.append(Hand([x for x in splitted[0]], int(splitted[1])))
        hands[-1].get_type()

    return hands

def smallest_recursive(hands_lst: list, card_idx: int, rank_value: int) -> None:
    if len(hands_lst) > 1:
        find_smallest(hands_lst, card_idx + 1, rank_value)
        hands_lst[-1].rank = rank_value
        rank_value += 1

    else:
        hands_lst[0].rank = rank_value
        rank_value += 1
        return

def find_smallest(hands: list, card_idx: int, rank_value: int) -> None:
    smallest_order = CARDS_ORDER[::-1]

    for current_card in smallest_order:
        hands_lst = [x for x in hands if x.cards[card_idx] == current_card]

        if hands_lst:
            smallest_recursive(hands_lst, card_idx, rank_value)
        
        

def pre_rank(hands: list) -> None:
    current_rank = 1
    for _, combination in enumerate(ALL_HANDS):
        has_at_least_one = False
        for hand in hands:
            if hand.type == combination:
                hand.rank = current_rank
                has_at_least_one = True

        if has_at_least_one:
            current_rank += 1


def rank_hands(hands: list) -> None:
    pre_rank(hands)

    


def read_input(path: str) -> list:
    with open(path, 'r') as input_file:
        contents = input_file.read().split('\n')
        return contents


def main():
    data = read_input('data_test.txt')
    hands = split_data_into_hands(data)
    rank_hands(hands)
    breakpoint()


if __name__ == '__main__':
    main()