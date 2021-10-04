from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.controllers import players_controller
from flask_app import app
from flask import flash

class Player:
    def __init__(self, data):
        self.id = data['id']
        self.number = data['number']
        self.coins = data['coins']
        self.hasVoted = data['hasVoted']
        self.vote = data['vote']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']


    #REGISTER NEW PLAYER
    @classmethod
    def register_player(cls, data):
        query = "INSERT INTO players (number, coins, hasVoted, created_at, updated_at) VALUES(%(number)s, %(coins)s, %(hasVoted)s, NOW(), NOW());"
        results = connectToMySQL('game_of_trust_schema').query_db(query, data)
        return results


    # #GET ONE PLAYER
    # @classmethod
    # def get_one_player(cls, data):
    #     query = "SELECT * FROM players WHERE id=%(id)s;"
    #     results = connectToMySQL('game_of_trust_schema').query_db(query, data)
    #     return results


