# https://open.kattis.com/problems/speedlimit
# while true, if not -1, check next n lines
# for each line split, convert to integer,
# take second num and subtract from prev num,
# then multiply numbers
# set prev num to current num and read t in next line
# print ans + 'miles'
# repeat loop until -1 is reached


while True:
    dist_driven = 0
    prev_elapsed = 0
    n = int(input())

    if n == -1:
        break
    else:
        for lines in range(n):
            # stores input speed and time as s and t respectively
            s, t = [int(x) for x in input().split()]
            final_t = t - prev_elapsed  # calculates time travelled at speed s
            dist_driven += s * final_t  # adds calculated distance to total
            prev_elapsed = t  # sets prev elapsed time to current t for next loop

    print(f'{dist_driven} miles')
