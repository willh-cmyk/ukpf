"""Unittesting for payslippersonalfinance module"""

import unittest
from payslip import Payslip

class TestPayslip(unittest.TestCase):

    def setUp(self):
        self.salary_names = ['low', 'medium', 'high']
        self.salary = {
            'low': 9000,
            'medium': 29000,
            'high': 45000,
            'negative': -300,
            'string': "test"}
        self.interest = {
            'principal': 2000,
            'rate': 0.02,
            'time': 10}
        self.exp_interest = {
            'simple': 400.0,
            'compound': 437.98883998951464}
        # exp short for expected
        self.exp_tax = {
            'low': 0,
            'medium': 3300,
            'high': 6500}
        self.exp_ni = {
            'low': 44.64,
            'medium': 2444.64,
            'high': 4364.639999999999}
        self.exp_sl = {
            'low': 0,
            'medium': 298.08,
            'high': 1738.08}
        self.exp_ae_pension = {
            'low': 0,
            'medium': 2320.0,
            'high': 3600.0}
        self.exp_comp_interest = {
            'low': 0,
            'medium': 2320.0,
            'high': 3600.0}
        self.exp_simple_interest = {
            'low': 0,
            'medium': 2320.0,
            'high': 3600.0}

    def test_init(self):
        for (key, salary) in self.salary.items():
            if key in self.salary_names:
                pspf = PayslipPersonalFinance(salary)
                self.assertEqual(12500, pspf.tax_free_allowance)
                self.assertEqual(0.2, pspf.basic_tax_rate)
                self.assertEqual(0.4, pspf.higher_tax_rate)
                self.assertEqual(0.45, pspf.additional_tax_rate)
                self.assertEqual(50000, pspf.upper_tax_threshold)
                self.assertEqual(150000, pspf.additional_tax_threshold)
                self.assertEqual(719*12, pspf.national_insurance_allowance)
                self.assertEqual(0.12, pspf.basic_rate_ni)
                self.assertEqual(0.02, pspf.higher_rate_ni)
                self.assertEqual(4167*12, pspf.upper_ni_threshold)
                self.assertEqual(25688, pspf.sl_repayment_threshold)
                self.assertEqual(0.09, pspf.sl_repayment_rate)
                self.assertEqual(0.03, pspf.ae_pension_employer_contrib)
                self.assertEqual(0.05, pspf.ae_pension_personal_contrib)
            elif salary == "test":
                self.assertRaises(TypeError, PayslipPersonalFinance, self.salary['string'])
            elif salary == -300:
                self.assertRaises(ValueError, PayslipPersonalFinance, self.salary['negative'])

    def test_tax_calculator(self):
        for salary_name in self.salary_names:
            pspf = PayslipPersonalFinance(self.salary[salary_name])
            self.assertEqual(self.exp_tax[salary_name], pspf.tax_calculator())

    def test_national_insurance_calculator(self):
        for salary_name in self.salary_names:
            pspf = PayslipPersonalFinance(self.salary[salary_name])
            self.assertEqual(self.exp_ni[salary_name], pspf.national_insurance_calculator())

    def test_student_loan_calculator(self):
        for salary_name in self.salary_names:
            pspf = PayslipPersonalFinance(self.salary[salary_name])
            self.assertEqual(self.exp_sl[salary_name], pspf.student_loan_repayment_calculator())

    def test_autoenrolement_pension(self):
        for salary_name in self.salary_names:
            pspf = PayslipPersonalFinance(self.salary[salary_name])
            self.assertEqual(self.exp_ae_pension[salary_name], pspf.autoenrolement_pension())

    def test_compound_interest_calculator(self):
        for salary_name in self.salary_names:
            pspf = PayslipPersonalFinance(self.salary[salary_name])
            self.assertEqual(self.exp_interest['compound'], pspf.compound_interest_calculator(self.interest['principal'], self.interest['rate'], self.interest['time']))

    def test_simple_interest_calculator(self):
        for salary_name in self.salary_names:
            pspf = PayslipPersonalFinance(self.salary[salary_name])
            self.assertEqual(self.exp_interest['simple'], pspf.simple_interest_calculator(self.interest['principal'], self.interest['rate'], self.interest['time']))


if __name__ == '__main__':
    unittest.main()