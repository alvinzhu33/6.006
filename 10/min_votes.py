def min_votes(districts, c):
    '''
    Find minimum votes needed to obtain c electoral counts.
    Input:  list of district tuples containing (population, electoral count)
            for each district, and target electoral count c
    Output: Minimum number of popular votes necessary, or None if not possible
    '''
    i = len(districts)-1;
    memo = {};

    min_votes_rec(districts, i, c, memo);

    # if (i, c-districts[i][1]) in memo:
    #     first = memo[(i,c-districts[i][1])]
    # else:
    #     first = min_votes(districts[:i], c-districts[i][1], memo);
    #     if first == None:
    #         first = float("inf");
    #     else:
    #         if first % 2 == 0:
    #             first += districts[i][0]/2 + 1;
    #         else:
    #             first += districts[i][0]/2 + .5
    # if (i, c) in memo:
    #     second = memo[(i, c)];
    # else:
    #     second = min_votes(districts[:i], c, memo)
    #     if second == None:
    #         second = float("inf")
    # decision = min(first, second);
    # if decision != str("inf"):
    #     memo[(i, c)] = decision;

    print(memo)
    if (i, c) in memo and memo[(i,c)]!=float("inf"):
        return memo[(i, c)];
    else:
        return None;

def min_votes_rec(districts, i, j, memo):
    if j < 0:
        return None;
    if j == 0:
        return 0;
    if i < 0:
        return None;

    if (i-1, j-districts[i][1]) in memo:
        first = memo[(i-1, j-districts[i][1])];
    else:
        first = min_votes_rec(districts, i-1, j-districts[i][1], memo)
    if first == None:
        first = float("inf");
    else:
        if first % 2 == 0:
            first += districts[i][0]/2 + 1;
        else:
            first += districts[i][0]/2 + .5;
    if (i-1, j) in memo:
        second = memo[(i-1, j)]
    else:
        second = min_votes_rec(districts, i-1, j, memo);
    if second == None:
        second = float("inf");
    memo[(i, j)] = min(first, second);

    return memo[(i, j)];
