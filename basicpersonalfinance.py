"""This is the basic personal finance module for the UK tax system.

This module can be used to calculate the size of contributions for tax, national insurance, pension and student loan.
This module also contains simple helper functions for calculating simple and compound interest.
"""

class BasicPersonalFinance:
    
    def __init__(self, 
                 salary, 
                 tax_free_allowance=12500, 
                 basic_tax_rate=0.2, 
                 higher_tax_rate=0.4,
                 upper_tax_threshold=50000,
                 national_insurance_allowance=8632, 
                 basic_rate_ni=0.12,
                 higher_rate_ni=0.02,
                 upper_ni_threshold=50024,
                 sl_repayment_threshold=25688, 
                 sl_repayment_rate=0.09,
                 ae_pension_employer_contrib=0.03,
                 ae_pension_personal_contrib=0.05):
        self.salary = salary
        self.tax_free_allowance = tax_free_allowance
        self.basic_tax_rate = basic_tax_rate
        self.higher_tax_rate = higher_tax_rate
        self.upper_tax_threshold = upper_tax_threshold
        self.national_insurance_allowance = national_insurance_allowance
        self.basic_rate_ni = basic_rate_ni
        self.higher_rate_ni = higher_rate_ni
        self.upper_ni_threshold = upper_ni_threshold
        self.sl_repayment_threshold = sl_repayment_threshold
        self.sl_repayment_rate = sl_repayment_rate
        self.ae_pension_employer_contrib = ae_pension_employer_contrib
        self.ae_pension_personal_contrib = ae_pension_personal_contrib

    def tax_calculator(self):
        if self.salary <= self.tax_free_allowance:
            self.tax = 0
        if self.salary > self.tax_free_allowance and self.salary <= self.upper_tax_threshold:
            self.tax = (
                (self.salary - self.tax_free_allowance)
                * self.basic_tax_rate
            )
        if self.salary > self.upper_tax_threshold:
            self.tax = (
                (self.upper_tax_threshold - self.tax_free_allowance)
                * self.basic_tax_rate
                + (self.salary - self.upper_tax_threshold)
                * self.higher_tax_rate
            )
        return self.tax
    
    def national_insurance_calculator(self):
        if self.salary <= self.national_insurance_allowance:
            self.national_insurance = 0
        if self.salary > self.national_insurance_allowance and self.salary < self.upper_ni_threshold:
            self.national_insurance = (
                (self.salary - self.national_insurance_allowance)
                * self.basic_rate_ni
            )
        if self.salary >= self.upper_ni_threshold:
            self.national_insurance = (
                (self.upper_ni_threshold - self.national_insurance_allowance)
                * self.basic_rate_ni 
                + (self.salary - self.upper_ni_threshold)
                * self.higher_rate_ni
            )
        return self.national_insurance
        
    def student_loan_repayment_calculator(self):
        if self.salary <= self.sl_repayment_threshold:
            self.student_loan_repayment = 0
        if self.salary > self.sl_repayment_threshold:
            self.student_loan_repayment = (
                (self.salary - self.sl_repayment_threshold)
                * self.sl_repayment_rate
            )
        return self.student_loan_repayment
    
    def autoenrolement_pension(self):
        if self.salary < 10000:
            ae_pension = 0
        else:
            ae_pension = self.salary * (self.ae_pension_employer_contrib + self.ae_pension_personal_contrib)
        return ae_pension
        
#     def house purchase(self,,):
#         pass
    
    @staticmethod
    def compound_interest_calculator(principal, rate, time):
        interest = principal * ((1 + rate)**time - 1)
        return interest
    
    @staticmethod
    def simple_interest_calculator(principal, rate, time):
        interest = principal * rate * time