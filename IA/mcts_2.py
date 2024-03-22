import random
from Node2 import Node

class MCTS:
    def __init__(self, game_state):
        self.game_state = game_state

    # getter de game_state
    def game_state(self):
        return self.game_state

    # Recherche MCTS pour choisir la meilleure action
    def search(self, num_iterations):
        # noeud root
        root_node = Node(self.game_state)
        # itéré 10 fois
        for iteration in range(num_iterations):
            print(f"Iteration {iteration + 1}/{num_iterations}")
            node = root_node
            # Sélection
            # tant que le jeu n'est pas terminé
            i = 0 
            while not node.is_terminal() and i < num_iterations:
                print("=============================================", i)
                i+=1
                # si tous les enfants n'ont pas été exploré 
                if node.is_fully_expanded():
                    # on sélectionne un enfant
                    node = self.select_child_node(node)
                else:
                    # sinon, on fait l'expension
                    node = self.expand_node(node)
            # quand le jeu est fini
            # Simulation
            simulation_result = self.simulate(node)

            # Backpropagation
            self.backpropagate(node, simulation_result)
        return root_node

    # Choix de l'action finale basée sur les statistiques MCTS
    def select_action(self):
        root_node = self.search(num_iterations=10)
        return self.select_child_node(root_node).get_action()


    # Choix du nœud enfant à explorer
    def select_child_node(self, node):
        print(node.get_children())
        return max(node.get_children(), key=lambda child: child.get_ucb_score())

    # Expansion dans un nœud de l'arbre de recherche
    def expand_node(self, node):
        print(" ========= SCORE: ", node.state.get_score())
        print("ETAT DE JEU DU NOEUD : ", node.get_state().get_board())
        # on récupère les actions inexplorées
        unexplored_actions = node.get_unexplored_actions()
        # on en choisit une au hasard 
        todo_action = random.choice(node.get_unexplored_actions())
        print("choix de l'action : ", todo_action)
        # on récupère le nouvel état du noeud en applicant ce choix au hasard 
        new_state = node.get_state().perform_action(todo_action)
        # on crée cet enfant 
        new_node = Node(new_state, parent=node, parent_action=todo_action)
        # on l'ajoute à la liste d'enfant du noeud actuel 
        node.add_child(new_node)
        print("SIZE OF CHILDREN : ", len(node.get_children()))
        # on enlève l'action des actions possibles du noeud 
        node.remove_actions(todo_action)
        print("actions restant du noeud : ", node.get_possible_actions())
        return new_node

    # Simulez un jeu à partir de l'état actuel
    def simulate(self, node, num_iterations=10):
        # tant que le jeu n'est pas fini
        i = 0
        while not node.get_state().is_game_over() and i < num_iterations:
            i+=1
            action = random.choice(node.get_possible_actions())
            print(f"Action choisie pour simulation : {action}")
            state = node.state.perform_action(action)
        print("Simulation terminée")
        return self.calculate_score(state)

    # Mise à jour des statistiques des nœuds de l'arbre en fonction du résultat de la simulation
    def backpropagate(self, node, result): 
        while node is not None:
            print(f"Mise à jour du nœud : Visites = {node.visits}, Score total = {node.total_score}")
            node.update_stats(result)
            node = node.get_parent()

    # Calculez le score final à partir de l'état final du jeu
    def calculate_score(self, state):
        return sum(map(sum, state.get_board()))

