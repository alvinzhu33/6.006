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
    prize_total[0] = [prize_values[0], [0]]
    if len(prize_values) == 1:
        return prize_total[0][1];
    before = prize_total[0][0];
    now = prize_values[1];
    if before > now:
        prize_total[1] = [before, [0]];
    else:
        prize_total[1] = [now, [1]];

    parent = [None]*len(prize_values);
    parent[0] = 0
    parent[1] = prize_total[1][1][0]

#    print(prize_values)
#    print(prize_total)
#    print()
    for i in range(2, len(prize_values)):
#        print(i, prize_values[i])
        before = prize_total[i-1][0];
        now = prize_values[i]+prize_total[i-2][0];
#        print(before, now)
        if before > now:
            prize_total[i] = [before, prize_total[i-1][1]];
            parent[i] = i-1
        else:
            prize_total[i] = [now, prize_total[i-2][1]+[i]];
            parent[i] = i-2
#        print(prize_values)
        # print(prize_total[i])
#        print()
    # print(parent)

    index = 0;
    for i in range(1, len(prize_values)):
        if prize_total[index][0] < prize_total[i][0]:
            index = i
    prizes = []
    # flag = True;
    while index:
        # if flag:
        #     print(index, parent[index], len(parent), len(prize_total))
        #     flag = False
        if index - 1 != parent[index]:
            prizes += [index];
        index = parent[index];
    prizes += [index]
    # print(prizes)
#    prizes = [];
#    print(prize_values[len(prize_total)-2])
#    if prize_total[len(prize_total)-1][1] == len(prize_total)-2:
#        prizes += [prize_values[len(prize_total)-2]];
#        parent = prize_total[len(prize_total)-2][1];
#    else:
#        prizes += [prize_values[len(prize_total)-1]];
#        parent = prize_values[len(prize_total)-1][1];
#    while parent:
#        if prize_total[parent][1] == (prize_total[prize_total[parent][1]][1] + 1):
#            parent = prize_total[prize_total[parent][1]][1]
#        prizes += [prize_values[parent]];
#        parent = prize_total[parent][1];

#    print("hello", prizes);
    # print(prize_total[len(prize_values)-1][0])
    # print(prizes)
    # print(prize_total[len(prize_values)-1][1])
    # print()
    return prizes;

# choose_prizes([14, 30, 27, 4, 5, 15, 1])
