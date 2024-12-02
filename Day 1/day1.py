import io
from pathlib import Path
import math


file_input = 'big'

list_1 = []
list_2 = []
with open(f'Day 1\\day1_{file_input}.txt', 'r') as input:
    for line in input:
        curr_line = line.split()
        list_1.append(int(curr_line[0]))
        list_2.append(int(curr_line[-1]))

# Part 1
# list_1.sort()
# list_2.sort()
# sum = 0

# for i in range(len(list_1)): # we know both lists have to have the same length
#     sum += abs(list_1[i] - list_2[i])

# print(sum)

# Part 2
counts = {}
sum = 0

# First make an inventory of the counts
for j in range(len(list_2)):
    if counts.get(list_2[j]): # If the item in list 2 is in the inventory add to the total
        counts[list_2[j]] = counts.get(list_2[j], 0) + 1
    else:
        counts[list_2[j]] = 1

# Then go through the left list and multiply by the counts
for i in range(len(list_1)): 
    sum += list_1[i] * counts.get(list_1[i], 0)

print(sum)

