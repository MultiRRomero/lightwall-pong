from flask import Flask

app = Flask(__name__)

@app.route('/')
def whoo():
    return 'WHOA WHOO'

@app.route('/sync')
def syncSync():
    return '3,3\n2,3\n1,1\n'

@app.route('/abc')
def whoo():
    return 'WHOA WHOO ACX'

@app.route('/hello/<name>')
def greet(name='Stranger'):
    return 'Hello %s, how are you?' % name

if __name__ == "__main__":
    app.run(host='10.47.52.89', port=8080)
