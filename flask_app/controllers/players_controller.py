from flask_app import app
from flask_app import socketio
from flask import flash
from flask_app.models.player_model import Player
from flask_app.models.user_model import User
from flask import render_template, redirect, request, session


@app.route('/')
def localRedirect():
    return redirect('/home')


#DISPLAY GAME DASHBOARD
@app.route('/dashboard')
def GameControl():
    count_data = {
        "coop_count": 0,
        "cheat_count": 0,
    }
    session['count_data'] = count_data
    return render_template('game_dashboard.html', count=count_data)


#REGISTER NEW PLAYER PROCESS
@app.route('/player/process', methods=['POST'])
def registerPlayer():
    data = {# put the pw_hash into the data dictionary
        "number": request.form['number'],
        "coins":3,
        "hasVoted": False,
        # "coopCount": 0,
        # "cheatCount": 0,
    }

    
    
    session['player_data'] = data
    # player_data = Player.register_player(data)# Call the save @classmethod on player
    # print(f"I have added you to the database, player {player_data}")
    # store player id into session
    # print('player number is'+str(player_data[0].number))
    # number = player_data[0].number
    # print(f"Your session is {session}")
    print(f'player data is {data}')
    print(f"player number is {data['number']}")
    number = data['number']
    return redirect(f"/player/{number}")


#DISPLAY PLAYER SCREEN
@app.route('/player/<number>')
def playerScreen(number):
    data = session['player_data']
    print("Player Session Data is",data)
    return render_template('player.html', data=data)


# def messageReceived(methods=['GET', 'POST']):
#     print('message was received!!!')


# @app.route('/player/2')
# def Player2():
#     data = session['player_data']
#     return render_template('Player2.html', data=data)


def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')


@socketio.on('my event')#receives a message from chatForm
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)


@socketio.on('my vote')#receives data from coopForm or cheatForm
def handle_my_vote(json, methods=['GET', 'POST']):
    print('received my vote: ' + str(json))
    data = session['player_data']
    json['data']=data

    # count_data = session['count_data']
    # json['count_data']=count_data
    print("session data is",data)
    print("json data is",json['data']['number'],json['vote'])


# first check if they have voted. if yes, turn the session to True
# then check what their vote is. 

    """ if (session['hasVoted'] == False): //if they have voted
        data.hasVoted=True

    if (str(json['vote']) =='coop'):
        session['count_data']['coop_count'] = session['count_data']['coop_count']+1
        data = session['count_data']
        json['count_data'] = data
        print('new json count_data is: ' + str(json))

    if (str(json['vote']) =='cheat'):
        session['count_data']['cheat_count'] = session['count_data']['cheat_count']+1
        data = session['count_data']
        json['count_data']= data
        print('new json count_data is: ' + str(json)) """

    if (str(json['vote']) =='cheat' and data['number']=='1'):#if player 1 cheats
        session['player_data']['coins'] = session['player_data']['coins']+3
        data = session['player_data']
        json['data']=data
        print('new json data is: ' + str(json))


    if (str(json['vote']) =='coop' and data['number']=='2'):#if player 2 cooperates
        session['player_data']['coins'] = session['player_data']['coins']+2
        data = session['player_data']
        json['data']=data
        print('new json data is: ' + str(json))

    socketio.emit('my vote response', json, callback=messageReceived)

    # word = 5
    # socketio.emit('total vote counts', word, callback=messageReceived)






if __name__ == '__main__':
    socketio.run(app, debug=True)
