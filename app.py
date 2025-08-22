from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        return redirect(url_for('profile_setup'))
    return render_template('signup.html')

@app.route('/profile-setup', methods=['GET', 'POST'])
def profile_setup():
    if request.method == 'POST':
        return redirect(url_for('welcome'))
    return render_template('profile-setup.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
