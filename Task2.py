import csv
import operator

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

#### TASK 2 ####
"""""""""""""""
TASK 2: Which telephone number spent the longest time on the phone
during the period?
Don't forget that time spent answering a call is also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""""
####
d = {}
for call in calls:
    for phone in call[:2]:
        d[phone] = d.get(phone, 0) + int(call[3])
longest_call_duration = max(d.items(), key=operator.itemgetter(1))

print(longest_call_duration[0], 'spent the longest time,', longest_call_duration[1],
    'seconds, on the phone during September 2016.')
