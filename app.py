from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_user():
    username = request.form['username']
    return redirect(url_for('welcome', username=username))

@app.route('/welcome/<username>')
def welcome(username):
    return f"Thanks for logging in, {username}!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
