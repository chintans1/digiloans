from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("testcommand.html")

@app.route('/', methods=['POST'])
def my_form_post():
    user = request.form['user']
    passw = request.form['pass']
    if(user == "123"):
    	return "logged in"
    else:
        return str((user,passw)).encode("utf8")	



if __name__ == '__main__':
    app.run()