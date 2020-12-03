# Advent of Code Day 2
# Mark Hegreberg
# part two

import re

f = open("data.txt", "r")
inData = f.read().splitlines()
data = []
valid = 0
print(inData)
for line in inData:
    x = re.split('-| |: ',line)
    x[0] = int(x[0])
    x[1] = int(x[1])
    data.append(x)
print(data)

for line in data:
    password = line[3]
    test = 0
    if password[line[0]-1] == line[2] :
        test += 1
    if password[line[1]-1] == line[2] :
        test += 1
    if test == 1 :
        valid += 1
    
    
print(valid)
