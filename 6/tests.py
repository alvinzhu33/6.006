import unittest
from solve_puzzle import solve_puzzle

def solved(n, m):
    return tuple(tuple(n * (m - j) - i - 1 for i in range(n)) for j in range(m))

def move(mv, config):
    n, m = len(config[0]), len(config)
    for i in range(n):
        for j in range(m):
            if config[j][i] == 0:
                k, l = i, j
                if   mv == 'U' and j != m - 1:  l = j + 1
                elif mv == 'D' and j != 0:      l = j - 1
                elif mv == 'L' and i != n - 1:  k = i + 1
                elif mv == 'R' and i != 0:      k = i - 1
                else:
                    return None
                return tuple(tuple( 
                        config[j][i] if el == config[l][k] else (
                        config[l][k] if el == config[j][i] else el)
                    for el in row) for row in config)
    raise TypeError('No zero to move configuration')

def check_moves(config, moves):
    if moves is None:
        return True # this case not checked here (would solve your problem set)
    sol = solved(len(config[0]), len(config))
    for mv in moves:
        config = move(mv, config)
    if config == sol:
        return True
    return False

test = (
    ((3, 2), (1, 0)),
    ((1, 0), (2, 3)),
    ((0, 1, 4), (5, 2, 3)),
    ((3, 0, 1), (4, 5, 2)),
    ((0, 4), (5, 3), (1, 2)), 
    ((2, 1), (3, 5), (0, 4)),
    ((8, 7, 6), (2, 5, 4), (1, 0, 3)),
    ((8, 4, 0), (5, 3, 7), (2, 6, 1)), 
    ((15, 14, 0, 12), (11, 10, 13, 8), (7, 6, 9, 4), (3, 2, 5, 1)),
    ((15, 14, 13, 12), (11, 10, 9, 8), (7, 0, 2, 5), (3, 1, 6, 4)),
)

test_solutions = ( # one solving sequence for each (many are possible)
    (),
    ('U', 'R', 'D', 'L', 'U'),
    ('U', 'L', 'D', 'L', 'U'),
    ('R', 'U', 'L', 'L', 'D', 'R', 'R', 'U', 'L', 'L'),
    ('U', 'L', 'U'),
    ('D', 'D', 'L', 'U', 'U', 'R', 'D', 'D', 'L', 'U', 'U', 'R', 'D', 'L', 'U'),
    ('R', 'D', 'L', 'L', 'U'),
    ('U', 'R', 'U', 'L', 'D', 'R', 'D', 'L', 'U', 'U'),
    ('U', 'U', 'U', 'L'),
    ('L', 'U', 'R', 'D', 'L', 'L', 'U'),
)

class TestDecodeMessage(unittest.TestCase):
    def test_01(self):
        self.assertTrue(check_moves(test[0], solve_puzzle(test[0])))
        # self.assertTrue(check_moves(test[0], test_solutions[0]))

    def test_02(self):
        self.assertTrue(check_moves(test[1], solve_puzzle(test[1])))
        # self.assertTrue(check_moves(test[1], test_solutions[1]))

    def test_03(self):
        self.assertTrue(check_moves(test[2], solve_puzzle(test[2])))
        # self.assertTrue(check_moves(test[2], test_solutions[2]))

    def test_04(self):
        self.assertTrue(check_moves(test[3], solve_puzzle(test[3])))
        # self.assertTrue(check_moves(test[3], test_solutions[3]))
       
    def test_05(self):
        self.assertTrue(check_moves(test[4], solve_puzzle(test[4])))
        # self.assertTrue(check_moves(test[4], test_solutions[4]))

    def test_06(self):
        self.assertTrue(check_moves(test[5], solve_puzzle(test[5])))
        # self.assertTrue(check_moves(test[5], test_solutions[5]))

    def test_07(self):
        self.assertTrue(check_moves(test[6], solve_puzzle(test[6])))
        # self.assertTrue(check_moves(test[6], test_solutions[6]))

    def test_08(self):
        self.assertTrue(check_moves(test[7], solve_puzzle(test[7])))
        # self.assertTrue(check_moves(test[7], test_solutions[7]))

    def test_09(self):
        self.assertTrue(check_moves(test[8], solve_puzzle(test[8])))
        # self.assertTrue(check_moves(test[8], test_solutions[8]))
       
    def test_10(self):
        self.assertTrue(check_moves(test[9], solve_puzzle(test[9])))
        # self.assertTrue(check_moves(test[9], test_solutions[9]))

if __name__ == '__main__':
    res = unittest.main(verbosity = 3, exit = False)
