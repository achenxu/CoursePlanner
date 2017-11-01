from HTMLParser import HTMLParser

#from Course import Course
#from Subject import Subject

class MyHTMLParser(HTMLParser):
    starts = []
    data = []
    toIgnore = ['CRN', 'Course #', 'Course Title', 'Units', 'Actv', 'Days', 'Time', 'Bldg/Rm', 'Start - End', 'Instructor', 'Max Enrl', 'Act Enrl', 'Seats Avail', 'Skip to top of page', 'Search Courses']
    passes = 0
    
    def handle_starttag(self, tag, attrs):
        self.starts.append(tag)
    
    def handle_endtag(self, tag):
        self.starts.pop()
    
    def handle_data(self, data):
        if len(self.starts) < 1:
            return
        if data in self.toIgnore:
            return

        if self.starts[len(self.starts) - 1] == 'h3':
            if data == "&":
                self.data[len(self.data)-1][0] = self.data[len(self.data)-1][0] + data
                self.passes = 1
            else:
                if self.passes == 0:
                    self.data.append([data, "subject"])
                else:
                    self.data[len(self.data)-1][0] = self.data[len(self.data)-1][0] + data
                    self.passes -= 1
        
        if self.starts[len(self.starts) - 1] == 'a':
            self.data.append([data, "crn"])

        if self.starts[len(self.starts) - 1] == 'small':
            if data == "&":
                self.data[len(self.data)-1][0] = self.data[len(self.data)-1][0] + data
                self.passes = 1
            else:
                if self.passes == 0:
                    self.data.append([data, "info"])
                else:
                    self.data[len(self.data)-1][0] = self.data[len(self.data)-1][0] + data
                    self.passes -= 1


parser = MyHTMLParser()
s = open("testfiles/long.html", "r").read()    # Extract from html file

parser.feed(s)                                  # Parse it into data elements (subject, crn, or info)

for info in parser.data:
    print(info)

datatoputinobjects = parser.data    # Needs another function to parse informations into the objects



