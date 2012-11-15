from flask import Flask
from threading import Thread

from game import GameState

app = Flask(__name__)

NUM_PLAYERS = 4
gameState = GameState(NUM_PLAYERS)
gameThread = Thread(target=gameState.run)

@app.route('/sync')
def syncSync():
    return gameState.serialize()

@app.route('/hello/<name>')
def greet(name='Stranger'):
    return 'Hello %s, how are you?' % name

if __name__ == "__main__":
    gameThread.start()
    app.run(host='10.47.52.89', port=8080)
