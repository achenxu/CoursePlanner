import os.path, time, csv
from Functions import extractValidSchedules, fetchTimes

# Find schedules
def findSchedules(coursesToExtract):
    updateDB()
    with open("testfiles/result.csv", "r") as f:
        reader = csv.reader(f)
        data = list(reader)

    classIDs = []
    for d in data:
        if len(d) > 1:
            classIDs.append(d[1])
        else:
            classIDs.append("")

    return extractValidSchedules(data, coursesToExtract, classIDs)

# Download latest version of the page and check if it changed
def updateDB():
    if not os.path.isfile("testfiles/result.csv"):
        import Parser
    elif os.path.getmtime("testfiles/result.csv")-time.time() > 3600:
        import Parser

def getClassIDs():
    with open("testfiles/result.csv", "r") as f:
        reader = csv.reader(f)
        data = list(reader)
    
    classIDs = []
    for d in data:
        if len(d) > 1:
            IDs = d[1].split("-")
            if len(IDs) >= 2:
                if (IDs[0] + IDs[1]) not in classIDs:
                    classIDs.append(IDs[0] + IDs[1])
    return classIDs
