from flask import Flask, render_template, request
app = Flask(__name__)
 
@app.route("/")
def home():
	return render_template('index.html')

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
