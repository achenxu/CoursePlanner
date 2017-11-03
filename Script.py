import os.path

# Download latest version of the page and check if it changed

if not os.path.isfile("testfiles/result.csv"):
    if os.path.isfile("testfiles/long.html"):
        import Parser
    else:
        quit()
else:
    if os.path.isfile("testfiles/long.html"):
        if os.path.getmtime("testfiles/long.html") > os.path.getmtime("testfiles/result.csv"):
            import Parser
    else:
        quit()

import csv

with open("testfiles/result.csv", "r") as f:
    reader = csv.reader(f)
    data = list(reader)

coursesToExtract = ["CSE120", "CSE150", "CSE180", "ENGR191"]
'''
s = raw_input("Please enter courses to filter (0 to exit): ")

while s != "0":
    coursesToExtract.append(s)
    s = raw_input()
'''
classIDs = []
for d in data:
    if len(d) > 1:
        classIDs.append(d[1])
    else:
        classIDs.append("")

from Functions import generatePermutationsFromData
permutations = generatePermutationsFromData(data, coursesToExtract)

for p in permutations:
    print(p)

timeTables = [[] for i in range(len(permutations))]
from Functions import convert24h
def fetchTimes(classID, data, classIDs):
    i = classIDs.index(classID)
    info = data[i]
    results = []
    results.append([info[5], convert24h(info[6]), info[8]])
    if len(info) > 14:
        results.append([info[14], convert24h(info[15]), info[17]])
    if len(info) > 19:
        results.append([info[19], convert24h(info[20]), info[22]])
    return results

for i in range(len(permutations)):
    for c in permutations[i]:
        for id in c:
            times = fetchTimes(id, data, classIDs)
            for t in times:
                timeTables[i].append(t)

for t in timeTables:
    print(t)
    print


