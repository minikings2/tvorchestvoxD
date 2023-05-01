import math
from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <!DOCTYPE html>
        <html>
        <head>
        <title>Уравнение</title>
        </head>
        <body>
        <h2><form method="POST" action="/submit">
            <b><label>Коэфф. 1:</label>
            <input type="text" name="var1"><br>
            <label>Коэфф. 2:</label>
            <input type="text" name="var2"><br>
            <label>Коэфф. 3:</label>
            <input type="text" name="var3"><br><br>
            <input type="submit"
            <button name="Далее" value="Отправить">
            <img style="vertical-align: middle; width: 240px;"
            </button></b></h2>
        </form>
        </body>
        </html>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    global K1
    global K2
    global K3
    K1 = int(request.form['var1'])
    K2 = int(request.form['var2'])
    K3 = int(request.form['var3'])
    global Dis
    Dis = K2**2-4*K1*K3
    return render_template('1step.html', K1=K1, K2=K2, K3=K3, Dis=Dis)

@app.route('/reshenie1', methods=['GET', 'POST'])
def reshenie1():
    if Dis>0:
        return redirect(url_for('reshenie3'))
    if Dis == 0:
        return redirect(url_for('reshenie2'))
    if Dis < 0:
        return render_template('2step.html')

@app.route('/reshenie2', methods=['GET', 'POST'])
def reshenie2():
    if Dis<0:
        return redirect(url_for('reshenie1'))
    if Dis>0:
        return redirect(url_for('reshenie3'))
    if Dis == 0:
        Resh:float = -K2/(2*K1)
    return render_template('3step.html', Resh=Resh, K2=K2, K1=K1)

@app.route('/reshenie3', methods=['GET', 'POST'])
def reshenie3():
    if Dis<0:
        return redirect(url_for('reshenie1'))
    if Dis == 0:
        return redirect(url_for('reshenie2'))
    if Dis>0:
        Resh1:float = (-K2+math.sqrt(Dis))/(2 * K1)
        Resh2:float = (-K2-math.sqrt(Dis))/(2 * K1)
    return render_template('4step.html', Resh1=Resh1, Resh2=Resh2, K2=K2, sDis=int(math.sqrt(Dis)), K1=K1)



if __name__ == '__main__':
    app.run(debug=True)
