# Advent of Code Day 2
# Mark Hegreberg
# part one
import re
f = open("data.txt", "r")
inData = f.read().splitlines()
data = []
valid = 0
print(inData)
for line in inData:
    x = re.split('-| |: ',line)
    print(x)
    data.append(x)
print(data)

for line in data:
    count = line[3].count(line[2])
    print(line)
    print(count)
    if count >= int(line[0]) and count <= int(line[1]):
        valid+=1
        print("valid")
print(valid)
