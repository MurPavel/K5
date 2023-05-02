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
    return render_template('index.html', kod='K5-Yka8qg', n='5', name='Никита')


@app.route('/')
@app.route('/index')
def index():
    return render_template('n.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
