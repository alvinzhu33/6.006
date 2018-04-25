# def catalan(n):
#         catNums = [None]*(n+1);
#         catNums[0] = 1;
#         catNums[1] = 1;
#
#         for counter in range(2, n+1):
#             sum = 0;
#             for i in range(1, counter):
#                 sum += catNums[i]*catNums[counter-i];
#             catNums[counter] = sum
#         return catNums[n];

def choose_prizes(prize_values):
    '''
    Find list of prizes to choose with largest total value
    Input:  list of positive integers corresponding to prize values
    Output: list of indices corresponding to prize values to select
    No two consecutive prize indices should be included
    '''
    prize_total = [None]*len(prize_values);
    prize_total[0] = prize_values[0];
    parent = [None]*len(prize_values);

    parent[0] = None;
    if len(prize_values) == 1:
        return [0];
    before = prize_total[0];
    now = prize_values[1];
    if before > now:
        prize_total[1] = before;
        parent[1] = 0;
    else:
        prize_total[1] = now;
        parent[1] = None;

    index = 0;
    for i in range(2, len(prize_values)):
        before = prize_total[i-1];
        now = prize_values[i]+prize_total[i-2];
        if before >= now:
            prize_total[i] = before;
            parent[i] = i-1
        else:
            prize_total[i] = now;
            parent[i] = i-2
            index = i;

    prizes = []
    while index is not None:
        if index - 1 != parent[index]:
            prizes += [index];
        index = parent[index];

    return prizes;

# print(choose_prizes([1, 4, 5, 5, 1]))
