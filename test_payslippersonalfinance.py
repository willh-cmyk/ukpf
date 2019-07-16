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
    
    def test_init(self):
        print("test_init")
        self.assertEqual(12500, self.pspf.tax_free_allowance)
        self.assertEqual(0.2, self.pspf.basic_tax_rate)
        self.assertEqual(0.4, self.pspf.higher_tax_rate)
        self.assertEqual(0.45, self.pspf.additional_tax_rate)
        self.assertEqual(50000, self.pspf.upper_tax_threshold)
#         self.assertEqual(self.pspf.national_insurance_allowance)  # TO DO
        self.assertEqual(0.12, self.pspf.basic_rate_ni)  # Do it for both contracted in and contracted out employees.
        self.assertEqual(0.02, self.pspf.higher_rate_ni)
#         self.assertEqual(, self.upper_ni_threshold)  # Recalculate this for test.
#         self.assertEqual(self.pspf.sl_repayment_threshold)  # To add
    
    def test_tax_calculator(self):
        print("test_tax_calculator")
        self.assertEqual(3300, self.positive_pspf.tax_calculator())
        self.assertEqual(0, self.negative_pspf.tax_calculator())  # Should probably not be the case. Raise an error if a negative salary is given to the class.
        self.assertEqual(0, self.zero_pspf.tax_calculator())
        
#     def test_national_insurance_calculator
        

if __name__ == '__main__':
    unittest.main()