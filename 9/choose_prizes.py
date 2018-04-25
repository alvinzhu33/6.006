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
        else:
            prize_total[i] = [now, prize_total[i-2][1]+[i]];
#        print(prize_values)
        # print(prize_total[i])
#        print()

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
    return prize_total[len(prize_values)-1][1];

# y = [753, 130, 544, 863, 81, 421, 856, 695, 436, 749, 451, 464, 499, 827, 550, 131, 385, 555, 363, 616, 951, 849, 541, 803, 254, 323, 587, 478, 461, 177, 710, 82, 81, 595, 757, 765, 806, 216, 82, 701, 88, 293, 378, 289, 860, 35, 338, 797, 795, 264, 994, 613, 244, 464, 155, 440, 40, 496, 544, 732, 345, 353, 822, 76, 374, 502, 355, 588, 857, 478, 295, 432, 20, 642, 107, 72, 22, 415, 567, 988, 759, 34, 190, 521, 820, 638, 141, 269, 371, 217, 446, 156, 519, 593, 511, 514, 514, 328, 265, 981, 558, 290, 926, 834, 5, 521, 122, 64, 505, 400, 954, 61, 731, 854, 149, 62, 952, 832, 232, 438, 531, 999, 621, 881, 24, 856, 697, 60, 322, 390, 969, 559, 581, 104, 572, 24, 789, 846, 190, 337, 563, 298, 856, 964, 239, 908, 879, 75, 320, 858, 509, 44, 455, 223, 526, 838, 893, 731, 299, 942, 105, 255, 583, 972, 333, 341, 140, 357, 882, 457, 427, 561, 553, 815, 240, 959, 834, 243, 334, 179, 446, 14, 125, 368, 173, 204, 112, 435, 898, 418, 217, 995, 631, 706, 75, 883, 863, 15, 96, 548, 842, 158, 306, 655, 281, 356, 316, 157, 224, 279, 201, 845, 899, 475, 894, 87, 14, 919, 45, 649, 138, 533, 238, 672, 974, 674, 818, 751, 734, 178, 399, 935, 982, 229, 531, 919, 337, 301, 82, 503, 727, 919, 426, 94, 472, 718, 660, 703, 826, 65, 293, 996, 121, 282, 726, 671]
# x = choose_prizes(y);
# print();
# print(x);
# print(len(y));
# sum = 0;
# for i in x:
#     sum += y[i];
# print(sum);
