import unittest
from sort_anagrams import sort_anagrams

tests = (
['ate', 'dog', 'eat', 'god', 'tea'],
['remain', 'rental', 'sale', 'scare', 'seal',
  'tabu', 'tap', 'treadle', 'tuba', 'wane', 'wean'],
['leas', 'ales', 'aligned', 'allergy', 'alter',
  'altered', 'amen', 'anew', 'angel', 'angle',
  'antler', 'beat', 'beats', 'beta', 'betas',
  'came', 'care', 'cares'],
['abed', 'abet', 'abets', 'abut', 'acme', 'acre',
  'largely', 'later', 'leading', 'learnt', 'leas',
  'mace', 'mane', 'marine', 'mean', 'name', 'pat',
  'race', 'races', 'recasts', 'regally', 'related',
  'remain', 'rental', 'sale', 'scare', 'seal',
  'tabu', 'tap', 'treadle', 'tuba', 'wane', 'wean'],
['abed', 'abet', 'abets', 'abut', 'acme', 'acre',
  'acres', 'actors', 'actress', 'airmen', 'alert',
  'alerted', 'ales', 'aligned', 'allergy', 'alter',
  'altered', 'amen', 'anew', 'angel', 'angle',
  'antler', 'apt', 'bade', 'baste', 'bead',
  'beast', 'beat', 'beats', 'beta', 'betas',
  'came', 'care', 'cares', 'casters', 'castor',
  'costar', 'dealing', 'gallery', 'glean',
  'largely', 'later', 'leading', 'learnt', 'leas',
  'mace', 'mane', 'marine', 'mean', 'name', 'pat',
  'race', 'races', 'recasts', 'regally', 'related',
  'remain', 'rental', 'sale', 'scare', 'seal',
  'tabu', 'tap', 'treadle', 'tuba', 'wane', 'wean'])

test_answers = (
['dog', 'god', 'ate', 'eat', 'tea'],
['tap', 'wane', 'wean', 'sale', 'seal',
 'rental', 'remain', 'treadle', 'scare', 'tabu', 'tuba'],
['anew', 'amen', 'leas', 'ales', 'alter', 'antler', 'angel', 'angle',
 'allergy', 'aligned', 'altered', 'care', 'cares', 'came', 'beat',
 'beta', 'beats', 'betas'],
['pat', 'tap', 'wane', 'wean', 'mane', 'mean', 'name', 'leas',
 'sale', 'seal', 'later', 'learnt', 'rental', 'marine', 'remain',
 'largely', 'regally','leading', 'related', 'treadle', 'acre',
 'race', 'races', 'scare', 'recasts', 'acme', 'mace', 'abut',
 'tabu', 'tuba', 'abet', 'abets', 'abed'],
['apt', 'pat', 'tap', 'anew', 'wane', 'wean', 'amen', 'mane',
 'mean', 'name', 'ales', 'leas', 'sale', 'seal', 'alert', 'alter',
 'later', 'antler', 'learnt', 'rental', 'airmen', 'marine', 'remain',
 'angel', 'angle', 'glean', 'allergy', 'gallery', 'largely', 'regally',
 'aligned', 'dealing', 'leading', 'alerted', 'altered', 'related',
 'treadle', 'actors', 'castor', 'costar', 'acre', 'care', 'race',
 'acres', 'cares', 'races', 'scare', 'actress', 'casters', 'recasts',
 'acme', 'came', 'mace', 'abut', 'tabu', 'tuba', 'abet', 'beat',
 'beta', 'abets', 'baste', 'beast', 'beats', 'betas', 'abed', 'bade', 'bead'])

def check_correct(A, ans):
    return sort_anagrams(A) == ans

class TestSortAnagrams(unittest.TestCase):
    def test_01(self):
        self.assertTrue(check_correct(tests[0], test_answers[0]))

    def test_02(self):
        self.assertTrue(check_correct(tests[1], test_answers[1]))

    def test_03(self):
        self.assertTrue(check_correct(tests[2], test_answers[2]))

    def test_04(self):
        self.assertTrue(check_correct(tests[3], test_answers[3]))
       
    def test_05(self):
        self.assertTrue(check_correct(tests[4], test_answers[4]))

if __name__ == '__main__':
   res = unittest.main(verbosity = 3, exit = False)
