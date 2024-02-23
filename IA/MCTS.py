from Node import Node
import math
import numpy as np

class MCTS(object):

    def __init__(self, initial_board):
        self._initial_node = Node(initial_board)

    @property
    def initial_node(self):
        return self._initial_node
    
    @initial_node.setter
    def initial_node(self, node):
        self._initial_node = node

    def ucb(self, node):
        if node.visited == 0:
            return float('inf')
        return node.score / node.visits + math.sqrt(2 * math.log(node.parents.visited) / node.visited)
 
    def selection(self, node):
        if not node.children:
            return node
        
        ucb_values = [self.ucb(child) for child in node.children]
        return node.children[np.argmax(ucb_values)]

    def expansion(self, node):
        possible_moves = node.get_possible_moves()

    def simulation(self, node, isGameOver):
        while not isGameOver:
            possible_moves = node.get_possible_moves()
            move = np.random.choice(possible_moves)
            node.apply_move(move)
        return node.score, move

    def backpropagation(self, node, score):
        while node is not None:
            node.visited += 1
            node.score += score
            node = node.parent

    def mcts_search(self, iterations, isGameOver=False):
        for _ in range(iterations):
            node = self._initial_node
            while node.children:
                node = self.selection(node)
            self.expansion(node)
            score = self.simulation(node, isGameOver)[0]
            self.backpropagation(node, score)
        best_child = max(self._initial_node, key=lambda x: x.visited)
        return best_child