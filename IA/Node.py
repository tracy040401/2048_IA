class Node:

    moves = ['UP', 'DOWN', 'LEFT', 'RIGHT']

    def __init__(self, board, parent=None):
        self._board = board
        self._parent = parent
        self._children = []
        self._visited = 0
        self._score = 0

    @property
    def board(self):
        return self._board
    
    @property
    def score(self):
        return self._score
    
    @property
    def children(self):
        return self._children
    
    @property
    def parent(self):
        return self._parent
    
    @property
    def visited(self):
        return self._visited
    
    @board.setter
    def board(self, b):
        self._board = b.copy()
    
    @parent.setter
    def parent(self, p):
        self._parent = p

    @visited.setter
    def visited(self, v):
        self._visited = v
    
    @children.setter
    def children(self, c):
        self._children = c
    
    @score.setter
    def score(self, s):
        self._score = s
    
    def get_possible_moves(self):
        board_UP = [[0 for _ in range(4)] for _ in range(4)]
        board_DOWN = [[0 for _ in range(4)] for _ in range(4)]
        board_LEFT = [[0 for _ in range(4)] for _ in range(4)]
        board_RIGHT = [[0 for _ in range(4)] for _ in range(4)]

        board_UP = self.board.copy()
        board_DOWN = self.board.copy()
        board_LEFT = self.board.copy()
        board_RIGHT = self.board.copy()

        """ for i in range(4):
                for j in range(4):
                    board_UP[i][j] = self.board[i][j]
                    board_DOWN[i][j] = self.board[i][j]
                    board_LEFT[i][j] = self.board[i][j]
                    board_RIGHT[i][j] = self.board[i][j] """

        child_UP = Node(board_UP, parent=self)
        child_DOWN = Node(board_DOWN, parent=self)
        child_LEFT = Node(board_LEFT, parent=self)
        child_RIGHT = Node(board_RIGHT, parent=self)

        #UP
        merged = [[False for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                shift = 0
                if i > 0:
                    for q in range(i):
                        if board_UP[q][j] == 0:
                            shift += 1
                    if shift > 0:
                        board_UP[i - shift][j] = board_UP[i][j]
                        board_UP[i][j] = 0
                    if board_UP[i - shift - 1][j] == board_UP[i - shift][j] and not merged[i - shift][j] \
                            and not merged[i - shift - 1][j]:
                        board_UP[i - shift - 1][j] *= 2
                        print("board_UP[i-shift-1][j] = ", board_UP[i-shift-1][j])
                        child_UP.score += board_UP[i - shift - 1][j]
                        print("child_UP score : ", child_UP.score)
                        board_UP[i - shift][j] = 0
                        merged[i - shift - 1][j] = True

        #DOWN
        merged = [[False for _ in range(4)] for _ in range(4)]
        for i in range(3):
            for j in range(4):
                shift = 0
                for q in range(i + 1):
                    if board_DOWN[3 - q][j] == 0:
                        shift += 1
                if shift > 0:
                    board_DOWN[2 - i + shift][j] = board_DOWN[2 - i][j]
                    board_DOWN[2 - i][j] = 0
                if 3 - i + shift <= 3:
                    if board_DOWN[2 - i + shift][j] == board_DOWN[3 - i + shift][j] and not merged[3 - i + shift][j] \
                            and not merged[2 - i + shift][j]:
                        board_DOWN[3 - i + shift][j] *= 2
                        print("board_DOWN[i-shift-1][j] = ", board_DOWN[i-shift-1][j])
                        child_DOWN.score += board_DOWN[3 - i + shift][j]
                        print("child_DOWN score : ", child_DOWN.score)
                        board_DOWN[2 - i + shift][j] = 0
                        merged[3 - i + shift][j] = True

        #LEFT
        merged = [[False for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                shift = 0
                for q in range(j):
                    if board_LEFT[i][q] == 0:
                        shift += 1
                if shift > 0:
                    board_LEFT[i][j - shift] = board_LEFT[i][j]
                    board_LEFT[i][j] = 0
                if board_LEFT[i][j - shift] == board_LEFT[i][j - shift - 1] and not merged[i][j - shift - 1] \
                        and not merged[i][j - shift]:
                    board_LEFT[i][j - shift - 1] *= 2
                    print("board_LEFT[i-shift-1][j] = ", board_LEFT[i-shift-1][j])
                    child_LEFT.score += board_LEFT[i][j - shift - 1]
                    print("child_LEFT score : ", child_LEFT.score)
                    board_LEFT[i][j - shift] = 0
                    merged[i][j - shift - 1] = True

        #RIGHT
        merged = [[False for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                shift = 0
                for q in range(j):
                    if board_RIGHT[i][3 - q] == 0:
                        shift += 1
                if shift > 0:
                    board_RIGHT[i][3 - j + shift] = board_RIGHT[i][3 - j]
                    board_RIGHT[i][3 - j] = 0
                if 4 - j + shift <= 3:
                    if board_RIGHT[i][4 - j + shift] == board_RIGHT[i][3 - j + shift] and not merged[i][4 - j + shift] \
                            and not merged[i][3 - j + shift]:
                        board_RIGHT[i][4 - j + shift] *= 2
                        print("board_RIGHT[i-shift-1][j] = ", board_RIGHT[i-shift-1][j])
                        child_RIGHT.score += board_RIGHT[i][4 - j + shift]
                        print("child_RIGHT score : ", child_RIGHT.score)
                        board_RIGHT[i][3 - j + shift] = 0
                        merged[i][4 - j + shift] = True

        #print("score child_UP : ", child_UP.score)
        #print("score child_DOWN : ", child_DOWN.score)
        #print("score child_LEFT : ", child_LEFT.score)
        #print("score child_RIGHT : ", child_RIGHT.score)

        self.children.append(child_UP)
        self.children.append(child_DOWN)
        self.children.append(child_LEFT)
        self.children.append(child_RIGHT)
        #print("children after get_possible_moves : ", self.children)
        
        return self.children

    
    def apply_move(self, move):
        #print("apply_move called.")
        if move == "UP":
            return self.children[0]
        elif move == "DOWN":
            return self.children[1]  
        elif move == "LEFT":
            return self.children[2]
        elif move == "RIGHT":
            return self.children[3]     
