#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 19:34:42 2025

@author: monicaguevara
"""

#a

Updatedbalanceeachmonth = balance
Monthlyinterestrate = annualInterestRate/12.0
for i in range(12):
    Minimummonthlypayment = monthlyPaymentRate * Updatedbalanceeachmonth
    Monthlyunpaidbalance = Updatedbalanceeachmonth - Minimummonthlypayment
    Interest = Monthlyinterestrate *  Monthlyunpaidbalance
    Updatedbalanceeachmonth = Monthlyunpaidbalance + Interest
        # print('Month', (i+1), 'Remaining balance is:', round(Updatedbalanceeachmonth, 2))
print('Remaining balance is:', round(Updatedbalanceeachmonth,2))



#b
Updatedbalanceeachmonth = balance
Minimummonthlypayment = 10
while Updatedbalanceeachmonth >= 0:
    Updatedbalanceeachmonth = balance
    Monthlyinterestrate = annualInterestRate/12.0
    Minimummonthlypayment += 10
    for i in range(12):
        Monthlyunpaidbalance = Updatedbalanceeachmonth - Minimummonthlypayment
        Interest = Monthlyinterestrate *  Monthlyunpaidbalance
        Updatedbalanceeachmonth = Monthlyunpaidbalance + Interest
print('Lowest Payment:', Minimummonthlypayment)


#c
Updatedbalanceeachmonth = balance
Monthlyinterestrate = annualInterestRate/12.0
Lower_Minimummonthlypayment = balance/12
Upper_Minimummonthlypayment = (balance * (1 + Monthlyinterestrate)**12)/12
Minimummonthlypayment = (Lower_Minimummonthlypayment + Upper_Minimummonthlypayment)/2
while abs(Updatedbalanceeachmonth) >= 0.01:
    Updatedbalanceeachmonth = balance
    for i in range(12):
        Monthlyunpaidbalance = Updatedbalanceeachmonth - Minimummonthlypayment
        Interest = Monthlyinterestrate *  Monthlyunpaidbalance
        Updatedbalanceeachmonth = Monthlyunpaidbalance + Interest
    if Updatedbalanceeachmonth > 0:
        Lower_Minimummonthlypayment = Minimummonthlypayment
    else:
        Upper_Minimummonthlypayment = Minimummonthlypayment
    Minimummonthlypayment = ((Lower_Minimummonthlypayment + Upper_Minimummonthlypayment)/2)
print('Lowest Payment:', round(Minimummonthlypayment, 2))

