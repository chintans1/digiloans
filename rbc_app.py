from flask import Flask, render_template, redirect, url_for, request,url_for


app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():
    user = request.form['user']
    passw = request.form['pass']
    usr_pass = {"jane":"1234","Mary":"hell0","rndm":"smh"}
    if((user in usr_pass.keys())and (passw == usr_pass.get(user))):
    	return render_template("404.html")
    else:
        return render_template("sign-up.html")
if __name__ == '__main__':
    app.run()