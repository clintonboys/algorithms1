__author__ = 'cboys'
from heapq import heappush, heappop

data = []
heap_low = []
heap_high = []

med = 0

with open('Median.txt') as f:
    for line in f:
        data.append(int(line))

heappush(heap_low, min([data[0],data[1]]))
med = med + data[0]
heappush(heap_high, -max([data[0], data[1]]))
med = med + min(data[0], data[1])


for item in data[2:]:

    if item < heap_high[0]:
        heappush(heap_high, -item)
    else:
        heappush(heap_low, item)
    if (len(heap_low) - len(heap_high) == 2):
        heappush(heap_high, -heappop(heap_low))
    elif (len(heap_high) - len(heap_low) == 2):
        heappush(heap_low, -heappop(heap_high))

    if len(heap_high) == len(heap_low):
        med = med +(heap_low[0]- heap_high[0])/2
    elif (len(heap_high) - len(heap_low) == 1):
        med = med - heap_high[0]
    else:
        med = med + heap_low[0]

print med % 10000

