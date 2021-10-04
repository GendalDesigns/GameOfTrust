from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.controllers import users_controller
from flask_app import app
from flask import flash
import re	# the regex module
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') # create a regular expression object that we'll use later

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @staticmethod
    def validate_register(data):
        is_valid = True
        if len(data['fname'])<2:
            flash('First Name is too short!')
            is_valid = False
        if len(data['lname'])<2:
            flash('Last Name is too short!')
            is_valid = False
        if len(data['email'])<2:
            flash('Email is too short!')
            is_valid = False
        if len(data['password'])<8:
            flash('Password is too short!')
            is_valid = False
        if (data['password'] != data['passwordConf']):
            flash('Passwords must match!')
            is_valid = False
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!")
            is_valid = False
        if is_valid:
            flash('Success!!')
        return is_valid


    #REGISTER NEW PARENT-USER
    @classmethod
    def register_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES(  %(first_name)s,  %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"
        results = connectToMySQL('game_of_trust_schema').query_db(query, data)
        return results


    #GET USER DATA BY CHECKING EMAIL
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("game_of_trust_schema").query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])


    #GET ONE USER
    @classmethod
    def get_one_user(cls, data):
        query = "SELECT * FROM users WHERE id=%(id)s;"
        results = connectToMySQL('game_of_trust_schema').query_db(query, data)
        return results

