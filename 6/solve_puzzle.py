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
    configSet = set();
    answer = computeAnswer(config);

    while answer not in configSet:
#        print("GO");
        moves += cont_solve_puzzle(config, answer, configSet);
#    print(configSet)

    return moves[:len(moves)-1];

def cont_solve_puzzle(config, answer, configSet):
    moves = [];
    zero = findZero(config);
#    print("config", config);
#    print("configs:", configSet);
#    print("zero", zero);
    if config not in configSet:
        configSet.add(config);
#        print(1, zero);
        if config==answer:
            return ["DONE"];
        if zero[0] < len(config)-1:
#            print(1);
            copy = list(list(line) for line in config);
            copy[zero[0]][zero[1]], copy[zero[0]+1][zero[1]] = copy[zero[0]+1][zero[1]], copy[zero[0]][zero[1]];         
            copy = tuple(tuple(line) for line in copy);
            direction = cont_solve_puzzle(copy, answer, configSet)
            if direction:
                moves += ['U'] + direction;
#        print(2, zero);        
        if zero[1] > 0:
#            print(2);
            copy = list(list(line) for line in config);
            copy[zero[0]][zero[1]], copy[zero[0]][zero[1]-1] = copy[zero[0]][zero[1]-1], copy[zero[0]][zero[1]]
            copy = tuple(tuple(line) for line in copy);
            direction = cont_solve_puzzle(copy, answer, configSet)
            if direction:
                moves += ['R'] + direction;
#        print(3, zero);
        if zero[0] > 0:
#            print(3);
            copy = list(list(line) for line in config);
            copy[zero[0]][zero[1]], copy[zero[0]-1][zero[1]] = copy[zero[0]-1][zero[1]], copy[zero[0]][zero[1]]
            copy = tuple(tuple(line) for line in copy);
            direction = cont_solve_puzzle(copy, answer, configSet)
            if direction:
                moves += ['D'] + direction;
#        print(2, zero);        
        if zero[1] < len(config[0])-1:
#            print(4);
            copy = list(list(line) for line in config);
            copy[zero[0]][zero[1]], copy[zero[0]][zero[1]+1] = copy[zero[0]][zero[1]+1], copy[zero[0]][zero[1]]
            copy = tuple(tuple(line) for line in copy);
            direction = cont_solve_puzzle(copy, answer, configSet)
            if direction:
                moves += ['L'] + direction;
    return moves;
