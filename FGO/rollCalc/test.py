'''
Created on Jun 7, 2018

@author: TheBorlax
'''
import unittest
from rollCalc.rolls import Core

class TestRolls(unittest.TestCase, Core):
    '''
    classdocs
    '''

    def testMinChance(self):
        self.assertAlmostEqual(self.minChance(1),
                               0.007)
        
        
    def testDistributeOf1(self):
        self.assertEqual(self
                         .distribute(1)
                         .__len__(),
                         2)
        self.assertAlmostEqual(self
                               .distribute(1, 0.1)
                               .get(0),
                               0.9)
        self.assertAlmostEqual(self
                               .distribute(1, 0.1)
                               .get(1),
                               0.1)
        
    def testDistributeOf2(self):
        self.assertEqual(self
                         .distribute(2)
                         .__len__(),
                         3)
        self.assertAlmostEqual(self
                               .distribute(2, 0.1)
                               .get(0),
                               0.81)
        self.assertAlmostEqual(self
                               .distribute(2, 0.1)
                               .get(1),
                               0.18)
        self.assertAlmostEqual(self
                               .distribute(2, 0.1)
                               .get(2),
                               0.01)
        
if __name__ == '__main__':
    unittest.main()
        