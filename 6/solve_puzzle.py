def conversion(config):
    list = [];
    zero = (0, 0);
    for y in config:
        row = [];
        for x in y:
            row += [x];
            if x == 0:
                zero = (y, x);
        list += [row];
    return list, zero;
def computeAnswer(config):
    track = len(config)*len(config[1])-1;
    for y in range(len(config)):
        for x in range(len(config[y])):
            config[y][x] = track;
            track -= 1;
    return config;

def solve_puzzle(config):
    '''Returns move sequence to solve configuration, or None'''
    moves = []
    zero = ();
    if isinstance(config, tuple):
        config, zero = conversion(config);
    answer = computeAnswer(config);
    if config != answer:
        moves += cont_solve_puzzle(config, zero, answer);
    return moves

def cont_solve_puzzle(config, zero, answer):
    if config != answer:
        #check if anythinga above 0
        #check if anythinga right of 0

solve_puzzle(((3, 2), (1, 0)));
