class Node:

    moves = ['UP', 'DOWN', 'LEFT', 'RIGHT']

    def __init__(self, board, parent=None):
        self._board = board
        self.parent = parent
        self.children = []
        self.visited = 0
        self._score = 0

    @property
    def board(self):
        return self._board
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, s):
        self._score = s

    # TODO : faire une fonction apply move, qu'on appelera dans le for move in moves
    def apply_move(self, move):
        merged = [[False for _ in range(4)] for _ in range(4)]
        if move == 'UP':
            for i in range(4):
                for j in range(4):
                    shift = 0
                    if i > 0:
                        for q in range(i):
                            if self._board[q][j] == 0:
                                shift += 1
                        if shift > 0:
                            self._board[i - shift][j] = self._board[i][j]
                            self._board[i][j] = 0
                        if self._board[i - shift - 1][j] == self._board[i - shift][j] and not merged[i - shift][j] \
                                and not merged[i - shift - 1][j]:
                            self._board[i - shift - 1][j] *= 2
                            self._score += self._board[i - shift - 1][j]
                            self._board[i - shift][j] = 0
                            merged[i - shift - 1][j] = True

        elif move == 'DOWN':
            for i in range(3):
                for j in range(4):
                    shift = 0
                    for q in range(i + 1):
                        if self._board[3 - q][j] == 0:
                            shift += 1
                    if shift > 0:
                        self._board[2 - i + shift][j] = self._board[2 - i][j]
                        self._board[2 - i][j] = 0
                    if 3 - i + shift <= 3:
                        if self._board[2 - i + shift][j] == self._board[3 - i + shift][j] and not merged[3 - i + shift][j] \
                                and not merged[2 - i + shift][j]:
                            self._board[3 - i + shift][j] *= 2
                            self._score += self._board[3 - i + shift][j]
                            self._board[2 - i + shift][j] = 0
                            merged[3 - i + shift][j] = True

        elif move == 'LEFT':
            for i in range(4):
                for j in range(4):
                    shift = 0
                    for q in range(j):
                        if self._board[i][q] == 0:
                            shift += 1
                    if shift > 0:
                        self._board[i][j - shift] = self._board[i][j]
                        self._board[i][j] = 0
                    if self._board[i][j - shift] == self._board[i][j - shift - 1] and not merged[i][j - shift - 1] \
                            and not merged[i][j - shift]:
                        self._board[i][j - shift - 1] *= 2
                        self._score += self._board[i][j - shift - 1]
                        self._board[i][j - shift] = 0
                        merged[i][j - shift - 1] = True

        elif move == 'RIGHT':
            for i in range(4):
                for j in range(4):
                    shift = 0
                    for q in range(j):
                        if self._board[i][3 - q] == 0:
                            shift += 1
                    if shift > 0:
                        self._board[i][3 - j + shift] = self._board[i][3 - j]
                        self._board[i][3 - j] = 0
                    if 4 - j + shift <= 3:
                        if self._board[i][4 - j + shift] == self._board[i][3 - j + shift] and not merged[i][4 - j + shift] \
                                and not merged[i][3 - j + shift]:
                            self._board[i][4 - j + shift] *= 2
                            self._score += self._board[i][4 - j + shift]
                            self._board[i][3 - j + shift] = 0
                            merged[i][4 - j + shift] = True
    
    def get_possible_moves(self):
        global score
        merged = [[False for _ in range(4)] for _ in range(4)]
        for move in self.moves:
            board_temp = self._board
            child = Node(board_temp)

            if move == 'UP':
                for i in range(4):
                    for j in range(4):
                        shift = 0
                        if i > 0:
                            for q in range(i):
                                if board_temp[q][j] == 0:
                                    shift += 1
                            if shift > 0:
                                board_temp[i - shift][j] = board_temp[i][j]
                                board_temp[i][j] = 0
                            if board_temp[i - shift - 1][j] == board_temp[i - shift][j] and not merged[i - shift][j] \
                                    and not merged[i - shift - 1][j]:
                                board_temp[i - shift - 1][j] *= 2
                                child.score += board_temp[i - shift - 1][j]
                                board_temp[i - shift][j] = 0
                                merged[i - shift - 1][j] = True

            elif move == 'DOWN':
                for i in range(3):
                    for j in range(4):
                        shift = 0
                        for q in range(i + 1):
                            if board_temp[3 - q][j] == 0:
                                shift += 1
                        if shift > 0:
                            board_temp[2 - i + shift][j] = board_temp[2 - i][j]
                            board_temp[2 - i][j] = 0
                        if 3 - i + shift <= 3:
                            if board_temp[2 - i + shift][j] == board_temp[3 - i + shift][j] and not merged[3 - i + shift][j] \
                                    and not merged[2 - i + shift][j]:
                                board_temp[3 - i + shift][j] *= 2
                                child.score += board_temp[3 - i + shift][j]
                                board_temp[2 - i + shift][j] = 0
                                merged[3 - i + shift][j] = True

            elif move == 'LEFT':
                for i in range(4):
                    for j in range(4):
                        shift = 0
                        for q in range(j):
                            if board_temp[i][q] == 0:
                                shift += 1
                        if shift > 0:
                            board_temp[i][j - shift] = board_temp[i][j]
                            board_temp[i][j] = 0
                        if board_temp[i][j - shift] == board_temp[i][j - shift - 1] and not merged[i][j - shift - 1] \
                                and not merged[i][j - shift]:
                            board_temp[i][j - shift - 1] *= 2
                            child.score += board_temp[i][j - shift - 1]
                            board_temp[i][j - shift] = 0
                            merged[i][j - shift - 1] = True

            elif move == 'RIGHT':
                for i in range(4):
                    for j in range(4):
                        shift = 0
                        for q in range(j):
                            if board_temp[i][3 - q] == 0:
                                shift += 1
                        if shift > 0:
                            board_temp[i][3 - j + shift] = board_temp[i][3 - j]
                            board_temp[i][3 - j] = 0
                        if 4 - j + shift <= 3:
                            if board_temp[i][4 - j + shift] == board_temp[i][3 - j + shift] and not merged[i][4 - j + shift] \
                                    and not merged[i][3 - j + shift]:
                                board_temp[i][4 - j + shift] *= 2
                                child.score += board_temp[i][4 - j + shift]
                                board_temp[i][3 - j + shift] = 0
                                merged[i][4 - j + shift] = True

            self.children.append(child)
        
        return self.children
