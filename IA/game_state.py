class GameState:
    def __init__(self, board_values):
        self.board_values = board_values
        self.score = 0

    '''
    ############## GETTERS #################
    '''
    def get_board(self):
        return self.board_values
    

    def get_score(self):
        return self.score

    # Déterminez si le jeu est terminé (aucun mouvement possible)
    def is_game_over(self):
        for i in range(4):
            for j in range(4):
                if self.board_values[i][j] == 0:
                    return False
                if j > 0 and self.board_values[i][j] == self.board_values[i][j - 1]:
                    return False
                if i > 0 and self.board_values[i][j] == self.board_values[i - 1][j]:
                    return False
        return True

    # Effectue une action sur l'état du jeu et renvoie le nouvel état
    def perform_action(self, action):
        new_board = [row[:] for row in self.board_values]
        score_increment = 0  # Initialiser l'incrément de score à zéro

        if action == 'UP':
            for j in range(4):
                i = 0
                while i < 3:
                    if new_board[i][j] != 0:
                        row = i
                        while row > 0 and (new_board[row - 1][j] == 0 or new_board[row - 1][j] == new_board[i][j]):
                            if new_board[row - 1][j] == new_board[i][j]:
                                new_board[row - 1][j] *= 2
                                score_increment += new_board[row - 1][j]  # Incrémentation du score
                                new_board[i][j] = 0
                                break
                            else:
                                new_board[row - 1][j] = new_board[row][j]
                                new_board[row][j] = 0
                                row -= 1
                    i += 1

        elif action == 'DOWN':
            for j in range(4):
                i = 3
                while i > 0:
                    if new_board[i][j] != 0:
                        row = i
                        while row < 3 and (new_board[row + 1][j] == 0 or new_board[row + 1][j] == new_board[i][j]):
                            if new_board[row + 1][j] == new_board[i][j]:
                                new_board[row + 1][j] *= 2
                                score_increment += new_board[row + 1][j]  # Incrémentation du score
                                new_board[i][j] = 0
                                break
                            else:
                                new_board[row + 1][j] = new_board[row][j]
                                new_board[row][j] = 0
                                row += 1
                    i -= 1

        elif action == 'LEFT':
            for i in range(4):
                j = 0
                while j < 3:
                    if new_board[i][j] != 0:
                        col = j
                        while col > 0 and (new_board[i][col - 1] == 0 or new_board[i][col - 1] == new_board[i][j]):
                            if new_board[i][col - 1] == new_board[i][j]:
                                new_board[i][col - 1] *= 2
                                score_increment += new_board[i][col - 1]  # Incrémentation du score
                                new_board[i][j] = 0
                                break
                            else:
                                new_board[i][col - 1] = new_board[i][col]
                                new_board[i][col] = 0
                                col -= 1
                    j += 1

        elif action == 'RIGHT':
            for i in range(4):
                j = 3
                while j > 0:
                    if new_board[i][j] != 0:
                        col = j
                        while col < 3 and (new_board[i][col + 1] == 0 or new_board[i][col + 1] == new_board[i][j]):
                            if new_board[i][col + 1] == new_board[i][j]:
                                new_board[i][col + 1] *= 2
                                score_increment += new_board[i][col + 1]  # Incrémentation du score
                                new_board[i][j] = 0
                                break
                            else:
                                new_board[i][col + 1] = new_board[i][col]
                                new_board[i][col] = 0
                                col += 1
                    j -= 1

        # Mettre à jour le score total de l'état du jeu
        self.score += score_increment
        # Retourner le nouvel état après l'action
        return GameState(new_board)
