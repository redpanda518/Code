from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World!'

@app.route('/projects/')
def projects():
	return 'The project page'

@app.route('/about/')
def about():
	return 'The about page'

#保证这个模块是在运行而不是被导入时使用
if __name__=='__main__':
	app.run(debug=True)