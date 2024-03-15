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
        if node is not None:
            if node.visited == 0:
                return float('inf')
            return node.score / node.visited + math.sqrt(2 * math.log(node.parent.visited) / node.visited)
        else:
            raise ValueError
 
    def selection(self, node):
        if node is not None:
            if not node.children:
                return node
            
            ucb_values = [self.ucb(child) for child in node.children]
            return node.children[np.argmax(ucb_values)]
        else:
            raise ValueError

    def expansion(self, node):
        if node is not None:
            return node.get_possible_moves()
        else:
            raise ValueError

    def simulation(self, node, isGameOver):
        #print("node in simulation beginning : ", node.board)
        #print("\n")
        while not isGameOver:
            score = node.score
            possible_moves = ["UP", "DOWN", "LEFT", "RIGHT"]
            if node.children is None:
                self.expansion(node)
            #for child in node.children:
                #print("possible move : ", child.board)
                #print("\n")

            move = np.random.choice(possible_moves)
            print("random move : ", move)
            node = node.apply_move(move)
            print("apply_move node : ", node)
            node.score += score
            #print("node after apply_move in simulation : ", node.board)
            #print("\n")

            isGameOver = True
            if node is not None:
                for child in node.children:
                    for i in range(4):
                        for j in range(4):
                            if child.board[i][j] != node.board[i][j]:
                                isGameOver = False
            else:
                raise ValueError
        print("score after simulation : ", node.score)
        return node.score

    def backpropagation(self, node, score):
        while node is not None:
            node.visited += 1
            node.score += score
            node = node.parent

    def mcts_search(self, iterations, isGameOver=False):
        for _ in range(iterations):
            if isGameOver:
                return None
            node = self._initial_node
            node.get_possible_moves()

            #for child in node.children:
                #print(child.board)

            while node.children:
                node = self.selection(node)
                #print("selection called, node chosen : ", node.board)

            self.expansion(node)
            #print("expansion called, children are :")
            #for child in node.children:
                #print(child.board)

            score = self.simulation(node, isGameOver)
            #print("simulation score :", score)

            self.backpropagation(node, score)
            #print("backpropagation called :", score)

        best_child = max(self._initial_node.children, key=lambda x: x.visited)
        print("best child :", best_child.board)
        return best_child.board, best_child.score