'''
1. split entire line
cursor: represented by index, when user is "typing",
        letters are (insert) into the list, index += 1
L: takes index and subtracts 1
R: takes index and adds 1
B: deletes character at that index
'''

raw_password = list(input())
cursor = 0
true_password = []

for keystroke in raw_password:
    if keystroke == 'L':
        cursor -= 1
    elif keystroke == 'R':
        cursor += 1
    elif keystroke == 'B':
        true_password.pop(cursor - 1)
        cursor -= 1
    else:
        true_password.insert(cursor, keystroke)
        cursor += 1

print(''.join(true_password))
