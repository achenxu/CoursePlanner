from flask import Flask, render_template, request
app = Flask(__name__)
 
@app.route("/")
def home():
	return render_template('index.html')

@app.route("/courses")
def loadSchedules():
    
    print(request.form.input)
    
    coursesToExtract = request.args["courses"].split(",")
    for c in coursesToExtract:
        c = c.upper()
    
    from Scheduler import findSchedules
    schedules = findSchedules(coursesToExtract)
    return str(schedules)

if __name__ == "__main__":
	app.run()
