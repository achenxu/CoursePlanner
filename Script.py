from HTMLParser import HTMLParser

from Course import Course
from Subject import Subject

class MyHTMLParser(HTMLParser):
    starts = []
    subjects = []
    courses = []
    
    currentCourse = []
    
    def handle_starttag(self, tag, attrs):
        self.starts.append(tag)
    
    def handle_endtag(self, tag):
        self.starts.pop()
    
    def handle_data(self, data):
        if len(self.starts) < 1:
            return

        if self.starts[len(self.starts) - 1] == 'h3':
            self.subjects.append(data)

        if self.starts[len(self.starts) - 1] == 'small':
            if data == "Must Also Register for a Corresponding Lab Section":
                return
            if data == "CRN":
                if len(self.currentCourse) > 3:
                    print(self.currentCourse[0] + "\t" + self.currentCourse[1]  + "\t" +  self.currentCourse[2]  + "\t" +  self.currentCourse[3])
                self.courses.append(self.currentCourse)
                self.currentCourse = []
            if data.count("-") == 2 and data.count(" ") == 0:
                print(self.currentCourse[0] + "\t" + self.currentCourse[1]  + "\t" +  self.currentCourse[2]  + "\t" +  self.currentCourse[3])
                self.courses.append(self.currentCourse)
                self.currentCourse = [data]
            else:
                self.currentCourse.append(data)


    def sortSubjects(self):
        newSubjects = []
        j = 0
        for i in range(len(self.subjects)-1):
            if (self.subjects[i+1] == '&'):
                newSubjects.append(self.subjects[i] + self.subjects[i+1] + self.subjects[i+2])
                j = 2
            else:
                if j == 0:
                    newSubjects.append(self.subjects[i])
                else:
                    j -= 1
        self.subjects = newSubjects


    def printSubjects(self):
        for subject in self.subjects:
            print("Subject", subject)









parser = MyHTMLParser()
s = open("long.html", "r").read()

parser.feed(s)

parser.sortSubjects()

parser.printSubjects()
