""" from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)


@app.route('/')
def sessions():
    return render_template('GameControl.html')


@app.route('/control')
def GameControl():
    return render_template('GameControl.html')

@app.route('/player1')
def Player1():
    coinCount = 3
    return render_template('Player1.html', coinCount=coinCount)

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')


@app.route('/player2')
def Player2():
    coinCount = 3
    return render_template('Player1.html', coinCount=coinCount)


def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')



@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)


@socketio.on('my vote')
def handle_my_vote(json, methods=['GET', 'POST']):
    print('received my vote: ' + str(json))
    print (json['vote'])

    if (json['vote'] == 'cheat'):
        pass
    

    socketio.emit('my vote response', json, callback=messageReceived)


if __name__ == '__main__':
    socketio.run(app, debug=True)
 """