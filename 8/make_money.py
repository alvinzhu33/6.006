from math import log;

def make_money(exchange_rate):
    '''
    Find list of currencies to exchange and make money.
    Input:  list of lists corresponding to exchange rates.
    Output: list of currencies (between 0 and n - 1 inclusive)
            starting and ending with currency 0, that is profitable,
            or None if no such sequence exists.
    '''
    d = [[float("inf"), 0]]*len(exchange_rate);
    d[0][0] = 0.0;
    found = 0;
    change = False;

    for relax in range(len(d)):
        for i in range(len(d)):
            for j in range(len(d)):
                # print(i, j, d[i], -log(exchange_rate[i][j]))
                if d[i][0] + -log(exchange_rate[i][j]) < d[j][0]:
                    change = True;
                    d[j] = [d[i][0] + -log(exchange_rate[i][j]), i];
        if not change:
            return None;
    for i in range(len(d)):
        for j in range(len(d)):
            if d[j][0] > d[i][0] + -log(exchange_rate[i][j]):
                found = j;

    cycle = [found];
    foundSet = set();
    cycleSet = set();
    found = d[found][1];
    while found not in cycleSet:
        if found in foundSet:
            cycleSet.add(found);
            cycle += [found];
        else: foundSet.add(found);
        found = d[found][1];
    cycle = cycle[len(cycle)-1:0:-1]
    print(cycle);

    conversion = 1;
    i = 0;
    counter = 0;
    j = cycle[counter];
    path = [];
    while True:
        path += [i];
        conversion = conversion * exchange_rate[i][j];
        if conversion * exchange_rate[j][0] > 1:
            path += [j, 0];
            conversion = conversion * exchange_rate[j][0];
            break;
        i = j;
        counter += 1;
        if counter >= len(cycle):
            counter = counter % len(cycle);
        j = cycle[counter];
    print(path);
    return path
