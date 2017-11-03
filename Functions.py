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
