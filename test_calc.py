import unittest
import calc

class testCaseAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        
class testCaseSub(unittest.TestCase):
    def test_sub(self):
        self.assertEqual(calc.sub(10,5), 5)
        
class testCaseMul(unittest.TestCase):
    def test_mul(self):
        self.assertEqual(calc.mul(10,5), 50)

class testCaseDiv(unittest.TestCase):
    def test_div(self):
        self.assertEqual(calc.div(10,5), 2)
        
if __name__ == '__main__':
    unittest.main()
    
