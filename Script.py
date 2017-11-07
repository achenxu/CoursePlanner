import os.path
import time
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

import csv

with open("testfiles/result.csv", "r") as f:
    reader = csv.reader(f)
    data = list(reader)

#coursesToExtract = ["CSE120", "CSE140", "CSE150"]#["CSE120", "CSE150", "CSE140", "ENGR191", "WRI100"]

coursesToExtract = []
s = raw_input("Please enter courses to filter (0 to exit): ")
if s == "0":
    quit()
while s != "0":
    coursesToExtract.append(s.upper())
    s = raw_input()
start = time.time()
classIDs = []
for d in data:
    if len(d) > 1:
        classIDs.append(d[1])
    else:
        classIDs.append("")

from Functions import extractValidSchedules, fetchTimes
validSchedules = extractValidSchedules(data, coursesToExtract, classIDs)

print("########################################")
for s in validSchedules:
    print(s["name"])
    days = {"M": [], "T": [], "W": [], "R": [], "F": []}
    for c in s["courses"]:
        print(c["crn"] + " - " + c["id"])
        print(c["times"])
    print("########################################")

end = time.time()
print("Valid schedules: " + str(len(validSchedules)))
print("in " + str(end - start) + " seconds")

