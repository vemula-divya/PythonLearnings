from flask import Flask, render_template

app = Flask(__name__)
db = {'number': 0}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/reset')
def home():
    return render_template('index.html')


app.run(host='0.0.0.0', port=81)
