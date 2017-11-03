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

from Functions import filterCourses
courses = filterCourses(coursesToExtract, data)

from Functions import generateAllPossibleClasses
sections = generateAllPossibleClasses(courses)


schedule = [[] for i in range(len(coursesToExtract))]

for s in sections:
    name = s[0].split("-")
    schedule[coursesToExtract.index(name[0] + name[1])].append(s)

for s in schedule:
    print(s)
