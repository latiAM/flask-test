from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/1')
def details():
    return render_template('first_page.html')


@app.route('/2')
def rsvp():
    return render_template('second_page.html')


@app.route('/3')
def mem1():
    return render_template('mem1.html')


@app.route('/4')
def mem2():
    return render_template('mem2.html')


@app.route('/5')
def mem3():
    return render_template('mem3.html')


@app.route('/6')
def mem4():
    return render_template('mem4.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)
