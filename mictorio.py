# coding=utf8

import unittest

def mictorio(mijoes):
    if mijoes is None:
       return []

    mictorios_livres = []
    c = 1
    for i, p in enumerate(mijoes):
        if p == 'o':
            c += 1
            if c == 3:
                mictorios_livres.append(i - 1)
                c = 1
        else:
            c = 0
    if c == 2:
        mictorios_livres.append(len(mijoes) - 1)

    return mictorios_livres

class MictorioTest(unittest.TestCase):
    def test_xoo(self):
        self.assertEqual([2], mictorio('xoo'))
    def test_xoxo(self):
        self.assertEqual([], mictorio('xoxo'))
    def test_x(self):
        self.assertEqual([], mictorio('x'))
    def test_o(self):
        self.assertEqual([0], mictorio('o'))
    def test_xoooo(self):
        self.assertEqual([2,4], mictorio('xoooo'))
    def test_ooxooxoooxxoo(self):
        self.assertEqual([0,7,12], mictorio('ooxooxoooxxoo'))
    def test_ooooooooo(self):
        self.assertEqual([0,2,4,6,8], mictorio('ooooooooo'))
    def test_oxoxoxoxo(self):
        self.assertEqual([], mictorio('oxoxoxoxo'))
    def test_oxoxoxoxoo(self):
        self.assertEqual([9], mictorio('oxoxoxoxoo'))
    def test_null(self):
        self.assertEqual([], mictorio(None))

if __name__ == '__main__':
    unittest.main()
