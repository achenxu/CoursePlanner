import sys
from Functions import *
import pytest

# Mock variables and functions
time_string = '1:30-2:45pm'
expected_convert24h = '1330-1445'




coursesToExtract = ['CSE120']

data = [['Column1', 'Column2', 'Column3', 'Column4', 'Column5', 'Column6', 'Column7', 'Column8', 'Column9', 'Column10', 'Column11', 'Column12', 'Column13'],
	['15910', 'CSE-120-01', 'Software Engineering', '4', 'LECT', 'WF', '12:00-1:15pm', 'COB2 140', '16-JAN 04-MAY', 'Leung', '60', '0', '60', 'EXAM', 'M', '3:00-6:00pm', 'COB2 140', '07-MAY 07-MAY'],
        ['15911', 'CSE-120-02L', 'Software Engineering', '0', 'LAB', 'M', '7:30-10:20am', 'CLSSRM 281', '16-JAN 04-MAY', 'Staff', '30', '0', '30'],
        ['15912', 'CSE-120-03L', 'Software Engineering', '0', 'LAB', 'M', '10:30-1:20pm', 'CLSSRM 281', '16-JAN 04-MAY', 'Staff', '30', '0', '30'],
        ['14999', 'CSE-140-01', 'Computer Architecture', '4', 'LECT', 'MW', '10:30-11:45am', 'CLSSRM 116', '16-JAN 04-MAY', 'Leung', '60', '1', '59', 'EXAM', 'S', '8:00-11:00am', 'CLSSRM 116', '05-MAY 05-MAY'],
        ['15000', 'CSE-140-02L', 'Computer Architecture', '0', 'LAB', 'W', '1:30-4:20pm', 'SCIENG 138', '16-JAN 04-MAY', 'Staff', '30', '0', '30'],
        ['15001', 'CSE-140-03L', 'Computer Architecture', '0', 'LAB', 'M', '7:30-10:20pm', 'SCIENG 138', '16-JAN 04-MAY', 'Staff', '30', '1', '29'],
        ['15898', 'CSE-150-01', 'Operating Systems', '4', 'LECT', 'MW', '7:00-8:15pm', 'KOLLIG 209', '16-JAN 04-MAY', 'Chandrasekhar', '60', '1', '59', 'EXAM', 'S', '11:30-2:30pm', 'SSB 130', '05-MAY 05-MAY'],
        ['15899', 'CSE-150-02L', 'Operating Systems', '0', 'LAB', 'W', '1:30-4:20pm', 'SCIENG 100', '16-JAN 04-MAY', 'Staff', '30', '0', '30'],
        ['15900', 'CSE-150-03L', 'Operating Systems', '0', 'LAB', 'F', '4:30-7:20pm', 'SCIENG 100', '16-JAN 04-MAY', 'Staff', '30', '1', '29']]

coursesExtracted = [['15910', 'CSE-120-01', 'Software Engineering', '4', 'LECT', 'WF', '12:00-1:15pm', 'COB2 140', '16-JAN 04-MAY', 'Leung', '60', '0', '60', 'EXAM', 'M', '3:00-6:00pm', 'COB2 140', '07-MAY 07-MAY'],
        ['15911', 'CSE-120-02L', 'Software Engineering', '0', 'LAB', 'M', '7:30-10:20am', 'CLSSRM 281', '16-JAN 04-MAY', 'Staff', '30', '0', '30'],
        ['15912', 'CSE-120-03L', 'Software Engineering', '0', 'LAB', 'M', '10:30-1:20pm', 'CLSSRM 281', '16-JAN 04-MAY', 'Staff', '30', '0', '30']]

allPossibleSections = [['CSE-120-01', 'CSE-120-02L'], ['CSE-120-01', 'CSE-120-03L']]

courses = ['CSE120', 'CSE140', 'CSE150']
permutations = [[['CSE-120-01', 'CSE-120-02L'], ['CSE-140-01', 'CSE-140-02L'], ['CSE-150-01', 'CSE-150-02L']], [['CSE-120-01', 'CSE-120-03L'], ['CSE-140-01', 'CSE-140-02L'], ['CSE-150-01', 'CSE-150-02L']], [['CSE-120-01', 'CSE-120-02L'], ['CSE-140-01', 'CSE-140-03L'], ['CSE-150-01', 'CSE-150-02L']], [['CSE-120-01', 'CSE-120-03L'], ['CSE-140-01', 'CSE-140-03L'], ['CSE-150-01', 'CSE-150-02L']], [['CSE-120-01', 'CSE-120-02L'], ['CSE-140-01', 'CSE-140-02L'], ['CSE-150-01', 'CSE-150-03L']], [['CSE-120-01', 'CSE-120-03L'], ['CSE-140-01', 'CSE-140-02L'], ['CSE-150-01', 'CSE-150-03L']], [['CSE-120-01', 'CSE-120-02L'], ['CSE-140-01', 'CSE-140-03L'], ['CSE-150-01', 'CSE-150-03L']], [['CSE-120-01', 'CSE-120-03L'], ['CSE-140-01', 'CSE-140-03L'], ['CSE-150-01', 'CSE-150-03L']]]

# Start tests
def test_convert24h():
    assert convert24h(time_string) == expected_convert24h
    
def test_filterCourses():
    assert filterCourses(coursesToExtract, data) == coursesExtracted

def test_generateAllPossibleClasses():
    assert generateAllPossibleClasses(coursesExtracted) == allPossibleSections

def test_generatePermutationsFromData():
    assert generatePermutationsFromData(data, courses) == permutations
    
