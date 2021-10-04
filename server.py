from flask_app import app
from flask_app import socketio
from flask_app.controllers import users_controller, players_controller

""" if __name__ == "__main__":
    app.run(debug=True) """
    
if __name__ == '__main__':
    socketio.run(app, debug=True)
