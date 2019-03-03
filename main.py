#!/usr/bin/python3

import csv
import datetime
import sys
import accounts

entries = []
with open(sys.argv[1], newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in spamreader:
        entries.append(row)

ledger_file = open('ledger-output.dat', 'w+');
for entry in entries:
    for dic_entry in accounts.accounts:
        if dic_entry in entry[1].upper():
            account_out = accounts.accounts[dic_entry]
            break
        else:
            account_out = 'Expenses:Other Payments ';
    date = datetime.datetime.strptime(entry[0], '%d/%m/%Y').date()
    ledger_file.write(str(date.year) + '-' + str(date.month) + '-' + str(date.day))
    if account_out == 'Expenses:Other Payments ':
        ledger_file.write(' ! ')
    else:
        ledger_file.write(' * ')
    ledger_file.write(entry[1])
    ledger_file.write('\n')
    ledger_file.write('    Assets:Bank:Checking ')
    ledger_file.write('  ' + entry[2])
    ledger_file.write('\n')
    ledger_file.write('    ' + account_out + ' ')
    ledger_file.write('\n')
    ledger_file.write('\n')
ledger_file.close()
