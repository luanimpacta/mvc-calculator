from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculator', methods=['POST', 'GET'])
def calculator():
    number1 = int(request.form['number1'])
    number2 = int(request.form['number2'])

    operation = request.form['operation']

    if operation == 'math':
        total = number1 + number2
    elif operation == 'sub':
        total = number1 - number2
    elif operation == 'mult':
        total = number1 * number2
    else:
        total = number1 / number2

    return str(total)


if __name__ == '__main__':
    app.debug = True
    app.run()
