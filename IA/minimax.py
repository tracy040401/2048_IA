# build 2048 in python using pygame!!
import pygame
import random

pygame.init()

# initial set up
WIDTH = 400
HEIGHT = 500
RANDOM_EVENT_AT_NODE = True
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('2048')
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 24)

# 2048 game color library
colors = {0: (204, 192, 179),
          2: (238, 228, 218),
          4: (237, 224, 200),
          8: (242, 177, 121),
          16: (245, 149, 99),
          32: (246, 124, 95),
          64: (246, 94, 59),
          128: (237, 207, 114),
          256: (237, 204, 97),
          512: (237, 200, 80),
          1024: (237, 197, 63),
          2048: (237, 194, 46),
          'light text': (249, 246, 242),
          'dark text': (119, 110, 101),
          'other': (0, 0, 0),
          'bg': (187, 173, 160)}

# game variables initialize
board_values = [[0 for _ in range(4)] for _ in range(4)]
game_over = False
spawn_new = True
init_count = 0
direction = ''
score = 0
file = open('high_score', 'r')
init_high = int(file.readline())
file.close()
high_score = init_high


# draw game over and restart text
def draw_over():
    pygame.draw.rect(screen, 'black', [50, 50, 300, 100], 0, 10)
    game_over_text1 = font.render('Game Over!', True, 'white')
    game_over_text2 = font.render('Press Enter to Restart', True, 'white')
    screen.blit(game_over_text1, (130, 65))
    screen.blit(game_over_text2, (70, 105))


# take your turn based on direction
def take_turn(direc, board):
    global score
    merged = [[False for _ in range(4)] for _ in range(4)]
    if direc == 'UP':
        for i in range(4):
            for j in range(4):
                shift = 0
                if i > 0:
                    for q in range(i):
                        if board[q][j] == 0:
                            shift += 1
                    if shift > 0:
                        board[i - shift][j] = board[i][j]
                        board[i][j] = 0
                    if board[i - shift - 1][j] == board[i - shift][j] and not merged[i - shift][j] \
                            and not merged[i - shift - 1][j]:
                        board[i - shift - 1][j] *= 2
                        score += board[i - shift - 1][j]
                        board[i - shift][j] = 0
                        merged[i - shift - 1][j] = True

    elif direc == 'DOWN':
        for i in range(3):
            for j in range(4):
                shift = 0
                for q in range(i + 1):
                    if board[3 - q][j] == 0:
                        shift += 1
                if shift > 0:
                    board[2 - i + shift][j] = board[2 - i][j]
                    board[2 - i][j] = 0
                if 3 - i + shift <= 3:
                    if board[2 - i + shift][j] == board[3 - i + shift][j] and not merged[3 - i + shift][j] \
                            and not merged[2 - i + shift][j]:
                        board[3 - i + shift][j] *= 2
                        score += board[3 - i + shift][j]
                        board[2 - i + shift][j] = 0
                        merged[3 - i + shift][j] = True

    elif direc == 'LEFT':
        for i in range(4):
            for j in range(4):
                shift = 0
                for q in range(j):
                    if board[i][q] == 0:
                        shift += 1
                if shift > 0:
                    board[i][j - shift] = board[i][j]
                    board[i][j] = 0
                if board[i][j - shift] == board[i][j - shift - 1] and not merged[i][j - shift - 1] \
                        and not merged[i][j - shift]:
                    board[i][j - shift - 1] *= 2
                    score += board[i][j - shift - 1]
                    board[i][j - shift] = 0
                    merged[i][j - shift - 1] = True

    elif direc == 'RIGHT':
        for i in range(4):
            for j in range(4):
                shift = 0
                for q in range(j):
                    if board[i][3 - q] == 0:
                        shift += 1
                if shift > 0:
                    board[i][3 - j + shift] = board[i][3 - j]
                    board[i][3 - j] = 0
                if 4 - j + shift <= 3:
                    if board[i][4 - j + shift] == board[i][3 - j + shift] and not merged[i][4 - j + shift] \
                            and not merged[i][3 - j + shift]:
                        board[i][4 - j + shift] *= 2
                        score += board[i][4 - j + shift]
                        board[i][3 - j + shift] = 0
                        merged[i][4 - j + shift] = True
    return board


# spawn in new pieces randomly when turns start
def new_pieces(board):
    count = 0
    full = False
    while any(0 in row for row in board) and count < 1:
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        if board[row][col] == 0:
            count += 1
            if random.randint(1, 10) == 10:
                board[row][col] = 4
            else:
                board[row][col] = 2
    if count < 1:
        full = True
    return board, full


# draw background for the board
def draw_board():
    pygame.draw.rect(screen, colors['bg'], [0, 0, 400, 400], 0, 10)
    score_text = font.render(f'Score: {score}', True, 'black')
    high_score_text = font.render(f'High Score: {high_score}', True, 'black')
    screen.blit(score_text, (10, 410))
    screen.blit(high_score_text, (10, 450))
    pass


# draw tiles for game
def draw_pieces(board):
    for i in range(4):
        for j in range(4):
            value = board[i][j]
            if value > 8:
                value_color = colors['light text']
            else:
                value_color = colors['dark text']
            if value <= 2048:
                color = colors[value]
            else:
                color = colors['other']
            pygame.draw.rect(screen, color, [j * 95 + 20, i * 95 + 20, 75, 75], 0, 5)
            if value > 0:
                value_len = len(str(value))
                font = pygame.font.Font('freesansbold.ttf', 48 - (5 * value_len))
                value_text = font.render(str(value), True, value_color)
                text_rect = value_text.get_rect(center=(j * 95 + 57, i * 95 + 57))
                screen.blit(value_text, text_rect)
                pygame.draw.rect(screen, 'black', [j * 95 + 20, i * 95 + 20, 75, 75], 2, 5)

# Make a copie of the actual board 
def clone(board):
    return [row[:] for row in board]

def evaluate(board):
    empty_cells = sum(row.count(0) for row in board) 
    max_tile = max(max(row) for row in board) 
    eval_score = 0

     # heuristique 1 : + il y a de case vide, mieux c'est 
    eval_score += empty_cells


    # heuristique 2: on préfère une organisation de grille en serpentin
    # avec la valeur la + importante en haut à gauche
    corner_weights = [[10, 8, 7, 6],
                      [8, 6, 5, 4],
                      [7, 5, 4, 3],
                      [6, 4, 3, 2]]
    for i in range(4):
        for j in range(4):
            eval_score += board[i][j] * corner_weights[i][j]
    
    # heuristique 3: gros bonus si la valeur la + haute est en haut à gauche 
    max_tile = max(max(row) for row in board) 
    if board[0][0] == max_tile: 
        eval_score += 100

    return eval_score

def minimax(actual_board, depth, maximizing_player):
    board = clone(actual_board)
    if depth == 0 or game_over:
        return None, evaluate(board)
    # joueur maximisant
    if maximizing_player:
        max_score = float('-inf')
        best_move = None

        for move in ['UP', 'DOWN', 'LEFT', 'RIGHT']:
            new_board = take_turn(move, board)
            _, new_score = minimax(new_board, depth - 1, False)
            if new_score > max_score:
                max_score = new_score
                best_move = move
        return best_move, max_score
    # joueur minimisant
    else:
        min_score = float('inf')
        best_move = None

        for move in ['UP', 'DOWN', 'LEFT', 'RIGHT']:
            new_board = take_turn(move, board)
            _, new_score = minimax(new_board, depth - 1, True)
            if new_score < min_score:
                min_score = new_score
                best_move = move
        return best_move, min_score


def expectiminimax(board, depth, maximizing_player):
    # si on a atteint la longueur max de l'arbre ou si le jeu est terminé
    if depth == 0 or game_over:
        # on retourne l'évaluation de la grille (avec les heuristiques définies)
        return None, evaluate(board)

    # si on est dans un noeud maximisant
    if maximizing_player:
        # on initialise le score maximal à -infini
        max_score = float('-inf')
        best_move = None

        # pour chacun des mouvements possibles
        for move in ['UP', 'DOWN', 'LEFT', 'RIGHT']:
            # on regarde le score obtenu après avoir effectué le mouvement
            new_board = take_turn(move, board)
            # et on rappelle récursivement la fonction avec depth - 1 et en changeant de joueur
            _, new_score = expectiminimax(new_board, depth - 1, False)
            # si le score obtenu est supérieur au score maximal actuel
            if new_score > max_score:
                # on met à jour le score et le mouvement
                max_score = new_score
                best_move = move
        return best_move, max_score
    # si on est dans un noeud chance 
    elif RANDOM_EVENT_AT_NODE:
        total_score = 0
        num_children = 0

        # pour chacun des mouvements possibles 
        for move in ['UP', 'DOWN', 'LEFT', 'RIGHT']:
            # on regarde le score obtenu après avoir effectué le mouvement
            new_board = take_turn(move, board)
            # et on rappelle récursivement la fonction avec depth - 1 et en changeant de joueur 
            _, new_score = expectiminimax(new_board, depth - 1, True)
            # on met à jour le score total et le nombre d'enfants
            total_score += new_score
            num_children += 1
        # on retourne la moyenne des scores obtenus
        return None, total_score / num_children
    # si on est dans un noeud minimisant
    else:
        # on initialise le score minimal à +infini
        min_score = float('inf')
        best_move = None

        # pour chacun des mouvements possibles
        for move in ['UP', 'DOWN', 'LEFT', 'RIGHT']:
            # on regarde le score obtenu après avoir effectué le mouvement
            new_board = take_turn(move, board)
            # et on rappelle récursivement la fonction avec depth - 1 et en changeant de joueur
            _, new_score = expectiminimax(new_board, depth - 1, True)
            # si le score est inférieur au score minimal actuel
            if new_score < min_score:
                # on met à jour le score et le mouvement
                min_score = new_score
                best_move = move
        return best_move, min_score




# main game loop
run = True
while run:
    timer.tick(fps)
    screen.fill('gray')
    draw_board()
    draw_pieces(board_values)
    if spawn_new or init_count < 2:
        board_values, game_over = new_pieces(board_values)
        spawn_new = False
        init_count += 1
    if direction != '':
        board_values = take_turn(direction, board_values)
        direction = ''
        spawn_new = True
    if game_over:
        draw_over()
        if high_score > init_high:
            file = open('high_score', 'w')
            file.write(f'{high_score}')
            file.close()
            init_high = high_score

    else:
        best_move, _ = expectiminimax(board_values, depth=6, maximizing_player=True)
        # best_move = random_move(board_values)
        # best_move, _ = minimax(board_values, depth=6, maximizing_player=True)
        if best_move:
            old_board_values = clone(board_values)
            board_values = take_turn(best_move, board_values)
            if board_values != old_board_values:
                RANDOM_EVENT_AT_NODE = True
            else:
                RANDOM_EVENT_AT_NODE = False
            direction = best_move


    for event in pygame.event.get():
        if game_over:
            if event.key == pygame.K_RETURN:
                board_values = [[0 for _ in range(4)] for _ in range(4)]
                spawn_new = True
                init_count = 0
                score = 0
                direction = ''
                game_over = False
        else:
            break

    if score > high_score:
        high_score = score

    pygame.display.flip()
pygame.quit()
