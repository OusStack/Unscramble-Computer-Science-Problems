### Unscramble Computer Science Problems

## Project Overview
In this project, you will complete five tasks based on a fabricated set of calls and texts exchanged during September 2016. 
You will use Python to analyze and answer questions about the texts and calls contained in the dataset. Lastly, you will 
perform run time analysis of your solution and determine its efficiency.

## What will I learn?
In this project, you will:

- Apply your Python knowledge to breakdown problems into their inputs and outputs.
- Perform an efficiency analysis of your solution.
- Warm up your Python skills for the course.

## Why this Project?
with this tasks You'll apply the skills you've learned so far in a more realistic scenario. The five tasks are structured to give you 
experience with a variety of programming problems. You will receive code review of your work; this personal feedback 
will help you to improve your solutions.

## Step 1 - Download the Files
Download and open the zipped folder here. Inside the folder you will find a five python files Task0.py, Task1.py, ...,Task4.py 
and two csv files calls.csv and texts.csv

## About the data
The text and call data are provided in csv files.

The text data (text.csv) has the following columns: sending telephone number (string), 
receiving telephone number (string), timestamp of text message (string).

The call data (call.csv) has the following columns: calling telephone number (string), 
receiving telephone number (string), start timestamp of telephone call (string), 
duration of telephone call in seconds (string)

All telephone numbers are 10 or 11 numerical digits long. Each telephone number starts with a code indicating the 
location and/or type of the telephone number. There are three different kinds of telephone numbers, 
each with a different format:

- Fixed lines start with an area code enclosed in brackets. The area codes vary in length but always begin with 0. 
Example: "(022)40840621".
- Mobile numbers have no parentheses, but have a space in the middle of the number to help readability. 
The mobile code of a mobile number is its first four digits and they always start with 7, 8 or 9. Example: "93412 66159".
- Telemarketers' numbers have no parentheses or space, but start with the code 140. Example: "1402316533".

## Step 2 - Implement the Code
Complete the five tasks (Task0.py, Task1.py, ...,Task4.py). Do not change the data or instructions, simply add your code 
below what has been provided. Include all the code that you need for each task in that file.

The solution outputs for each file should be the print statements described in the instructions. Feel free to use other 
print statements during the development process, but remember to remove them for submission - the submitted files should 
print only the solution outputs.

## Step 3 - Calculate Big O
Once you have completed your solution for each problem, perform a run time analysis (Worst Case Big-O Notation) of your 
solution. Document this for each problem and include this in your submission.

## Step 4 - Check again Rubric and Submit
Use the rubric to check your work before submission. A Udacity Reviewer will give feedback on your work based on this 
rubric and will leave helpful comments on your code.

## Solution 3. Big O Calculation Analysis

#### Task 0 - O(1)
Always gonna take the same amount of time
```
print(texts[0][0], 'texts', texts[0][1], 'at time', texts[0][2])
print(calls[-1][0], 'calls', calls[-1][1], 'at time', calls[-1][2], 'lasting', calls[-1][3], 'seconds')
```

#### Task 1 - O(n)
There is 1 for loop iterating over records object (texts + calls)
```
print('There are', len(set([phone for record in (texts + calls) for phone in record[:2]])),'different telephone numbers in the records.')
```

#### Task 2 - O(n)
There is 1 for loop iterating over calls object
```
d = {}
for call in calls:
    for phone in call[:2]:
        d[phone] = d.get(phone, 0) + int(call[3])
longest_call_duration = sorted(d.items(), key=lambda c: c[1], reverse=True)[0]

print(longest_call_duration[0], 'spent the longest time,', longest_call_duration[1],
      'seconds, on the phone during September 2016.')
```

#### Task 3 - O(n)
1. 1 loop among calls -> O(n)
2. 1 loop among calls (worst case all calls again) -> O(n)
3. 1 sorted function -> O(nlogn)
4. 1 loop among calls (worst case all calls again) -> O(n)

Total = O(n + n + nlogn + n) -> O(3n + nlogn) -> O(nlogn) 
```
called_from_banglore = [call[1] for call in calls if call[0][:5] == '(080)']
area_codes = [phone[:phone.find(')') + 1].replace('(', '').replace(')', '') if ')' in phone else phone[0:4] for phone in
              called_from_banglore]
print('The numbers called by people in Bangalore have codes:\n' + '\n'.join(sorted(set(area_codes))))

print('{0:.2f}'.format(
    (len([phone for phone in called_from_banglore if '(080)' in phone]) / len(called_from_banglore)) * 100),
    'percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.')
```

#### Task 4 - O(n^2)
Getting texters -> O(n)
Getting call_receivers -> O(n)
Getting marketers -> O(n) 
The sorted function at the end -> O(nlogn)
O(n + n + n + nlogn) -> O(3n + nlogn) -> O(nlogn) as final complexity
```
texters = {phone for text in texts for phone in text[:2]}
call_receivers = {call[1] for call in calls}
marketers = {call[0] for call in calls if call[0] not in texters and call[0] not in call_receivers}

print('These numbers could be telemarketers:')
print('\n'.join(sorted(marketers)))
```

