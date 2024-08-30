from flask import Flask

app = Flask(__name__)

@app.route("/hello_rest_server", methods=['POST'])
def hello_rest1():
    return '안녕 난 rest server야'

if __name__ == '__main__':
    app.run()
