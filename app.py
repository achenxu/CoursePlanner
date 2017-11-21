from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
 
@app.route("/", methods=['POST'])
def home():
    from Scheduler import findSchedules
    print(request.form["classes"])
    coursesToExtract = [request.form["classes"]]
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
	app.run()
