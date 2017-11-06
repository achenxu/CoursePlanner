from flask import Flask, render_template
app = Flask(__name__)
 
@app.route("/")
def home():
	return render_template('index.html')
 
if __name__ == "__main__":
	app.run()

@app.route("/", methods=['GET', 'POST'])
def loadSchedules():
	print 'hello'
	if request.method == 'POST':
		from Scheduler import findSchedules
		return render_template('index.html')
		
	else:
		return render_template('index.html')
