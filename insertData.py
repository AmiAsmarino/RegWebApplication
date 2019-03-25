from flask import Flask, render_template, request
from model import *

app = Flask(__name__)

@app.route('/')
def login_page():
    return render_template("Login.html")
@app.route('/form', methods=['POST'])
def User_page():
    pets =  TaxiUser.query.all()

    return render_template("UserPage.html", pets= pets)
@app.route('/register')
def User_reg():
    return render_template("RegisterPage.html")

@app.route('/mypage', methods=['GET','POST'])
def after_reg_new_user():
    if request.method == 'POST':
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        password = request.form.get('password')
        confPassword = request.form.get('confPassword')
        email = request.form.get('email')
        telephone = request.form.get('telephone')
        city = request.form.get('city')
        company = request.form.get('company')

        newuser = TaxiUser(firstName= firstName,lastName= lastName,password = password,
        conf_password = confPassword,email = email,
        phone_num= telephone,city= city,taxi_company = company)
        db.session.add(newuser)
        print(password)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            raise
        finally:
                db.session.close()
        db.session.commit()


        return render_template("Mypage.html", firstName= firstName)
    else :
        message = "Something went wrong"
        return render_template("error.html", message= message)

if __name__ == '__main__':
   app.debug = True
   app.run()
