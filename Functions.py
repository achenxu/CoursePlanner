def convert24h(s):
    bounds = s.split("-")
    hs = bounds[0].split(":")
    hf = bounds[1].split(":")
    if hf[1].count("pm") > 0:
        hf[0] = str(int(hf[0]) + 12)
        hf[1] = hf[1][0:2]
        if int(hs[0]) < 10 and hs[0] != "12":
            hs[0] = str(int(hs[0]) + 12)
    else:
        hf[1] = hf[1][0:2]
    
    return hs[0] + hs[1] + "-" + hf[0] + hf[1]

def filterCourses(coursesToExtract, data):
    courses = []
    for i in range(1, len(data)):
        if len(data[i]) > 2:
            s = data[i][1].split("-")
            course = s[0] + s[1]
            if course in coursesToExtract:
                courses.append(data[i])
    return courses

def generateAllPossibleClasses(courses):
    lecture = courses[0][1]
    section = ""
    sections = []
    currentSection = []
    for i in range(1, len(courses)):
        current = courses[i][1].split("-")
        if len(current[2]) > 2:
            if section == "" or section != current[2][0:2]:
                if section != "":
                    sections.append([lecture])
                    for s in currentSection:
                        sections[len(sections)-1].append(s)
                section = current[2][0:2]
                currentSection = [courses[i][1]]
            else:
                currentSection.append(courses[i][1])
        else:
            sections.append([lecture])
            for s in currentSection:
                sections[len(sections)-1].append(s)
            section = ""
            currentSection = []
            lecture = courses[i][1]

    sections.append([lecture])
    for s in currentSection:
        sections[len(sections)-1].append(s)
    section = ""
    lecture = ""
    return sections


def generatePermutationsFromData(data, coursesToExtract):
    courses = filterCourses(coursesToExtract, data)
    sections = generateAllPossibleClasses(courses)
    
    schedule = [[] for i in range(len(coursesToExtract))]
    for s in sections:
        name = s[0].split("-")
        schedule[coursesToExtract.index(name[0] + name[1])].append(s)
    n=1
    for s in schedule:
        n *= len(s)
    permutations = [[] for i in range(n)]
    for i in range(len(permutations)):
        n=1
        for s in schedule:
            permutations[i].append(s[i/n % len(s)])
            n *= len(s)
    return permutations

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

def getTimeTables(permutations, classIDs, data):
    timeTables = [[] for i in range(len(permutations))]
    for i in range(len(permutations)):
        for c in permutations[i]:
            for id in c:
                times = fetchTimes(id, data, classIDs)
                for t in times:
                    timeTables[i].append(t)
    return timeTables

def isOverlapping(time, times):
    time = time.split("-")
    for t in times:
        t = t.split("-")
        if (int(time[0]) >= int(t[0]) and int(time[0]) < int(t[1])) or (int(time[1]) > int(t[0]) and int(time[1]) <= int(t[1])):
            return False
    return True

def isValidPerm(timeTable):
    dict = {}
    for t in timeTable:
        if t[2] not in dict:
            dates = t[2].split(" ")
            if dates[0] == dates[1]:
                dict.update({t[2]:{t[0]:[]}})
            else:
                dict.update({t[2]:{"M":[], "T":[], "W":[], "R":[], "F":[], "S":[]}})
    
        for c in t[0]:
            timeStack = dict[t[2]][c]
            if not isOverlapping(t[1], timeStack):
                return False
            dict[t[2]][c].append(t[1])
    return True

def extractValidSchedules(data, coursesToExtract, classIDs):
    permutations = generatePermutationsFromData(data, coursesToExtract)
    timeTables = getTimeTables(permutations, classIDs, data)
    validPerms = []
    for i in range(len(timeTables)):
        if isValidPerm(timeTables[i]):
            validPerms.append(permutations[i])

    validSchedules = []
    number = 1

    for s in validPerms:
        dict = {"name": ("Schedule #" + str(number)), "courses": []}
        for courses in s:
            for classid in courses:
                i = classIDs.index(classid)
                course = {"id": classid, "crn": data[i][0], "times": fetchTimes(classid, data, classIDs)}
                dict["courses"].append(course)
        validSchedules.append(dict)
        number += 1
    return validSchedules
