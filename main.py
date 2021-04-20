from flask import Flask, redirect, render_template

app = Flask(__name__)


@app.route('/')
def to_go():
    return redirect('/theatre/main')


@app.route('/theatre/main')
def index():
    return render_template("main.html")


@app.route('/theatre/look_all')
def to_watch():
    return render_template('all_theatres.html')


@app.route('/theatre/to_watch/<theatre>')
def theatres(theatre):
    return render_template('theatre.html', info="", age="", adress="", link="")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')