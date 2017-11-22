from flask import Flask, render_template, request, jsonify
from Scheduler import findSchedules, getClassIDs

app = Flask(__name__)

@app.route("/")
def home():
    ids = getClassIDs()
    return render_template('index.html', autocomplete=ids)

@app.route("/", methods=['POST'])
def loadCourses():
    print(request.form["classes"])
    coursesToExtract = request.form["classes"].upper().split(",")
    ids = getClassIDs()
    return render_template('index.html', result=findSchedules(coursesToExtract), autocomplete=ids)

@app.route("/courses")
def loadSchedules():
    
    courses = request.args["courses"].split(",")
    coursesToExtract = []
    for c in courses:
        coursesToExtract.append(c.upper())
    
    print(coursesToExtract)
    
    from Scheduler import findSchedules
    schedules = findSchedules(coursesToExtract)
    return jsonify(schedules)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
