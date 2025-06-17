import unittest
from operaciones_comparacion import es_mayor_que, es_menor_que, es_menor_o_igual_que, es_mayor_o_igual_que, son_iguales

class TestOperacionesComparacion (unittest.TestCase):
    
    def test_es_mayor_que(self):
        self.assertGreater(es_mayor_que(5,3), 0)
        self.assertTrue(es_mayor_que(10,5))
        
        self.assertFalse(es_mayor_que(3,5))
        self.assertFalse(es_mayor_que(-8,-8))
        
    def test_es_menor_que(self):
        
        self.assertLess(es_menor_que(3, 5), 2)
        self.assertTrue(es_menor_que(0,1))
        
        self.assertFalse(es_menor_que(10,3))
        self.assertFalse(es_menor_que(1,1))
        
    def test_es_mayor_o_igual_que(self):
        
        self.assertTrue(es_mayor_o_igual_que(24, 3))
        self.assertTrue(es_mayor_o_igual_que(10, 10))

        self.assertGreaterEqual(es_mayor_o_igual_que(7, 7), 0)
        self.assertFalse(es_mayor_o_igual_que(3, 5))
        
    def test_es_menor_o_igual_que(self):
        
        self.assertTrue(es_menor_o_igual_que(4, 9))
        self.assertTrue(es_menor_o_igual_que(9, 9))
        self.assertLessEqual(es_menor_o_igual_que(2, 2), 1)
        self.assertFalse(es_menor_o_igual_que(23, 22))
        
    def test_son_iguales(self):
        self.assertTrue(son_iguales(7, 7))
        self.assertEqual(son_iguales(10, 10), True)
                         
        self.assertFalse(son_iguales(7, 6))
        self.assertEqual(son_iguales(1, -7), False)
        
if __name__ == '__main__':
     unittest.main()