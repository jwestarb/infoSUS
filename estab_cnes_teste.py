#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import unittest
from estab_cnes import busca_estab

class TestEstabCnes(unittest.TestCase):

    def test_EstabCnes(self):
        teste = busca_estab('2558246', '420240')
        self.assertEqual(len(teste), 22)

if __name__ == '__main__':
    unittest.main()
