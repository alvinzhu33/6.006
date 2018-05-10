def min_votes(districts, c, memo={}):
    '''
    Find minimum votes needed to obtain c electoral counts.
    Input:  list of district tuples containing (population, electoral count)
            for each district, and target electoral count c
    Output: Minimum number of popular votes necessary, or None if not possible
    '''
    if c < 0:
        return None;
    if c==0:
        return 0;
    elif not districts:
        return None;

    i = len(districts)-1;

    if (i, c-districts[i][1]) in memo:
        first = memo[(i,c-districts[i][1])]
    else:
        first = min_votes(districts[:i], c-districts[i][1], memo);
        if first == None:
            first = float("inf");
        else:
            first += districts[i][0]/2;
    if (i, c) in memo:
        second = memo[(i, c)];
    else:
        second = min_votes(districts[:i], c, memo)
        if second == None:
            second = float("inf")
    decision = min(first, second);
    if decision != float("inf"):
        memo[(i, c)] = decision;
    # print(first, second);

    # print(memo)
    if (i, c) in memo and memo[(i, c)]!=float("inf"):
        # if memo[c] == float("inf"):
        #     return None;
        return memo[(i, c)];
    else:
        return None;

print(min_votes([(93635, 2604), (7087, 3108), (64379, 1764), (48761, 3822), (93330, 2100), (37785, 2184), (71978, 1134), (98365, 462), (21939, 2982), (61448, 2058)], 9282));

c = [2604, 3108, 1764, 3822, 2100, 2184, 1134, 462, 2982, 2058]
y=0
for x in range(len(c)):
    y += c[x]
print(y)
