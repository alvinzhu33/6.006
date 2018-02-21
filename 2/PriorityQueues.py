# Heap functions

def parent(i):
    p = (i - 1) // 2
    return p if 0 < i else i

def left(i, n):
    l = 2 * i + 1
    return l if l < n else i

def right(i, n):
    r = 2 * i + 2
    return r if r < n else i

def max_heapify_up(A, n, i):        # O(log i)
    p = parent(i)                   # O(1) index of parent (or i)
    if A[p] < A[i]:                 # O(1) compare
        A[i], A[p] = A[p], A[i]     # O(1) swap parent
        max_heapify_up(A, n, p)     # O(log p) recursive call on parent

def max_heapify_down(A, n, i):      # O(log n - log i)
    l, r = left(i, n), right(i, n)  # O(1) indices of children (or i)
    c = l if A[r] < A[l] else r     # O(1) index of largest child
    if A[i] < A[c]:                 # O(1) compare
        A[i], A[c] = A[c], A[i]     # O(1) swap child
        max_heapify_down(A, n, c)   # O(log n - log c) recursive call on child

def build_max_heap(A, n):
    for i in range(n // 2, -1, -1): # O(n) loop backward over array
        max_heapify_down(A, n, i)   # O(log n - log i)) fix max heap

# Priority Queues

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

class PQ_Array(PriorityQueue):
    def extract_max(self):      # O(n)
        super().extract_max()
        n, A, m = self.n, self.A, self.n
        for i in range(n):
            if A[m] < A[i]:
                m = i
        A[m], A[n] = A[n], A[m]

class PQ_SortedArray(PriorityQueue):
    def insert(self):           # O(n)
        super().insert()
        i, A = self.n - 1, self.A
        while 0 < i and A[i] < A[i - 1]:
            A[i - 1], A[i] = A[i], A[i - 1]
            i -= 1

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

# Array Binary Tree Stringify

def array_tree_str(A, n = None, i = 0):
    if n is None:
        n = len(A)
    if i >= n:
        return ''               # i not in tree
    l = 2 * i + 1               # index of left child
    r = 2 * i + 2               # index of right child
    s = str(A[i])               # convert to string
    if l >= n and r >= n:
        return s                                    # A[i] is leaf
    la = array_tree_str(A, n, l).split('\n')        # recursive call on left
    ra = array_tree_str(A, n, r).split('\n')        # recursive call on right
    wl, cl = len(la[0]), len(la[0].lstrip(' _'))    # location of left child
    wr, cr = len(ra[0]), len(ra[0].rstrip(' _'))    # location of right child
    a = [(' ' * (wl - cl)) + ('_' * cl) + s +       # top line string
         ('_' * cr) + (' ' * (wr - cr))]
    for i in range(max(len(la), len(ra))):          # loop through lower lines
        ls = la[i] if i < len(la) else ''           # line on left
        rs = ra[i] if i < len(ra) else ''           # line on right
        a.append(ls + ' ' * len(s) + rs)            # construct new line
    return '\n'.join(a)                             # join lines together

if __name__ == '__main__':
    # testing sorts
    A = [1,0,9,8,1,5,7,1,4,8,0,1,4,3,8,7,0]
    B = [i for i in A]
    C = [i for i in A]
    print('Original Array A:')
    print(A)
    PQ_Array.sort(A)
    print('\nPQ_Array.sort(A):')
    print(A)
    PQ_SortedArray.sort(B)
    print('\nPQ_SortedArray.sort(A):')
    print(B)
    PQ_Heap.sort(C)
    print('\nPQ_Heap.sort(A):')
    print(C)
    print('\nPretty print heap (sorted array is a min heap!):')
    print(array_tree_str(C))
    C.extract_max();
    print(C);
