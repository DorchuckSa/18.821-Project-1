import fib_class
import unittest

class TestFibClass(unittest.TestCase):

    def test_dec_to_fib(self):
        pass

    def test_fib_to_dec(self):
        pass

    # def test_add(self):
    #     ## runs 0 to 20 in 0.24 seconds
    #     ## runs 0 to 100 in 2.971 seconds
    #     ## runs 0 to 500 in 83.810 seconds (with prints)
    #     ## runs 0 to 500 in 57.382 seconds (with no prints)
    #     for bot in range(500):
    #         for top in range(500):
    #             first_fib = fib_class.dec_to_fib(top)
    #             second_fib = fib_class.dec_to_fib(bot)
    #             fib_sol = first_fib + second_fib 
    #             real_sol = top + bot
    #             ## Ensure addition works
    #             self.assertEqual(fib_sol.dec, real_sol)
                
    def test_sub(self):
        ## runs 0 to 20 in 0.025 seconds
        ## runs 0 to 50 in 0.263 seconds
        ## runs 0 to 100 in 1.173 seconds
        ## runs 0 to 250 in 8.637 seconds
        ## runs 0 to 500 in 36.703 seconds - doubling is multiplying by 4 about - checks out
        for bot in range(500):
            for top in range(bot, 500):
                first_fib = fib_class.dec_to_fib(top)
                second_fib = fib_class.dec_to_fib(bot)
                fib_sol = first_fib - second_fib 
                real_sol = top - bot
                ## Ensure subtraction works
                self.assertEqual(fib_sol.dec, real_sol)
    
    def test_mul(self):
        for bot in range(20):
            for top in range(20):
                first_fib = fib_class.dec_to_fib(top)
                second_fib = fib_class.dec_to_fib(bot)
                fib_sol = first_fib * second_fib 
                real_sol = top * bot
                ## Ensure multiplication works
                self.assertEqual(fib_sol.dec, real_sol)        
if __name__ == '__main__':
    unittest.main()
