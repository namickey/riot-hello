from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import send, emit

app = Flask('wa')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route("/")
def hello():
    return render_template('index.html')

@socketio.on('cast')
def cast(text):
    emit('update', text, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
