import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

#### TASK 1 ####
"""""""""""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""""
####
print('There are', len(set([phone for record in (texts + calls) for phone in record[:2]])),
    'different telephone numbers in the records.')