import sys
import math

args = sys.argv

if ('--type=annuity' not in args) and ('--type=diff' not in args):
    print("Incorrect parameters")
    exit()
elif '--type=annuity' in args:
    cal_type = 'annuity'
elif '--type=diff' in args:
    cal_type = 'diff'
    for x in args:
        if '--payment' in x:
            print("Incorrect parameters")
            exit()

if len(args) != 5:
    print("Incorrect parameters")
    exit()

a = 0
for x in args:
    if '--interest' in x:
        a += 1
if a != 1:
    print("Incorrect parameters")
    exit()

P = 0
A = 0
i = 0
n = 0    

for x in args:
        
    if '--principal' in x:
        principal = x.split('=')
        P = int(principal[1])
        if P < 0:
            print("Incorrect parameters")
            exit()
        
    elif '--payment' in x:
        payment = x.split('=')
        A = int(payment[1])
        if A < 0:
            print("Incorrect parameters")
            exit()
    
    elif '--interest' in x:
        interest = x.split('=')
        i_percent = float(interest[1])
        i = i_percent / 12 / 100
        if i < 0:
            print("Incorrect parameters")
            exit()

    elif '--periods' in x:
        periods = x.split('=')
        n = int(periods[1])
        if n < 0:
            print("Incorrect parameters")
            exit()

if cal_type == 'diff':

    total_pay = 0

    for m in range(1, n+1):
        result = math.ceil(P/n + i * (P - (P*(m-1))/n))
        total_pay += result
        print(f'Month {m}: paid out {result}')   
    
    over_pay = total_pay - P
    print()
    print(f'Overpayment = {over_pay}')

else:
    b = 0
    for x in args:
        if '--payment' in x:
            b += 1
    if b == 0:
        x = pow(1 + i, n)
        A = math.ceil(((i * x) / (x - 1)) * P)
        over_pay = A * n - P
        print(f'Your annuity payment = {A}!')
        print(f'Overpayment = {over_pay}')
    
    c = 0
    for x in args:
        if '--principal' in x:
            c += 1
    if c == 0:
        x = pow(1 + i, n)
        P = math.floor(A / ((i * x) / (x - 1)))
        over_pay = A * n - P
        print(f'Your credit principal = {P}!')
        print(f'Overpayment = {over_pay}')

    d = 0
    for x in args:
        if '--periods' in x:
            d += 1
    if d == 0:
        x = A / (A - i * P)
        n = math.ceil(math.log(x, 1 + i))
        
        year = math.floor(n / 12)
        over_pay = year * A * 12 - P
        
        if year == 1:
            print('You need 1 year to repay this credit!')
        else:
            print(f'You need {year} years to repay this credit!')
        
        print(f'Overpayment = {over_pay}')