from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '952003'
app.config['MYSQL_DB'] = 'Cash_Dash'
mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        if 'sign_up' in request.form:
            signUpDetails = request.form
            username = signUpDetails.get('username')
            password = signUpDetails.get('password')
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO sign_up(username, password) VALUES (%s, %s)", (username, password))
            mysql.connection.commit()
            cur.close()
            return redirect(url_for('user_deets', username=username))
        elif 'login' in request.form:
            loginDetails = request.form
            username = loginDetails.get('username')
            password = loginDetails.get('password')
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM sign_up WHERE username = %s AND password = %s", (username, password))
            account = cur.fetchone()
            cur.close()
            if account:
                return redirect(url_for('user_deets', username=username))
            else:
                return "Invalid username or password"

    return render_template('sign_up.html')

@app.route('/user_deets', methods=['GET', 'POST'])
def user_deets():
    if request.method == 'POST':
        userDeetsDetails = request.form
        username = userDeetsDetails.get('username')
        name = userDeetsDetails.get('name')
        email = userDeetsDetails.get('email')
        address = userDeetsDetails.get('address')
        phoneno = userDeetsDetails.get('phoneno')
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO user_deets(username, name, email, address, phone_no) VALUES (%s, %s, %s, %s, %s)", (username, name, email, address, phoneno))
        mysql.connection.commit()
        cur.close()
        return 'Success'
    return render_template('user_deets.html')

if __name__ == '__main__':
    app.run(debug=True)
