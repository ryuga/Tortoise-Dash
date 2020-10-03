from flask import Flask, render_template, request, redirect, url_for
from utility import valuate_credentials, add_data
app = Flask(__name__)


@app.route('/index')
def home():
    return render_template('index.html')


@app.route('/bot/<path>')
def bot_pages(path):
    return render_template(f'bot-{path}.html')  # noqa


@app.route('/server/<path>')
def server_pages(path):
    return render_template(f'{path}.html')  # noqa


@app.route('/', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('accounts/login.html')
    elif request.method == "POST":
        username = request.form.get("username", None)
        password = request.form.get("password", None)
        if valuate_credentials(username, password):
            return redirect(url_for('home'))
        return render_template('accounts/login.html', msg="Account does not exist!")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template('accounts/register.html')
    elif request.method == "POST":
        username = request.form.get("username", None)
        password1 = request.form.get("password1", None)
        password2 = request.form.get("password2", None)
        if password1 == password2:
            add_data(username, password2)
            return redirect(url_for('login'))
        else:
            return render_template("accounts/register.html", msg="Passwords doesn't match!")


@app.route('/logout')
def logout():
    return redirect(url_for('login'))
