"""Unittesting for payslippersonalfinance module"""

import unittest
from payslippersonalfinance import PayslipPersonalFinance

class TestPayslipPersonalFinance(unittest.TestCase):
    
    def setUp(self):
        print("setUp")
        positive_salary = 29000
        negative_salary = -300
        zero_salary = 0
        self.positive_pspf = PayslipPersonalFinance(positive_salary)
        self.negative_pspf = PayslipPersonalFinance(negative_salary)
        self.zero_pspf = PayslipPersonalFinance(zero_salary)
    
    def test_tax_calculator(self):
        print("test_tax_calculator")
        self.assertEqual(3300, self.positive_pspf.tax_calculator())
        self.assertEqual(0, self.negative_pspf.tax_calculator())  # Should probably not be the case. Raise an error if a negative salary is given to the class.
        self.assertEqual(0, self.zero_pspf.tax_calculator())
        
#     def test_national_insurance_calculator
        

if __name__ == '__main__':
    unittest.main()