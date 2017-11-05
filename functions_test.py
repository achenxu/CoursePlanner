import sys
from Functions import *
import pytest

# Mock variables and functions
time_string = '13:30-14:45'
expected_convert24h = '1:30-2:45pm'

# Start tests
def test_convert24h():
    assert convert24h(time_string) == expected_convert24h
    
def test_filterCourses():
    assert True

def test_generateAllPossibleClasses():
    assert True

def test_generatePermutationsFromData():
    assert True
    
