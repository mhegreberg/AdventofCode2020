# Advent of Code 2020
# Mark Hegreberg
# day three
# part one

xIters = (1,3,5,7,1)
yIters = (1,1,1,1,2)
treeCount=0
treesCount=1

f=open("data.txt","r")
sledmap = f.read().splitlines()
# print(sledmap)
width=len(sledmap[0])
length=len(sledmap)
print(width)
print(length)

for i in range(0,5,1):
    x = 0
    y = -1

    for line in sledmap:
        y+=1
        if (yIters[i] == 2 and y%2 == 1):
            continue
        if line[x % width] == "#":
            treeCount += 1
        x+=xIters[i]
    treesCount *= treeCount
    print(treeCount)
    treeCount = 0
print(treesCount)
