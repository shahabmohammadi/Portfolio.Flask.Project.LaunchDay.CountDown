from flask import Flask, render_template

app = Flask(__name__)

RELEASE_DATE = '2021/3/24'


@app.route('/')
def main():
    return render_template('index.html', RELEASE_DATE=RELEASE_DATE)
