def min_votes(districts, c, memo={}):
    '''
    Find minimum votes needed to obtain c electoral counts.
    Input:  list of district tuples containing (population, electoral count)
            for each district, and target electoral count c
    Output: Minimum number of popular votes necessary, or None if not possible
    '''
    if c < 0:
        return float("inf");
    if c==0:
        return 0;
    elif not districts:
        return float("inf");

    i = len(districts)-1;
    if (i, c-districts[i][1]) in memo:
        first = memo[(i,c-districts[i][1])]
    else:
        first = districts[i][0]/2 + min_votes(districts[:len(districts)-1], c-districts[i][1], memo);
    if (i, c) in memo:
        second = memo[(i, c)];
    else:
        second = min_votes(districts[:len(districts)-1], c, memo)
    decision = min(first, second);
    memo[(i, c)] = decision;

    # print(memo)
    if memo[(i, c)]:
        # if memo[c] == float("inf"):
        #     return None;
        return memo[(i, c)];

print(min_votes([(61882, 66), (38066, 153), (70731, 30), (91363, 198), (56869, 276)], 66+153));
