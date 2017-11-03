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

def convert24h(s):
    bounds = s.split("-")
    hs = bounds[0].split(":")
    hf = bounds[1].split(":")
    if hf[1].count("pm") > 0:
        hf[0] = str(int(hf[0]) + 12)
        hf[1] = hf[1][0:2]
        if hs[0] > 9 and hs[0] != "12":
            hf[1] = str(int(hf[1]) + 12)
    else:
        hf[1] = hf[1][0:2]

    return hs[0] + ":" + hs[1] + "-" + hf[0] + ":" + hf[1]

coursesToExtract = ["CSE120", "CSE150", "CSE140", "PHYS009"]

courses = []

for i in range(1, len(data)):
    if len(data[i]) > 2:
        s = data[i][1].split("-")
        course = s[0] + s[1]
        if course in coursesToExtract:
            courses.append(data[i])
'''
for c in courses:
    print(c)
'''

lecture = courses[0][1].split("-")
section = ""
print(lecture)
info = ["", []]

for i in range(1, len(courses)):
    current = courses[i][1].split("-")
    
    if len(current[2]) > 2:
        if section == "" or section != current[2][0:2]:
            print(section)
            section = current[2][0:2]
    else:
        lecture = current
        print(lecture)





