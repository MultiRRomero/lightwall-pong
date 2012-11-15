from flask import Flask

from game import GameState

app = Flask(__name__)

NUM_PLAYERS = 4
gameState = GameState(NUM_PLAYERS)

@app.route('/sync')
def syncSync():
    return gameState.serialize()

@app.route('/hello/<name>')
def greet(name='Stranger'):
    return 'Hello %s, how are you?' % name

if __name__ == "__main__":
    app.run(host='10.47.52.89', port=8080)
