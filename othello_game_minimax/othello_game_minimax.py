import random
import copy
import matplotlib.pyplot as plt

def generate_board():
    # generate new board
    board = [[[] for _ in range(8)] for _ in range(8)]
    board[3][3] = 'o'
    board[3][4] = 'x'
    board[4][3] = 'x'
    board[4][4] = 'o'
    return board


def get_board(board):
    # return board to print
    actual_board = '\n'
    for line_y in range(8):
        for line_x in range(8):
            if str(board[line_y][line_x]) in ['x', 'o']:
                actual_board += str(board[line_y][line_x]) + ' '
            else:
                actual_board += '. '
        actual_board += '\n'
    return actual_board


def find_moves(board, player):
    # find all possible moves
    # checking possibilities in all dimensions
    # up, down, left, right, and four crosses
    if player == 'x':
        opponent = 'o'
    else:
        opponent = 'x'
    moves = {}
    for x in range(8):
        for y in range(8):
            if board[y][x] not in ['x', 'o']:
                j = x - 1
                if j >= 0 and board[y][j] == opponent:
                    j = j - 1
                    while j >= 0 and board[y][j] == opponent:
                        j = j - 1
                    if j >= 0 and board[y][j] == player:
                        moves[(y, x)] = 1
                        continue
                i = y - 1
                if i >= 0 and board[i][x] == opponent:
                    i = i - 1
                    while i >= 0 and board[i][x] == opponent:
                        i = i - 1
                    if i >= 0 and board[i][x] == player:
                        moves[(y, x)] = 1
                        continue
                j = x + 1
                if j < 8 and board[y][j] == opponent:
                    j = j + 1
                    while j < 8 and board[y][j] == opponent:
                        j = j + 1
                    if j < 8 and board[y][j] == player:
                        moves[(y, x)] = 1
                        continue
                i = y + 1
                j = x + 1
                if i < 8 and j < 8 and board[i][j] == opponent:
                    i = i + 1
                    j = j + 1
                    while i < 8 and j < 8 and board[i][j] == opponent:
                        i = i + 1
                        j = j + 1
                    if i < 8 and j < 8 and board[i][j] == player:
                        moves[(y, x)] = 1
                        continue
                i = y + 1
                if i < 8 and board[i][x] == opponent:
                    i = i + 1
                    while i < 8 and board[i][x] == opponent:
                        i = i + 1
                    if i < 8 and board[i][x] == player:
                        moves[(y, x)] = 1
                        continue
                i = y - 1
                j = x + 1
                if i >= 0 and j < 8 and board[i][j] == opponent:
                    i = i - 1
                    j = j + 1
                    while i >= 0 and j < 8 and board[i][j] == opponent:
                        i = i - 1
                        j = j + 1
                    if i >= 0 and j < 8 and board[i][j] == player:
                        moves[(y, x)] = 1
                        continue
                i = y + 1
                j = x - 1
                if i < 8 and j >= 0 and board[i][j] == opponent:
                    i = i + 1
                    j = j - 1
                    while i < 8 and j >= 0 and board[i][j] == opponent:
                        i = i + 1
                        j = j - 1
                    if i < 8 and j >= 0 and board[i][j] == player:
                        moves[(y, x)] = 1
                        continue
                i = y - 1
                j = x - 1
                if i >= 0 and j >= 0 and board[i][j] == opponent:
                    i = i - 1
                    j = j - 1
                    while i >= 0 and j >= 0 and board[i][j] == opponent:
                        i = i - 1
                        j = j - 1
                    if i >= 0 and j >= 0 and board[i][j] == player:
                        moves[(y, x)] = 1
    return moves


def selections(y, x, board, player):
    # select point on board by player
    # and changing all opponent points
    # between new point of player
    if player == 'x':
        opponent = 'o'
    else:
        opponent = 'x'
    i = y - 1
    if i >= 0 and board[i][x] == opponent:
        i = i - 1
        while i >= 0 and board[i][x] == opponent:
            i = i - 1
        if i >= 0 and board[i][x] == player:
            i += 1
            next_move = opponent
            while i <= y:
                board[i][x] = player
                i += 1
    i = y - 1
    j = x + 1
    if i >= 0 and j < 8 and board[i][j] == opponent:
        i = i - 1
        j = j + 1
        while i >= 0 and j < 8 and board[i][j] == opponent:
            i = i - 1
            j = j + 1
        if i >= 0 and j < 8 and board[i][j] == player:
            i = i + 1
            j = j - 1
            next_move = opponent
            while i <= y:
                board[i][j] = player
                i = i + 1
                j = j - 1
    j = x + 1
    if j < 8 and board[y][j] == opponent:
        j = j + 1
        while j < 8 and board[y][j] == opponent:
            j = j + 1
        if j < 8 and board[y][j] == player:
            j = j - 1
            next_move = opponent
            while j >= x:
                board[y][j] = player
                j -= 1
    i = y + 1
    j = x + 1
    if i < 8 and j < 8 and board[i][j] == opponent:
        i = i + 1
        j = j + 1
        while i < 8 and j < 8 and board[i][j] == opponent:
            i = i + 1
            j = j + 1
        if i < 8 and j < 8 and board[i][j] == player:
            i = i - 1
            j = j - 1
            next_move = opponent
            while i >= y:
                board[i][j] = player
                i = i - 1
                j = j - 1
    i = y + 1
    j = x - 1
    if i < 8 and j >= 0 and board[i][j] == opponent:
        i = i + 1
        j = j - 1
        while i < 8 and j >= 0 and board[i][j] == opponent:
            i = i + 1
            j = j - 1
        if i < 8 and j >= 0 and board[i][j] == player:
            i = i - 1
            j = j + 1
            next_move = opponent
            while i >= y:
                board[i][j] = player
                i = i - 1
                j = j + 1
        i = y + 1
    if i < 8 and board[i][x] == opponent:
        i = i + 1
        while i < 8 and board[i][x] == opponent:
            i = i + 1
        if i < 8 and board[i][x] == player:
            i = i - 1
            next_move = opponent
            while i >= y:
                board[i][x] = player
                i -= 1
    j = x - 1
    if j >= 0 and board[y][j] == opponent:
        j = j - 1
        while j >= 0 and board[y][j] == opponent:
            j = j - 1
        if j >= 0 and board[y][j] == player:
            j += 1
            next_move = opponent
            while j <= x:
                board[y][j] = player
                j += 1
    i = y - 1
    j = x - 1
    if i >= 0 and j >= 0 and board[i][j] == opponent:
        i = i - 1
        j = j - 1
        while i >= 0 and j >= 0 and board[i][j] == opponent:
            i = i - 1
            j = j - 1
        if i >= 0 and j >= 0 and board[i][j] == player:
            i = i + 1
            j = j + 1
            next_move = opponent
            while i <= y:
                board[i][j] = player
                i = i + 1
                j = j + 1
    if next_move == opponent:
        return opponent


def result(board):
    # return result of a match
    result_o = 0
    result_x = 0
    for x in range(8):
        for y in range(8):
            if board[y][x] == 'x':
                result_x += 1
            elif board[y][x] == 'o':
                result_o += 1
    result = result_x, result_o
    return result


def othello(type_player=1, type_opponent=2, depth=4):
    # type of players in argument will decide
    # if player will play with algorithm minimax or random
    # 1 means with algorithm, 2 means randomly
    # third argument is eventual depth of tree
    board = generate_board()
    player = 'o'
    flag = 0
    amount = 0
    while flag != 2:
        print(get_board(board))
        print(f'Move: {player}')
        moves = find_moves(board, player)
        print(moves.keys())
        if moves != {}:
            flag = 0
            if player == 'x' and len(moves) != 1:
                if type_player == 1:
                    choice = minimax(board, depth, player)[0]
                else:
                    choice = random.choice(list(moves.keys()))
            else:
                if type_opponent == 1:
                    choice = minimax(board, depth, player)[0]
                else:
                    choice = random.choice(list(moves.keys()))
            if choice != -1:
                print(f'Chosen point {choice}')
                y = choice[0]
                x = choice[1]
                amount += 1
                selections(y, x, board, player)
        else:
            flag += 1
        if player == 'x':
            player = 'o'
        else:
            player = 'x'
    print(f'Result: X have {result(board)[0]} points, O have {result(board)[1]} points')
    return result(board)[0], result(board)[1], amount


def is_game_end(board):
    # checking if game is finished
    if find_moves(board, 'x') == {} and find_moves(board, 'o') == {}:
        return True
    return False


def minimax(board, depth, player):
    # minimax implementation
    if depth == 0 or is_game_end(board):
        points = result(board)
        points_x = points[0]
        points_o = points[1]
        if player == 'x':
            return None, points_x
        else:
            return None, points_o
    best_choice = [(-1, -1)]
    if find_moves(board, player) == {}:
        if player == 'x':
            player = 'o'
        else:
            player = 'x'
    for choice in find_moves(board, player):
        copy_board = copy.deepcopy(board)
        selections(choice[0], choice[1], copy_board, player)
        if player == 'x':
            opponent = 'o'
        else:
            opponent = 'x'
        evaluation = minimax(copy_board, depth - 1, opponent)
        if evaluation[1] == best_choice[0][0]:
            best_choice.append((choice, evaluation[1]))
        elif evaluation[1] > best_choice[0][1]:
            best_choice = [(choice, evaluation[1])]
    random_from_best = random.choice(best_choice)
    # print(random_from_best)
    return random_from_best[0], random_from_best[1]


def main():

    # player = 1
    # opponent = 2
    # # depth = 4
    # results_minmax_vs_random_o = [[] for _ in range(3)]
    # for depth in range(1, 5):
    #     for _ in range(5):
    #         results_minmax_vs_random_o[depth-1].append(othello(player, opponent, depth)[0])
    # print(results_minmax_vs_random_o)
    # avg_results = []
    # for index in range(4):
    #     avg_results.append(sum(results_minmax_vs_random_o[index])/len(results_minmax_vs_random_o[index]))
    # plt.stem([x for x in range(1, 5)], avg_results, 'o')
    # plt.xlabel('value of depth')
    # plt.ylabel('Average points achieved by minimax')
    # plt.show()
    # player = 2
    # opponent = 1
    # depth = 5
    # result = othello(player, opponent, depth)

    # liczba_wygranych_per_glebokosc = []
    # player = 1
    # opponent = 2
    # for
    value = [0, 0, 0, 0]
    for depth in range(1, 4):
        for _ in range(3):
            gra = othello(1, 2, depth)
            value[depth-1] += gra[2]
        value[depth-1] = value[depth-1]/3



    plt.stem([x for x in range(1, 5)], value, 'o')

    plt.xlabel('value of depth')
    plt.ylabel("Amount of wins by player 'x' and 'o'")
    plt.show()

if __name__ == "__main__":
    main()
