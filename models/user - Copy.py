# -*- coding: utf-8 -*-

import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))
    
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password
        
    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        select_query = "select * from users where username=?"
        result = cursor.execute(select_query, (username,))
        row = result.fetchone()
        if row:
            user = cls(row[0], row[1], row[2])
            #or we can use this command user = cls(*row)
        else:
            user = None
    
        connection.close()
        return user
    
    @classmethod
    def find_by_userid(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        select_query = "select * from users where id=?"
        result = cursor.execute(select_query, (username,))
        row = result.fetchone()
        if row:
            user = cls(row[0], row[1], row[2])
            #or we can use this command user = cls(*row)
        else:
            user = None
    
        connection.close()
        return user