from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/K5-pOyNPP')
def K5_pOyNPP():
    return render_template('index.html', kod='K5-pOyNPP', n='1', name='Никита')


@app.route('/K5-j4fmmm')
def K5_j4fmmm():
    return render_template('index.html', kod='K5-j4fmmm', n='2', name='Мохамед')


@app.route('/K5-svOAzJ')
def K5_svOAzJ():
    return render_template('index.html', kod='K5-svOAzJ', n='3', name='София')


@app.route('/K5-w3tuEw')
def K5_w3tuEw():
    return render_template('index.html', kod='K5-w3tuEw', n='4', name='Ярослав')


@app.route('/K5-Yka8qg')
def K5_Yka8qg():
    return render_template('index.html', kod='K5-Yka8qg', n='5', name='Анастасия')


@app.route('/K5-Tts4qw')
def K5_Tts4qw():
    return render_template('index.html', kod='K5-Tts4qw', n='6', name='Андрей')


@app.route('/K5-C26uws')
def K5_Tts4qw():
    return render_template('index.html', kod='K5-C26uws', n='7', name='Саша')


@app.route('/fate')
def res1():
    return "Первый пункт: https://t.me/+RmPHGfIuc7x_4yDz"

@app.route('/apologies')
def res2():
    return "5 людей - 5 проблем; нет первой - 5 удач"


@app.route('/')
@app.route('/index')
def index():
    return render_template('n.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
