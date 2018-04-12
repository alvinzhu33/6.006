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

def solve_sudoku(config):
    '''
    Solve input Sudoku puzzle configuration.
    Input:  list of lists corresponding to the rows of a 9 x 9 grid with
            entries 0-9 inclusive (0 corresponding to blank cell)
    Output: list of lists corresponding to the rows of a 9 x 9 grid with
        entries 1-9 inclusive, or None if no solution found
    '''
    for y in range(len(config)):
        for x in range(len(config[0])):
            if config[y][x] == 0:
                neighbors = getNeighbors(config, x, y);
                if len(neighbors) == 0:
                    return None;
                for value in neighbors:
                    copy = [row[:] for row in config];
                    copy[y][x] = value;
                    answer = solve_sudoku(copy);
                    if answer:
                        return answer;
                return None
    return config;
