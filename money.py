# Script for calculating finances
import datetime

# Variables for income, expenses.
income = 1000
constantExpenses = {'fee1': 100, 'fee2': 100, 'fee3': 100,
                    'fee4': 100, 'fee5': 100, 'fee6': 100}
extraExpenses = None
leftOverMoney = None
addmoney = True
moneyAdd = float()

# Add other expenses through extraExpenses, add those values in moneyAdd variable.
while addmoney is True:
    extraExpenses = input('Enter added expense: ')
    if extraExpenses == 'Done':
        addmoney = False
    else:
        moneyAdd += float(extraExpenses)

moneyAdd += sum(constantExpenses.values())

print(income - moneyAdd)

# Convert income minus expenses to string to write to file in documents
string = income - moneyAdd

# Fix user within the open(...) to match your username 

f = open('C:\\Users\\INSERTUSER\\Documents\\MonthlyExpenses', "a")
f.write(str(datetime.date.today()))
f.write('\n')
f.write(str(string))
f.write("\n")
f.close()

