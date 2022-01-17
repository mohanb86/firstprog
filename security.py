# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 11:30:00 2021

@author: mobhaska
"""
from models.user import UserModel

def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and user.password == password:
        return user
    
def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_userid(user_id)