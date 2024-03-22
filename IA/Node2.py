
import uuid
import math
class Node:
    def __init__(self, state, parent=None, parent_action=None):
        self.id = uuid.uuid4()
        self.state = state # état du jeu associé à un noeud
        self.parent = parent # noeud parent dans l'arbre 
        self.parent_action = parent_action # action qui a été fait par le parent pour arriver au noeud actuel
        self.children = [] # noeud enfants 
        self.visits = 0 # nb de fois que le noeud a été visité 
        self.total_score = 0 # score accumulé lors de la simulation à partir de ce noeud
        self._possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT'] # actions possibles du noeud

    '''
    ############## GETTERS ###############
    '''

    def get_id(self):
        return self.id
        
    def get_state(self):
        return self.state

    def get_parent(self):
        return self.parent

    def get_action(self):
        return self.parent_action

    def add_child(self, child):
        self.children.append(child)

    def get_children(self):
        return self.children

    def get_possible_actions(self):
        return self._possible_actions

    @property
    def possible_actions(self):
        return self._possible_actions

    '''
    ############## SETTERS ###############
    '''

    # @possible_actions.setter
    # def_possible_actions(self, actions):
    #     self._possible_actions = actions
    
    # remove une action possible
    def remove_actions(self, action):
        if action in self._possible_actions:
            self._possible_actions.remove(action)


    '''
    ######################################
    '''
    # Retourne True si le noeud est feuille => game over 
    def is_terminal(self):
        return self.state.is_game_over()

    # Vérifie qu'il y a un enfant pour chaque action possible
    def is_fully_expanded(self):
        print("is_fully_expanded : " + str(len(self.children)) + "  ===  " + str(len(self.get_possible_actions())))
        return len(self.children) == len(self.get_possible_actions())

    
    # renvoie les actions qui n'ont pas été explorées 
    def get_unexplored_actions(self):
        print("UNEXPLORED ACTIONS : ", self._possible_actions)
        return self._possible_actions
        # # récupère les actions possibles 
        # possible_actions = self.get_possible_actions()

        # # pour chaque enfant, récupère chaque action
        # explored_actions = [child.get_action() for child in self.children]
        # print("ACTIONS EXPLORED : ", explored_actions)

        # # récupère les actions inexplorées
        # unexplored_actions = [action for action in self.possible_actions if action not in explored_actions]
        # print("ACTIONS UNEXPLORED : ", explored_actions)
        # return unexplored_actions


    # mise à jour des variables visite et score du noeud 
    def update_stats(self, score):
        self.visits += 1
        self.total_score += score

    # retourne un score 
    def get_ucb_score(self):
        if self.visits == 0:
            return float('inf')
        return self.total_score / self.visits + math.sqrt(2 * math.log(self.parent.visits) / self.visits)