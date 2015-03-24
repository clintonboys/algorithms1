__author__ = 'cboys'

t = 6000
i=0
hashtable = {}
with open('algo1-programming_prob-2sum.txt') as f:
    for line in f:
        hashtable[int(line)] = i

with_distinct = 0

for n in range(-10000,10000):
    if n < 0:
        prog_tick = -n
    else:
        prog_tick = n + 10000
    if prog_tick % 200 == 0:
        print "Progress: " + str(20000/prog_tick)+"%"
    numbers_count = 0
    for i in range(0,len(hashtable)):
        try:
            y = hashtable[n-i]
            numbers_count = numbers_count + 1
        except KeyError:
            pass
    if numbers_count == 1:
        with_distinct = with_distinct + 1


print with_distinct
