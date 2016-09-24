from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    if(text == "ilidf10y"):
    	return "logged in"
    else:
        return "wrong password"	



if __name__ == '__main__':
    app.run()