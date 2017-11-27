import os.path
import time
# Download latest version of the page and check if it changed

if not os.path.isfile("testfiles/result.csv"):
    import Parser
elif os.path.getmtime("testfiles/result.csv")-time.time() > 3600:
    import Parser

import csv

with open("testfiles/result.csv", "r") as f:
    reader = csv.reader(f)
    data = list(reader)

#coursesToExtract = ["CSE120", "CSE140", "CSE150"]#["CSE120", "CSE150", "CSE140", "ENGR191", "WRI100"]

coursesToExtract = []
s = raw_input("Please enter courses to filter (0 to continue): ")
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

text_file = open("output.txt", "w")
print("########################################")
text_file.write("########################################")
for s in validSchedules:
    print(s["name"])
    text_file.write("{}\n".format(s["name"]))
    days = {"M": [], "T": [], "W": [], "R": [], "F": []}
    for c in s["courses"]:
        text_file.write("{} - {}\n".format(c["crn"], c["id"]))
        text_file.write("{}\n".format(c["times"]))
        print(c["crn"] + " - " + c["id"])
        print(c["times"])
    print("########################################")
    text_file.write("########################################")

text_file.close()
end = time.time()
print("Valid schedules: " + str(len(validSchedules)))
print("in " + str(end - start) + " seconds")
print("Output has been printed to output.txt")






