import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
##### TASK 4 #####
""""""""""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""""""""
#####

texters = {phone for text in texts for phone in text[:2]}
call_receivers = {call[1] for call in calls}
marketers = {call[0] for call in calls if call[0] not in texters and call[0] not in call_receivers}

print('These numbers could be telemarketers:')
print('\n'.join(sorted(marketers)))