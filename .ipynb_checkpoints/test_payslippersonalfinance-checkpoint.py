"""Unittesting for payslippersonalfinance module"""

import unittest
from payslippersonalfinance import PayslipPersonalFinance

class TestPayslipPersonalFinance(unittest.TestCase):
    
    def setUp(self):
        print("setUp")
        self.positive_salary = 29000
        self.negative_salary = -300
        self.zero_salary = 0
        self.str_salary = "test"
        self.pspf = PayslipPersonalFinance(self.positive_salary)
    
    def test_init(self):
        print("test_init")
        self.assertEqual(12500, self.pspf.tax_free_allowance)
        self.assertEqual(0.2, self.pspf.basic_tax_rate)
        self.assertEqual(0.4, self.pspf.higher_tax_rate)
        self.assertEqual(0.45, self.pspf.additional_tax_rate)
        self.assertEqual(50000, self.pspf.upper_tax_threshold)
        self.assertEqual(150000, self.pspf.additional_tax_threshold)
        self.assertEqual(719*12, self.pspf.national_insurance_allowance)
        self.assertEqual(0.12, self.pspf.basic_rate_ni)
        self.assertEqual(0.02, self.pspf.higher_rate_ni)
        self.assertEqual(4167*12, self.pspf.upper_ni_threshold)
        self.assertEqual(25688, self.pspf.sl_repayment_threshold)
        self.assertEqual(0.09, self.pspf.sl_repayment_rate)
        self.assertEqual(0.03, self.pspf.ae_pension_employer_contrib)
        self.assertEqual(0.05, self.pspf.ae_pension_personal_contrib)
        self.assertRaises(TypeError, PayslipPersonalFinance, self.str_salary)
        self.assertRaises(ValueError, PayslipPersonalFinance, self.negative_salary)
    
    def test_tax_calculator(self):
        print("test_tax_calculator")
        self.assertEqual(3300, self.pspf.tax_calculator())
        pspf = PayslipPersonalFinance(self.zero_salary)
        self.assertEqual(0, pspf.tax_calculator())
        

if __name__ == '__main__':
    unittest.main()