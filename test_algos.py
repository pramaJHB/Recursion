import unittest
import super_algos

class MyTestAlgos(unittest.TestCase):
    def test_find_min(self):
        self.assertEqual(super_algos.find_min([3, 3, 2, 9, 5, 2]), 2)
        self.assertEqual(super_algos.find_min([2, 3, 1, -9, 5, 2]), -9)
        self.assertEqual(super_algos.find_min([0, 0, 0, 0]), 0)
        self.assertEqual(super_algos.find_min([4, 8 , -12, 'hello', 1, 'w', 6]), -1)
        self.assertEqual(super_algos.find_min([]), -1)
        self.assertEqual(super_algos.find_min([7, 3, '', 12, 4]), -1)
        self.assertEqual(super_algos.find_min([5, 18, 99, 1.618, 9.5]), -1)
        self.assertEqual(super_algos.find_min('qwerty'), -1)


    def test_sum_all(self):
        self.assertEqual(super_algos.sum_all([2, 7, 4, 12]), 25)
        self.assertEqual(super_algos.sum_all([2, -7, -4, 12]), 3)
        self.assertEqual(super_algos.sum_all([0, 0, 0, 0]), 0)
        self.assertEqual(super_algos.sum_all([2, 7, 'h', 4, 'world']), -1)
        self.assertEqual(super_algos.sum_all([]), -1)
        self.assertEqual(super_algos.sum_all([3, 5, 2.5, 10.25]), -1)
        self.assertEqual(super_algos.sum_all(True), -1)


    def test_find_possible_strings(self):
        self.assertEqual(super_algos.find_possible_strings(['a', 'b'], 2), ['aa', 'ab', 'ba', 'bb'])
        self.assertEqual(super_algos.find_possible_strings(['h', 'w'], 2), ['hh', 'hw', 'wh', 'ww'])
        self.assertEqual(super_algos.find_possible_strings(['a', 'b'], 3), ['aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb'])
        self.assertEqual(super_algos.find_possible_strings(['x', 'y', 'z'], 2), ['xx', 'xy', 'xz', 'yx', 'yy', 'yz', 'zx', 'zy', 'zz'])
        self.assertEqual(super_algos.find_possible_strings(['x', 'X'], 3), ['xxx', 'xxX', 'xXx', 'xXX', 'Xxx', 'XxX', 'XXx', 'XXX'])
        self.assertEqual(super_algos.find_possible_strings(['o'], 5), ['ooooo'])
        self.assertEqual(super_algos.find_possible_strings(['w', 't', 'c'], 1), ['w', 't', 'c'])
        self.assertEqual(super_algos.find_possible_strings(['ab', 'c'], 2), ['abab', 'abc', 'cab', 'cc'])
        self.assertEqual(super_algos.find_possible_strings(['w', 't', 'c'], 3), ['www', 'wwt', 'wwc', 'wtw', 'wtt', 'wtc', 'wcw', 'wct', 'wcc', \
                                                                                'tww', 'twt', 'twc', 'ttw', 'ttt', 'ttc', 'tcw', 'tct', 'tcc', \
                                                                                'cww', 'cwt', 'cwc', 'ctw', 'ctt', 'ctc', 'ccw', 'cct', 'ccc'])
        self.assertEqual(super_algos.find_possible_strings(['a', 4, 'c'], 2), [])
        self.assertEqual(super_algos.find_possible_strings([], 4), [])
        self.assertEqual(super_algos.find_possible_strings(17, 2), [])
        self.assertEqual(super_algos.find_possible_strings(['a', 'b'], 0), [])


if __name__ == '__main__':
    unittest.main()
