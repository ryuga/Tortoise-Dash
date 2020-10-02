from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/bot/<path>')
def bot_pages(path):
    return render_template(f'bot-{path}.html')  # noqa


@app.route('/server/<path>')
def server_pages(path):
    return render_template(f'{path}.html')  # noqa


if __name__ == '__main__':
    app.run(debug=True)
