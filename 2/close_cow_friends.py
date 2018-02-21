def parent(i):
    p = (i - 1) // 2
    return p if 0 < i else i

def left(i, n):
    l = 2 * i + 1
    return l if l < n else i

def right(i, n):
    r = 2 * i + 2
    return r if r < n else i

def distance(x, y):
    return (x**2+y**2)**.5;

def max_heapify_up(A, n, i):        # O(log i)
    p = parent(i)                   # O(1) index of parent (or i)
    if distance(A[p][0],A[p][1]) < distance(A[i][0],A[i][1]):                 # O(1) compare
        A[i], A[p] = A[p], A[i]     # O(1) swap parent
        max_heapify_up(A, n, p)     # O(log p) recursive call on parent

def max_heapify_down(A, n, i):      # O(log n - log i)
    l, r = left(i, n), right(i, n)  # O(1) indices of children (or i)
    c = l if distance(A[r][0],A[r][1]) < distance(A[l][0],A[l][1]) else r     # O(1) index of largest child
    if distance(A[i][0],A[i][1]) < distance(A[c][0],A[c][1]):                 # O(1) compare
        A[i], A[c] = A[c], A[i]     # O(1) swap child
        max_heapify_down(A, n, c)   # O(log n - log c) recursive call on child

class PriorityQueue:
    def __init__(self, A):
        self.n, self.A = 0, A

    def insert(self):
        if not self.n < len(self.A):
            raise IndexError('insert into full priority queue')
        self.n = self.n + 1

    def extract_max(self):
        if self.n < 0:
            raise IndexError('pop from empty priority queue')
        self.n = self.n - 1

    @classmethod
    def sort(cls, A):
        pq = cls(A)
        n = len(A)
        for i in range(n):
            pq.insert()         # n x T_i
        for i in range(n):
            pq.extract_max()    # n x T_e

class PQ_Heap(PriorityQueue):
    def insert(self):           # O(log n)
        super().insert()
        n, A = self.n, self.A
        max_heapify_up(A, n, n - 1)

    def extract_max(self):      # O(log n)
        super().extract_max()
        n, A = self.n, self.A
        A[0], A[n] = A[n], A[0]
        max_heapify_down(A, n, 0)

def close_cow_friends(locations, g):
    '''
    Return g locations closest to origin in increasing order.
    Input:  locations | generator of location tuples (x, y)
            g         | number locations to return
    '''
    invites = [];
    sortedInvites = PQ_Heap(invites);
    for index in range(g):
        invites.append(locations[index]);
        sortedInvites.insert();
    print("Sorted:", invites);
    for index in range(g, len(locations)):
        # print(locations[index], distance(locations[index][0], locations[index][1]));
        # print(invites[0], distance(invites[0][0], invites[0][1]));
        if distance(locations[index][0], locations[index][1]) < distance(invites[0][0], invites[0][1]):
            invites[0] = locations[index];
            max_heapify_down(invites, g, 0);
    PQ_Heap.sort(invites);
    return invites;

print([(-3.085938209482254, -35.51086598631448), (26.993450139920384, 0.8331111535179057), (18.498724377558744, 30.754288731062978), (6.608602405714086, 29.946996046275647), (-6.474375132714367, 11.891001424902061), (2.6030415461917915, -23.33983716414429), (20.043810572570063, -34.85060665721733), (23.528508854561295, -2.4642560026968043), (-38.75851406006202, 14.135701382849792), (-25.728316581837667, -26.455843842973806)], 5);
print(close_cow_friends([(2.7, 8.3), (-1.7, -3.0), (3.4, 5.6), (1.2, 3.4), (10.8, -17.4)], 3));
