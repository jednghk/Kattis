'''while true (if n = 0, break)
    store every line into a list
    case 1: odd number of names
        have a new list and pop every even number element in orig list
        combine with old list
    case 2: even num of names
        actually the same


    print f'SET {set_num}' then loop to print out the entire list
'''
n = 0

while True:
    n += 1  # to print set number
    num_names = int(input())
    if num_names == 0:
        break
    else:
        name_list = []
        for line in range(num_names):  # loop to create list of names
            name_list.append(input())
        for i in range(num_names - 1, -1, -1):  # loop to rearrange list
            if i % 2 == 1:
                name_list.append(name_list.pop(i))

        print(f'SET {n}')
        for name in name_list:  # prints SET n and loops to print all names
            print(name)
