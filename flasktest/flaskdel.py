from flask import Flask,request,render_template


app = Flask(__name__)

user = 'abc'

@app.route('/')
def index():
	return render_template('index.html',user=user)

@app.route('/udel')
def udel():
	user = request.args.get('user')	
	#print (user)
	return (user)
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=9013,debug=True)