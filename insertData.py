from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def login_page():
    return render_template("Login.html")
@app.route('/form')
def User_page():
    return render_template("UserPage.html")
@app.route('/register')
def User_reg():
    return render_template("RegisterPage.html")

if __name__ == '__main__':
   app.run()
