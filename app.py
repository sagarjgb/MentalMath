from flask import Flask, render_template, request
import random as rd
import os
import time

app = Flask(__name__)

count = 0
score = 0
start_time = time.time()
end_time = time.time()
operatorList = ['+', '-', '/', '*']
a, b, operator = rd.randint(1, 100), rd.randint(
    1, 100), rd.choice(operatorList)
evalInput = str(a) + operator + str(b)
output = eval(evalInput)


@app.route('/')
@app.route('/index')
def index():
    global score
    global count
    score += 1
    global a
    global b
    global operator
    global evalInput
    global output
    global start_time
    start_time = time.time()
    a, b, operator = rd.randint(1, 100), rd.randint(
        1, 100), rd.choice(operatorList)
    evalInput = str(a) + str(operator) + str(b)
    output = eval(evalInput)
    if score == 10:
        tempcount = count
        tempscore = score
        score, count = -1, 0
        return render_template('index.html', count=tempcount, score=tempscore)
    return render_template('index.html', num1=a, num2=b, operator=operator, time=round(end_time-start_time))


@app.route('/result', methods=['POST', 'GET'])
def result():
    global count
    global score
    if request.method == 'GET':
        formOutput = request.args.get('val')
        print(formOutput, type(formOutput))
        print(output, "{:.1f}".format(output))
        if "{:.1f}".format(output) == "{:.1f}".format(float(formOutput)):
            count += 1
            return index()
        else:
            return index()

    return render_template('index.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='127.0.0.1', port=port)
