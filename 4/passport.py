# Advent of Code 2020
# Mark Hegreberg
# day four
# part one

f=open("data.txt","r")
batch = f.read().splitlines()
batch.append("")
print(batch)
checks = {
    "byr" : False,
    "iyr" : False,
    "eyr" : False,
    "hgt" : False,
    "hcl" : False,
    "ecl" : False,
    "pid" : False,
    "cid" : False
    }

valid = True
validCount = 0
for line in batch:
    if len(line) == 0 :
        for test in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"): 
            if checks[test] == False:
                valid = False
        if valid == True:
            validCount+=1
            print("valid")
        else :
            valid = True
            print("invalid")
            
        checks = {
            "byr" : False,
            "iyr" : False,
            "eyr" : False,
            "hgt" : False,
            "hcl" : False,
            "ecl" : False,
            "pid" : False,
            "cid" : False
        }
    else:
        for test in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"): 
#            print(test)
#            print(line.find(test))
            if line.find(test) != -1:
                checks[test] = True
#            print(checks[test])
print(validCount)
