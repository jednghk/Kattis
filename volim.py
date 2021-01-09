'''
1. first input is current_pos of the popper
2. second is num of questions asked

3. have a accumulator variable time_elapsed
    if elapsed > 210, return current_pos
4. if T, current_pos += 1, else no change
5. make sure to print ans%8 in case the
'''

current_pos = int(input())
num_questions = int(input())
time_elapsed = 0
seq_events = []

for line in range(num_questions):  # preprocessing the input, creates a list of events
    duration, ans = input().split()
    duration = int(duration)
    seq_events.append((duration, ans))

for event in seq_events:
    time_elapsed += event[0]
    if time_elapsed > 210:
        break
    else:
        if event[1] == "T":
            current_pos += 1

if current_pos < 9:
    print(current_pos)
else:
    print(current_pos % 8)
