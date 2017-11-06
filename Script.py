import time
coursesToExtract = []
s = raw_input("Please enter courses to filter (0 to exit): ")

while s != "0":
    coursesToExtract.append(s.upper())
    s = raw_input()
start = time.time()

from Scheduler import findSchedules
validSchedules = findSchedules(coursesToExtract)

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

