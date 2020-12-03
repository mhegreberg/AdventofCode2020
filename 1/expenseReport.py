#Advent of Code day 1
#Mark Hegreberg
#

f = open("realReport.txt", "r")
report = f.read().splitlines()
report = [int(line) for line in report]


print(report)
# test = int(report[0])+int(report[1])
# print(test)
answer = 0
for line in report:
    for line2 in report:
        print(line+line2)
        if line+line2 == 2020:
            print("hit")
            answer = line*line2
            
print(answer)

