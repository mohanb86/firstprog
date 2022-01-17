# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 11:36:43 2021

@author: mobhaska
"""
import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank.")
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank.")
    
    def post(self):
        
        data = UserRegister.parser.parse_args()
        
        if UserModel.find_by_username(data['username']):
            return {'message': 'Username already exists.'}, 400
        
        user = UserModel(**data)
        user.save_to_db()
        
        return {"message": "user created successfully."}, 201