from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def first_page():
    return render_template("FirstPage.html")
@app.route('/form')
def User_form():
    return render_template("NewTaxi.html")
@app.route('/reg')
def User_reg():
    return render_template("btst.html")

if __name__ == '__main__':
   app.run()
