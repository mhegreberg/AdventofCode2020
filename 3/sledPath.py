# Advent of Code 2020
# Mark Hegreberg
# day three
# part one

x = 0
y = 0
xIter = 3
yIter = 1
treeCount=0
f=open("data.txt","r")
sledmap = f.read().splitlines()
print(sledmap)
width=len(sledmap[0])
length=len(sledmap)
print(width)
print(length)

for line in sledmap:
    if line[x % width] == "#":
        treeCount += 1
    x+=xIter

print(treeCount)
