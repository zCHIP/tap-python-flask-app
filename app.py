from flask import Flask, render_template

app = Flask(__name__)


@app.route('/basepath')
def index():
    return render_template('index.html')