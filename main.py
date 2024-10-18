import pandas as pd
from sympy import Poly, symbols

class Bisection:
    global x
    x = symbols("x")
    
    def __init__(self, expr: str) -> None:
        self.expr = expr
    
    def eq_coeff(self) -> list:
        coef = Poly(self.expr, x)
        return coef.all_coeffs()

    def calc_func(self, n) -> int:
        order = len(Bisection(self.expr).eq_coeff()) - 1
        k = 0
        for i in Bisection(self.expr).eq_coeff():
            k += i * n ** order
            order -= 1
        
        return k

    def bisection(self, intervals: list, k = 10):
        data = []
        
        if k < 0:
            return "please enter positive n"
        
        else:
            
            # data for first iteration
            a_1 = intervals[0]
            b_1 = intervals[1]
            m_n = (intervals[0] + intervals[1]) / 2
            h_n = (intervals[1] - intervals[0]) / 2
            
            for n in range(1, k + 1):
            
                if n == 1:
                    f_m_n = round(Bisection(self.expr).calc_func(m_n), 3)
                    f_m_a = round(Bisection(self.expr).calc_func(a_1), 3)
                    
                    mul = round(f_m_a * f_m_n)
                    m_n = (a_1 + b_1) / 2
                    h_n = (b_1 - a_1) / 2
                    
                    if f_m_n * f_m_a < 0:
                        a_n = a_1
                        b_n = m_n
                    else:
                        a_n = m_n
                        b_n = b_1
                    
                    data.append([n, a_1, b_1, h_n, m_n, f_m_a, f_m_n, mul])
                    
                    if f_m_n == 0:
                        break
                    
                    continue
                        
                m_n = (a_n + b_n) / 2
                
                f_m_n = round(Bisection(self.expr).calc_func(m_n), 7)
                f_m_a = round(Bisection(self.expr).calc_func(a_n), 7)
                
                mul = round(f_m_a * f_m_n, 5)
                
                h_n = round((b_n - a_n) / 2, 5)
                
                data.append([n, a_n, b_n, h_n, m_n, f_m_a, f_m_n, mul])
                
                
                if f_m_n * f_m_a < 0:
                    a_n = a_n
                    b_n = m_n
                else:
                    a_n = m_n
                    b_n = b_n

        key = {
            "n" : [i[0] for i in data],
            "a_n" : [i[1] for i in data],
            "b_n" : [i[2] for i in data],
            "h_n" : [i[3] for i in data],
            "m_n" : [i[4] for i in data],
            "f_m_a" : [i[5] for i in data],
            "f_m_n" : [i[6] for i in data],
            "f_m_a * f_m_n" : [i[7] for i in data]
        }
        
        df = pd.DataFrame(key)
        return df 
                    

expr = x**3 - 3 * x - 5
obj = Bisection(expr).bisection([2, 3], k=20)
print(obj)
