def getNeighbors(config, x, y):
    neighbors = set([1, 2, 3, 4, 5, 6, 7, 8, 9]);
    for line in config:
        if line[x] != 0 and line[x] in neighbors:
            neighbors.remove(line[x]);
    for bad in config[y]:
        if bad in neighbors:
            neighbors.remove(bad);
    if x < 3:
        xG = 0;
        xE = 3;
    elif x < 6:
        xG = 3;
        xE = 6;
    else:
        xG = 6;
        xE = 9;
    if y < 3:
        yG = 0;
        yE = 3;
    elif y < 6:
        yG = 3;
        yE = 6;
    else:
        yG = 6;
        yE = 9;
    for y in range(yG, yE):
        for x in range(xG, xE):
            if config[y][x] != 0 and config[y][x] in neighbors:
                neighbors.remove(config[y][x]);
#                print(config[y][x])
#    print(x, y, neighbors);
    return list(neighbors);

def nextNeighbor(value, set):
    value += 1;
    while value not in set:
        value += 1;
        if value > 9:
            return;
    return value;
    
def getNext(config, x, y):
    while y < len(config):
        while x < len(config[y]):
            if config[y][x] == 0:
                return (x, y);
            x+=1;
        x=0;
        y+=1;
    return;

def solve_sudoku1(config):
    '''
    Solve input Sudoku puzzle configuration.
    Input:  list of lists corresponding to the rows of a 9 x 9 grid with
            entries 0-9 inclusive (0 corresponding to blank cell)
    Output: list of lists corresponding to the rows of a 9 x 9 grid with
            entries 1-9 inclusive, or None if no solution found
    '''
    zeros = [];
    curZero = getNext(config, 0, 0);
    zeros += [curZero];
    
    while curZero:
        neighbors = getNeighbors(config, curZero[0], curZero[1]);
        nextValue = nextNeighbor(config[curZero[1]][curZero[0]], neighbors);
        print(curZero, neighbors, nextValue);
        print(zeros, curZero);
        if nextValue:
            config[curZero[1]][curZero[0]] = nextValue;
            if zeros[len(curZero)-1] != curZero:
                zeros += [curZero];
            curZero = getNext(config, curZero[0]+1, curZero[1]);
        else:
            config[curZero[1]][curZero[0]] = 0;
            zeros.pop();
            curZero = zeros[len(zeros)-1];
        print(config);
        print();

    return config;

def solve_sudoku(config):
#    print(config)
    for y in range(len(config)):
        for x in range(len(config[0])):
            if config[y][x] == 0:
                neighbors = getNeighbors(config, x, y);
#                print(neighbors);
                #break;
                if len(neighbors) == 0:
                    return None;
                for value in neighbors:
#                    print(value)
                    # print(value, config);
                    copy = [row[:] for row in config];
                    copy[y][x] = value;
                    answer = solve_sudoku(copy);
                    if answer:
                        return answer;
                return None
            #break;
#    print(config)
    #KEEP TRACK OF EVERY ZERO!!
    return config;
#
#print(solve_sudoku([[0,2,0,5,0,1,0,9,0],
#     [8,0,0,2,0,3,0,0,6],
#     [0,3,0,0,6,0,0,7,0],
#     [0,0,1,0,0,0,6,0,0],
#     [5,4,0,0,0,0,0,1,9],
#     [0,0,2,0,0,0,7,0,0],
#     [0,9,0,0,3,0,0,8,0],
#     [2,0,0,8,0,4,0,0,7],
#     [0,1,0,9,0,7,0,6,0]], 0, 0))