# CoursePlanner
CoursePlanner is an open source tool to parse course information and help plan a schedule for next semester.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need python 2.7.13 installed on your machine.
Since it is a script at this stage, we don't need anything else installed yet.
We are running the scripts through the terminal.

### Running

Open up the terminal and cd into the project directory

```
cd <CoursePlanner folder>
```
Then run the script, it will put classes and info in a .csv file
```
python Script.py
```
This prompt will show up:
```
Please enter courses to filter (0 to exit):
```
Here is an example input:
```
cse140
cse150
cse165
cse120
0
```

Example output:
```
########################################
Schedule #1
14999 - CSE-140-01
[['MW', '1030-1145', '16-JAN 04-MAY'], ['S', '800-1100', '05-MAY 05-MAY']]
15000 - CSE-140-02L
[['W', '1330-1620', '16-JAN 04-MAY']]
15898 - CSE-150-01
[['MW', '1900-2015', '16-JAN 04-MAY'], ['S', '1130-1430', '05-MAY 05-MAY']]
15900 - CSE-150-03L
[['F', '1630-1920', '16-JAN 04-MAY']]
13813 - CSE-165-01
[['TR', '900-1015', '16-JAN 04-MAY'], ['T', '1500-1800', '08-MAY 08-MAY']]
13814 - CSE-165-02L
[['F', '730-1020', '16-JAN 04-MAY']]
15910 - CSE-120-01
[['WF', '1200-1315', '16-JAN 04-MAY'], ['M', '1500-1800', '07-MAY 07-MAY']]
15911 - CSE-120-02L
[['M', '730-1020', '16-JAN 04-MAY']]
########################################
Schedule #2
14999 - CSE-140-01
[['MW', '1030-1145', '16-JAN 04-MAY'], ['S', '800-1100', '05-MAY 05-MAY']]
15000 - CSE-140-02L
[['W', '1330-1620', '16-JAN 04-MAY']]
15898 - CSE-150-01
[['MW', '1900-2015', '16-JAN 04-MAY'], ['S', '1130-1430', '05-MAY 05-MAY']]
15900 - CSE-150-03L
[['F', '1630-1920', '16-JAN 04-MAY']]
13813 - CSE-165-01
[['TR', '900-1015', '16-JAN 04-MAY'], ['T', '1500-1800', '08-MAY 08-MAY']]
13815 - CSE-165-03L
[['F', '1330-1620', '16-JAN 04-MAY']]
15910 - CSE-120-01
[['WF', '1200-1315', '16-JAN 04-MAY'], ['M', '1500-1800', '07-MAY 07-MAY']]
15911 - CSE-120-02L
[['M', '730-1020', '16-JAN 04-MAY']]
########################################
Valid schedules: 2
in 0.0120759010315 seconds
```

## Built With

* Python 2.7.13 (so far)

## Contributing

Feel free to submit a pull request, however, make sure to pull the information often when we update the code base.
Please be descriptive in your pull requests as well.  

Make sure your branch names are short and descriptive.
Examples:
```
# good
$ git checkout -b oauth-migration

# bad - too vague
$ git checkout -b login_fix

# You can also use issue number as branch name
# GitHub issue #15 
$ git checkout -b issue-15
```

Feel free to reach out to us if you have any questions on anything or open up an issue.

