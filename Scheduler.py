import os.path, time, csv
from Functions import extractValidSchedules, fetchTimes

# Find schedules
def findSchedules(coursesToExtract):
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
def updateDB:
    if not os.path.isfile("testfiles/result.csv"):
        if os.path.isfile("testfiles/long.html"):
        import Parser
        else:
        return
    else:
        if os.path.isfile("testfiles/long.html"):
        if os.path.getmtime("testfiles/long.html") > os.path.getmtime("testfiles/result.csv"):
            import Parser
