from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)
usr_pass = {"Jane":"1234","Mary":"hell0","rndm":"smh"}
employee_pass = {"Dino":"admin","Sam":"iusetd"}

@app.route('/')
def my_form():
    return render_template("index.html")

@app.route('/contact')
def contact():
  return render_template('contact.html')

@app.route('/signup')
def signup():
  return render_template('sign-up.html')

@app.route('/employee')
def creditPanel():
  return render_template('credit_panel.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/tables')
def tables():
  return render_template('tables.html')

#@app.route('/user')
#def user():
#  return render_template('user.html') 

@app.route('/', methods=['POST'])
def my_form_post():
    user = request.form['user']
    passw = request.form['pass']
    
    if(request.method == "POST"):
        if((user in usr_pass.keys())and (passw == usr_pass.get(user))):
            return render_template("user.html",number1 = "15",number2 = "25")
        if((user in employee_pass.keys())and (passw == employee_pass.get(user))):
            render_template("tables.html")
            return render_template("credit_panel.html")
        else:
            return render_template("sign-up.html")
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()