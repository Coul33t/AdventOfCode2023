from dataclasses import dataclass


@dataclass
class Instructions:
    instrs: list

class Node:
    def __init__(self, name: str):
        self.name = name
        self.left = None
        self.right: None

    def __repr__(self) -> str:
        return f'{self.name}: ({self.left}, {self.right})'

    def __str__(self) -> str:
        return f'{self.name}: ({self.left}, {self.right})'


class BinaryTree:
    def __init__(self):
        self.nodes = []
        self.instructions = None
        self.starting_node = 'A'
        self.target_node = 'Z'

    def construct_tree(self, data):
        for node in data:
            if not node:
                continue

            else:
                splitted = node.split('=')
                node = Node(splitted[0].strip())
                targets = [''.join([i for i in x if i.isalpha()]) for x in splitted[1].split(',')]
                node.left = targets[0]
                node.right = targets[1]
                self.nodes.append(node)

    def load_instructions(self, data: str) -> None:
        self.instructions = Instructions([x for x in data])
    
    def find_node(self, name: str) -> Node:
        for node in self.nodes:
            if node.name == name:
                return node

    def find_nodes_ending_with(self, char: str) -> list:
        lst = []
        for node in self.nodes:
            if node.name[-1] == char:
                lst.append(node)

        return lst


    def run_tree(self) -> int:
        steps = 0
        current_nodes = self.find_nodes_ending_with(self.starting_node)
        print(f'Simultaneous nodes: {len(current_nodes)}')
        idx = 0

        while True:
            if self.instructions.instrs[idx] == 'L':
                current_nodes = [self.find_node(n.left) for n in current_nodes]
            else:
                current_nodes = [self.find_node(n.right) for n in current_nodes]

            steps += 1

            if all([n.name[-1] == self.target_node for n in current_nodes]):
                break

            idx += 1

            if idx == len(self.instructions.instrs):
                idx = 0

            print(f"{steps}", end='\r')

            


        return steps


def read_input(path: str) -> list:
    with open(path, 'r') as input_file:
        contents = input_file.read().split('\n')
        return contents


def main():
    data = read_input('data.txt')
    tree = BinaryTree()
    tree.construct_tree(data[1:])
    tree.load_instructions(data[0])
    print(f'Number of steps to reach {tree.target_node}: {tree.run_tree()}')


if __name__ == '__main__':
    main()