from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/K5')
def k5():
    return render_template('index.html')


@app.route('/')
@app.route('/index')
def index():
    return 'К5'


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)