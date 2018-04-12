def findZero(config):
    for y in range(len(config)):
        for x in range(len(config[y])):
            if config[y][x] == 0:
                return (y, x);
    return (0, 0);

def computeAnswer(matrix):
    answer = [];
    track = len(matrix)*len(matrix[1])-1;
    for y in range(len(matrix)):
        line = [];
        for x in range(len(matrix[y])):
            line += [track];
            track -= 1;
        answer.append(tuple(line))
    return tuple(answer);

def solve_puzzle(config):
    '''Returns move sequence to solve configuration, or None'''
    moves = []
    level = [];
    level += [[config,moves]];
    configSet = set();
    answer = computeAnswer(config);

    while level:
        newlevel = [];
        for tup in level:
            matrix = tuple(tuple(line) for line in tup[0])
            if matrix == answer:
                return tup[1];
            if matrix not in configSet:
                configSet.add(matrix);
                zero = findZero(matrix);
                if zero[0] < len(matrix)-1:
                    copy = list(list(line) for line in matrix);
                    copy[zero[0]][zero[1]], copy[zero[0]+1][zero[1]] = copy[zero[0]+1][zero[1]], copy[zero[0]][zero[1]];
                    newlevel+=[[copy, tup[1]+['U']]]
                if zero[1] > 0:
                    copy = list(list(line) for line in matrix);
                    copy[zero[0]][zero[1]], copy[zero[0]][zero[1]-1] = copy[zero[0]][zero[1]-1], copy[zero[0]][zero[1]]
                    newlevel+=[[copy, tup[1]+['R']]]
                if zero[0] > 0:
                    copy = list(list(line) for line in matrix);
                    copy[zero[0]][zero[1]], copy[zero[0]-1][zero[1]] = copy[zero[0]-1][zero[1]], copy[zero[0]][zero[1]]
                    newlevel+=[[copy, tup[1]+['D']]]
                if zero[1] < len(matrix[0])-1:
                    copy = list(list(line) for line in matrix);
                    copy[zero[0]][zero[1]], copy[zero[0]][zero[1]+1] = copy[zero[0]][zero[1]+1], copy[zero[0]][zero[1]]
                    newlevel+=[[copy, tup[1]+['L']]]
        level = newlevel;

    return None;

# def cont_solve_puzzle(config, answer, configSet):
#     moves = [];
#
#     if config not in configSet:
#         configSet.add(config);
#         if config==answer:
#             return ["DONE"];
#         if zero[0] < len(config)-1:
#             copy = list(list(line) for line in config);
#             copy[zero[0]][zero[1]], copy[zero[0]+1][zero[1]] = copy[zero[0]+1][zero[1]], copy[zero[0]][zero[1]];
#             copy = tuple(tuple(line) for line in copy);
#             direction = cont_solve_puzzle(copy, answer, configSet)
#             if direction:
#                 moves += ['U'] + direction;
#         if zero[1] > 0:
#             copy = list(list(line) for line in config);
#             copy[zero[0]][zero[1]], copy[zero[0]][zero[1]-1] = copy[zero[0]][zero[1]-1], copy[zero[0]][zero[1]]
#             copy = tuple(tuple(line) for line in copy);
#             direction = cont_solve_puzzle(copy, answer, configSet)
#             if direction:
#                 moves += ['R'] + direction;
#         if zero[0] > 0:
#             copy = list(list(line) for line in config);
#             copy[zero[0]][zero[1]], copy[zero[0]-1][zero[1]] = copy[zero[0]-1][zero[1]], copy[zero[0]][zero[1]]
#             copy = tuple(tuple(line) for line in copy);
#             direction = cont_solve_puzzle(copy, answer, configSet)
#             if direction:
#                 moves += ['D'] + direction;
#         if zero[1] < len(config[0])-1:
#             copy = list(list(line) for line in config);
#             copy[zero[0]][zero[1]], copy[zero[0]][zero[1]+1] = copy[zero[0]][zero[1]+1], copy[zero[0]][zero[1]]
#             copy = tuple(tuple(line) for line in copy);
#             direction = cont_solve_puzzle(copy, answer, configSet)
#             if direction:
#                 moves += ['L'] + direction;
#     return moves;