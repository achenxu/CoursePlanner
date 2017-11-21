from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html', result={})

@app.route("/", methods=['POST'])
def loadCourses():
    from Scheduler import findSchedules
    print(request.form["classes"])
    coursesToExtract = request.form["classes"].upper().split(",")
    return render_template('index.html', result=findSchedules(coursesToExtract))

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
